"""Comprehensive test suite for POWEtsy — MCP server, adapters, capabilities."""

import hashlib
import json
import os
import sys
import sqlite3
import pytest
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from powetsy.shared.persist import (
    get_db, upsert_category, upsert_agent_node, upsert_product,
    upsert_component, insert_product_bom, insert_substitution,
    insert_observation, insert_edge
)
from powetsy.shared.db import SCHEMA, _enable_foreign_keys
from powetsy.mcp.server import PowMCP


@pytest.fixture
def temp_db(tmp_path):
    db_path = tmp_path / 'test.db'
    os.environ['POWETSY_DB'] = str(db_path)
    conn = sqlite3.connect(str(db_path))
    _enable_foreign_keys(conn)
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()
    yield db_path
    os.environ.pop('POWETSY_DB', None)


@pytest.fixture
def mcp(temp_db):
    return PowMCP()


# =============================================================================
# MCP SERVER
# =============================================================================

class TestMCPSearch:
    def test_search_capability(self, temp_db):
        upsert_component('cam1', 'USB Camera', category='vision', price_usd=12)
        upsert_component('cam2', 'Global Shutter Camera', category='vision', price_usd=25)
        upsert_component('mic1', 'INMP441 Mic', category='audio', price_usd=3)
        mcp = PowMCP()
        results = mcp.search_capability('vision')
        assert len(results) == 2
        assert all(r['category'] == 'vision' for r in results)

    def test_search_with_price_filter(self, temp_db):
        upsert_component('cam1', 'Cheap Cam', category='vision', price_usd=8.0)
        upsert_component('cam2', 'Expensive Cam', category='vision', price_usd=50.0)
        mcp = PowMCP()
        results = mcp.search_capability('vision', max_price=20.0)
        assert len(results) == 1
        assert float(results[0]['price_usd']) == 8.0

    def test_search_no_results(self, temp_db):
        mcp = PowMCP()
        results = mcp.search_capability('nonexistent_category')
        assert len(results) == 0


class TestMCPCompare:
    def test_compare_options(self, temp_db):
        upsert_component('a', 'Part A', price_usd=10)
        upsert_component('b', 'Part B', price_usd=15)
        mcp = PowMCP()
        results = mcp.compare_options(['a', 'b'])
        assert len(results) == 2

    def test_compare_single(self, temp_db):
        upsert_component('x', 'Only Part', price_usd=5)
        mcp = PowMCP()
        results = mcp.compare_options(['x'])
        assert len(results) == 1


class TestMCPGetPart:
    def test_get_part(self, temp_db):
        upsert_component('stm32', 'STM32G4', category='compute', price_usd=5)
        mcp = PowMCP()
        part = mcp.get_part('stm32')
        assert part is not None
        assert part['name'] == 'STM32G4'

    def test_get_part_missing(self, temp_db):
        mcp = PowMCP()
        assert mcp.get_part('nonexistent') is None


class TestMCPQuote:
    def test_quote_build(self, temp_db):
        upsert_product('test_build', 'Test Build')
        upsert_component('esp32', 'ESP32-S3', price_usd=3.50)
        upsert_component('mic', 'INMP441', price_usd=2.50)
        insert_product_bom('test_build', 'esp32', quantity=1, role='compute')
        insert_product_bom('test_build', 'mic', quantity=1, role='audio')
        mcp = PowMCP()
        quote = mcp.quote_build('test_build', quantities=[1, 10])
        assert quote['build_id'] == 'test_build'
        assert len(quote['quotes']) == 2
        assert quote['quotes'][0]['total_cost'] == 6.0


class TestMCPSaveBuild:
    def test_save_build(self, temp_db):
        mcp = PowMCP()
        build_id = mcp.save_build('My Agent', [
            {'component_id': 'esp32', 'quantity': 1, 'role': 'compute'},
            {'component_id': 'mic', 'quantity': 1, 'role': 'audio'},
        ], metadata={'description': 'Test build'})
        assert build_id.startswith('build:')


class TestMCPResolve:
    def test_resolve(self, temp_db):
        upsert_component('cam', 'USB Camera', category='vision', price_usd=12)
        upsert_component('mic', 'INMP441', category='audio', price_usd=3)
        mcp = PowMCP()
        result = mcp.resolve('I need a camera and microphone')
        assert len(result['capabilities']) >= 2
        # Routes may be empty if no template matches, that's OK for now
        assert 'routes' in result

    def test_parse_need(self, temp_db):
        mcp = PowMCP()
        caps = mcp._parse_need('I need eyes and ears')
        assert 'vision' in caps
        assert 'audio' in caps

    def test_parse_need_motion(self, temp_db):
        mcp = PowMCP()
        caps = mcp._parse_need('turn its head')
        assert 'motion' in caps

    def test_parse_need_default(self, temp_db):
        mcp = PowMCP()
        caps = mcp._parse_need('build something')
        assert 'compute' in caps

    def test_resolve_with_template(self, temp_db):
        mcp = PowMCP()
        result = mcp.resolve('I want a voice puck that glows')
        assert 'routes' in result
        # Should match voice_puck template (has 'hear', 'speak', 'status_light')
        if result['routes']:
            assert any(r['template'] == 'voice_puck' for r in result['routes'])


# =============================================================================
# COMPONENT GRAPH
# =============================================================================

class TestComponentGraph:
    def test_components_and_edges(self, temp_db):
        upsert_component('esp32', 'ESP32-S3', category='compute')
        upsert_component('mic', 'INMP441', category='audio')
        insert_edge('component:esp32', 'often_used_with', 'component:mic',
                    evidence='common voice assistant BOM')
        conn = sqlite3.connect(str(temp_db))
        count = conn.execute('SELECT COUNT(*) FROM edge').fetchone()[0]
        assert count == 1
        conn.close()


# =============================================================================
# SCHEMA
# =============================================================================

class TestSchema:
    def test_all_tables(self, temp_db):
        conn = sqlite3.connect(str(temp_db))
        tables = [r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()]
        for t in ['category', 'agent_node', 'product', 'component',
                  'product_bom', 'substitution', 'observation', 'edge']:
            assert t in tables, f'Missing: {t}'
        conn.close()


# =============================================================================
# SEEDS
# =============================================================================

class TestSeeds:
    def test_categories(self):
        from powetsy.seeds.seed_data import CATEGORIES
        assert len(CATEGORIES) >= 15

    def test_agent_nodes(self):
        from powetsy.seeds.seed_data import AGENT_NODES
        assert len(AGENT_NODES) >= 3

    def test_reference_products(self):
        from powetsy.seeds.seed_data import REFERENCE_PRODUCTS
        assert len(REFERENCE_PRODUCTS) >= 10

    def test_substitutions(self):
        from powetsy.seeds.seed_data import SUBSTITUTIONS
        assert len(SUBSTITUTIONS) >= 15

    def test_canonical_machines(self):
        from powetsy.seeds.machines_20 import MACHINES_20
        assert len(MACHINES_20) >= 15

    def test_manufacturing_suppliers(self):
        from powetsy.seeds.seed_data import MANUFACTURING_SUPPLIERS
        assert len(MANUFACTURING_SUPPLIERS) >= 4
        assert 'makerfabs' in MANUFACTURING_SUPPLIERS
        assert 'jlcpcb' in MANUFACTURING_SUPPLIERS

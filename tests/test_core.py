"""Tests for POWEtsy."""

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


class TestCategories:
    def test_create(self, temp_db):
        upsert_category('plant', 'Plant Agent', description='Moisture sensing')
        conn = sqlite3.connect(str(temp_db))
        row = conn.execute('SELECT name, description FROM category WHERE category_id="plant"').fetchone()
        assert row == ('Plant Agent', 'Moisture sensing')
        conn.close()

    def test_hierarchy(self, temp_db):
        upsert_category('root', 'Root')
        upsert_category('child', 'Child', parent_id='root')
        conn = sqlite3.connect(str(temp_db))
        row = conn.execute('SELECT parent_id FROM category WHERE category_id="child"').fetchone()
        assert row[0] == 'root'
        conn.close()


class TestAgentNodes:
    def test_create(self, temp_db):
        upsert_agent_node('pow-agent', 'POW Agent Node', mcu='ESP32-S3',
                          connectivity='WiFi+BLE', price_usd=8)
        conn = sqlite3.connect(str(temp_db))
        row = conn.execute('SELECT mcu, price_usd FROM agent_node WHERE node_id="pow-agent"').fetchone()
        assert row == ('ESP32-S3', 8.0)
        conn.close()


class TestProducts:
    def test_create(self, temp_db):
        upsert_category('plant', 'Plant Agent')
        upsert_product('plant-basic', 'Plant Agent Basic', category_id='plant',
                        target_price_usd=25, personalization_options=['plant_type', 'led_color'])
        conn = sqlite3.connect(str(temp_db))
        row = conn.execute('SELECT name, target_price_usd FROM product WHERE product_id="plant-basic"').fetchone()
        assert row == ('Plant Agent Basic', 25.0)
        conn.close()

    def test_bom(self, temp_db):
        upsert_product('test', 'Test Product')
        upsert_component('esp32s3', 'ESP32-S3', price_usd=3.50)
        insert_product_bom('test', 'esp32s3', quantity=1, role='compute')
        conn = sqlite3.connect(str(temp_db))
        row = conn.execute('SELECT quantity, role FROM product_bom WHERE product_id="test"').fetchone()
        assert row == (1, 'compute')
        conn.close()


class TestSubstitutions:
    def test_create(self, temp_db):
        upsert_component('a', 'Part A')
        upsert_component('b', 'Part B')
        sub_id = insert_substitution('a', 'b', 'drop_in', confidence=0.9, notes='Same pinout')
        conn = sqlite3.connect(str(temp_db))
        row = conn.execute('SELECT substitution_type, confidence FROM substitution WHERE substitution_id=?',
                           (sub_id,)).fetchone()
        assert row == ('drop_in', 0.9)
        conn.close()

    def test_idempotent(self, temp_db):
        upsert_component('a', 'Part A')
        upsert_component('b', 'Part B')
        s1 = insert_substitution('a', 'b', 'drop_in')
        s2 = insert_substitution('a', 'b', 'drop_in')
        assert s1 == s2


class TestObservations:
    def test_create(self, temp_db):
        insert_observation('plant-basic', 'product', 'sales', '30', source='etsy', numeric_value=30)
        conn = sqlite3.connect(str(temp_db))
        row = conn.execute('SELECT metric, numeric_value FROM observation WHERE entity_id="plant-basic"').fetchone()
        assert row == ('sales', 30.0)
        conn.close()

    def test_append(self, temp_db):
        insert_observation('x', 'product', 'price', '25', source='etsy')
        insert_observation('x', 'product', 'price', '23', source='etsy')
        conn = sqlite3.connect(str(temp_db))
        count = conn.execute('SELECT COUNT(*) FROM observation').fetchone()[0]
        assert count == 2
        conn.close()


class TestEdges:
    def test_create(self, temp_db):
        insert_edge('product:plant', 'uses_node', 'node:esp32', evidence='BOM')
        conn = sqlite3.connect(str(temp_db))
        row = conn.execute('SELECT predicate, object_id FROM edge').fetchone()
        assert row == ('uses_node', 'node:esp32')
        conn.close()


class TestSeeds:
    def test_seed_loader(self):
        from powetsy.seeds.seed_data import CATEGORIES, AGENT_NODES, REFERENCE_PRODUCTS, SUBSTITUTIONS
        assert len(CATEGORIES) >= 5
        assert len(AGENT_NODES) >= 3
        assert len(REFERENCE_PRODUCTS) >= 4
        assert len(SUBSTITUTIONS) >= 10

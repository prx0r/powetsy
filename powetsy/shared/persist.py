"""Persistence for POWEtsy."""

import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from powetsy.shared.db import get_db, _enable_foreign_keys


def upsert_category(category_id, name, parent_id=None, description=''):
    conn = get_db()
    conn.execute(
        "INSERT OR REPLACE INTO category (category_id, name, parent_id, description) "
        "VALUES (?, ?, ?, ?)",
        (category_id, name, parent_id, description)
    )
    conn.commit()
    conn.close()


def upsert_agent_node(node_id, name, mcu='', connectivity='', io_json='',
                       price_usd=None, description=''):
    conn = get_db()
    conn.execute(
        "INSERT OR REPLACE INTO agent_node (node_id, name, mcu, connectivity, "
        "io_json, price_usd, description) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (node_id, name, mcu, connectivity, io_json, price_usd, description)
    )
    conn.commit()
    conn.close()


def upsert_product(product_id, name, category_id=None, description='',
                    target_price_usd=None, personalization_options=None):
    conn = get_db()
    now = datetime.now(timezone.utc).isoformat()
    conn.execute(
        "INSERT INTO product (product_id, name, category_id, description, "
        "target_price_usd, personalization_options_json, first_seen_at, last_seen_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(product_id) DO UPDATE SET "
        "name=excluded.name, last_seen_at=excluded.last_seen_at",
        (product_id, name, category_id, description, target_price_usd,
         json.dumps(personalization_options or {}), now, now)
    )
    conn.commit()
    conn.close()


def upsert_component(component_id, name, category='', mpn='',
                      manufacturer='', description='', price_usd=None,
                      voltage='', interface=''):
    conn = get_db()
    now = datetime.now(timezone.utc).isoformat()
    conn.execute(
        "INSERT INTO component (component_id, name, category, mpn, manufacturer, "
        "description, price_usd, voltage, interface, first_seen_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(component_id) DO UPDATE SET name=excluded.name, price_usd=excluded.price_usd",
        (component_id, name, category, mpn, manufacturer, description,
         price_usd, voltage, interface, now)
    )
    conn.commit()
    conn.close()


def insert_product_bom(product_id, component_id, quantity=1, role='', notes=''):
    conn = get_db()
    conn.execute(
        "INSERT INTO product_bom (product_id, component_id, quantity, role, notes) "
        "VALUES (?, ?, ?, ?, ?)",
        (product_id, component_id, quantity, role, notes)
    )
    conn.commit()
    conn.close()


def insert_substitution(src_id, dst_id, stype, confidence=0.5, notes='', source=''):
    raw = f'{src_id}:{dst_id}:{stype}'
    sub_id = hashlib.sha256(raw.encode()).hexdigest()[:16]
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO substitution (substitution_id, src_component_id, dst_component_id, "
            "substitution_type, confidence, notes, source) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (sub_id, src_id, dst_id, stype, confidence, notes, source)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()
    return sub_id


def insert_observation(entity_id, entity_type, metric, value, source='',
                        numeric_value=None):
    conn = get_db()
    conn.execute(
        "INSERT INTO observation (entity_id, entity_type, metric, value, "
        "numeric_value, observed_at, source) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (entity_id, entity_type, metric, value, numeric_value,
         datetime.now(timezone.utc).isoformat(), source)
    )
    conn.commit()
    conn.close()


def insert_edge(subject_id, predicate, object_id, evidence='', confidence=1.0):
    raw = f'{subject_id}:{predicate}:{object_id}'
    edge_id = hashlib.sha256(raw.encode()).hexdigest()[:16]
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO edge (edge_id, subject_id, predicate, object_id, evidence, confidence) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (edge_id, subject_id, predicate, object_id, evidence, confidence)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()
    return edge_id

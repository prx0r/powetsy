"""Database — canonical schema for POWEtsy."""

import os
import sqlite3
from pathlib import Path


def get_db_path() -> Path:
    return Path(os.environ.get('POWETSY_DB', str(Path(__file__).parent.parent.parent / 'warehouse' / 'powetsy.db')))


SCHEMA = """
-- Source infrastructure
CREATE TABLE IF NOT EXISTS source_registry (
    source_id TEXT PRIMARY KEY, name TEXT NOT NULL, authority TEXT,
    access_method TEXT, cadence TEXT, requires_auth INTEGER DEFAULT 0,
    enabled INTEGER DEFAULT 1
);
CREATE TABLE IF NOT EXISTS raw_blob (
    sha256 TEXT PRIMARY KEY, source_id TEXT NOT NULL, content_type TEXT,
    content_length INTEGER, storage_path TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS raw_acquisition (
    acquisition_id INTEGER PRIMARY KEY AUTOINCREMENT, source_id TEXT NOT NULL,
    retrieved_at TEXT NOT NULL, request_url TEXT, http_status INTEGER,
    sha256 TEXT NOT NULL, FOREIGN KEY (sha256) REFERENCES raw_blob(sha256)
);
CREATE TABLE IF NOT EXISTS source_record (
    source_record_id TEXT PRIMARY KEY, source_id TEXT NOT NULL, dataset TEXT NOT NULL,
    source_native_id TEXT, retrieved_at TEXT NOT NULL, normalized_json TEXT NOT NULL,
    payload_hash TEXT NOT NULL, parser_id TEXT NOT NULL, parser_version TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS collector_run (
    run_id INTEGER PRIMARY KEY AUTOINCREMENT, source_id TEXT NOT NULL,
    started_at TEXT NOT NULL DEFAULT (datetime('now')), finished_at TEXT,
    status TEXT DEFAULT 'running', records_new INTEGER DEFAULT 0, error TEXT
);

-- === PRODUCT CATEGORIES ===
CREATE TABLE IF NOT EXISTS category (
    category_id TEXT PRIMARY KEY, name TEXT NOT NULL, parent_id TEXT,
    description TEXT,
    FOREIGN KEY (parent_id) REFERENCES category(category_id)
);

-- === AGENT NODES (reusable control cores) ===
CREATE TABLE IF NOT EXISTS agent_node (
    node_id TEXT PRIMARY KEY, name TEXT NOT NULL, description TEXT,
    mcu TEXT, connectivity TEXT, io_json TEXT, price_usd REAL,
    first_seen_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- === PRODUCTS (physical AI agents) ===
CREATE TABLE IF NOT EXISTS product (
    product_id TEXT PRIMARY KEY, name TEXT NOT NULL, category_id TEXT,
    description TEXT, target_price_usd REAL,
    personalization_options_json TEXT,
    first_seen_at TEXT NOT NULL DEFAULT (datetime('now')),
    last_seen_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);

-- === COMPONENTS (parts used in products) ===
CREATE TABLE IF NOT EXISTS component (
    component_id TEXT PRIMARY KEY, name TEXT NOT NULL, category TEXT,
    mpn TEXT, manufacturer TEXT, description TEXT,
    price_usd REAL, voltage TEXT, interface TEXT,
    first_seen_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- === PRODUCT BOM ===
CREATE TABLE IF NOT EXISTS product_bom (
    id INTEGER PRIMARY KEY AUTOINCREMENT, product_id TEXT NOT NULL,
    component_id TEXT NOT NULL, quantity INTEGER DEFAULT 1,
    role TEXT, notes TEXT,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (component_id) REFERENCES component(component_id)
);

-- === SUBSTITUTIONS ===
CREATE TABLE IF NOT EXISTS substitution (
    substitution_id TEXT PRIMARY KEY,
    src_component_id TEXT NOT NULL, dst_component_id TEXT NOT NULL,
    substitution_type TEXT NOT NULL, confidence REAL DEFAULT 0.5,
    notes TEXT, source TEXT,
    FOREIGN KEY (src_component_id) REFERENCES component(component_id),
    FOREIGN KEY (dst_component_id) REFERENCES component(component_id)
);

-- === OBSERVATIONS (price, sales, demand signals) ===
CREATE TABLE IF NOT EXISTS observation (
    observation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id TEXT NOT NULL, entity_type TEXT NOT NULL,
    metric TEXT NOT NULL, value TEXT, numeric_value REAL,
    observed_at TEXT NOT NULL, source TEXT
);

-- === EDGES (cross-repo links) ===
CREATE TABLE IF NOT EXISTS edge (
    edge_id TEXT PRIMARY KEY, subject_id TEXT NOT NULL,
    predicate TEXT NOT NULL, object_id TEXT NOT NULL,
    evidence TEXT, confidence REAL DEFAULT 1.0
);

-- === PERSONALIZATION PROFILES ===
CREATE TABLE IF NOT EXISTS personalization_profile (
    profile_id TEXT PRIMARY KEY, name TEXT, product_id TEXT,
    customization_json TEXT, created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

-- === INDEXES ===
CREATE INDEX IF NOT EXISTS idx_product_category ON product(category_id);
CREATE INDEX IF NOT EXISTS idx_product_bom_product ON product_bom(product_id);
CREATE INDEX IF NOT EXISTS idx_product_bom_component ON product_bom(component_id);
CREATE INDEX IF NOT EXISTS idx_substitution_src ON substitution(src_component_id);
CREATE INDEX IF NOT EXISTS idx_obs_entity ON observation(entity_id);
CREATE INDEX IF NOT EXISTS idx_obs_time ON observation(observed_at);
CREATE INDEX IF NOT EXISTS idx_edge_subject ON edge(subject_id);
CREATE INDEX IF NOT EXISTS idx_edge_object ON edge(object_id);
"""


def _enable_foreign_keys(conn):
    conn.execute("PRAGMA foreign_keys=ON")


def get_db():
    db_path = get_db_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    _enable_foreign_keys(conn)
    conn.executescript(SCHEMA)
    conn.commit()
    return conn


def init_db():
    db_path = get_db_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    _enable_foreign_keys(conn)
    conn.executescript(SCHEMA)
    conn.commit()
    print(f'Database initialized: {db_path}')
    return conn


def status():
    conn = get_db()
    tables = [r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()]
    print('=== DATABASE STATUS ===')
    for t in tables:
        try:
            count = conn.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
            if count > 0:
                print(f'  {t:35s} {count:>8,}')
        except:
            pass
    conn.close()


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'status':
        status()
    else:
        init_db()

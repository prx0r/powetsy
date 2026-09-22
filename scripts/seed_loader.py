"""Seed loader for POWEtsy."""

import os
import sys
import json
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from powetsy.shared.persist import (
    upsert_category, upsert_agent_node, upsert_product,
    upsert_component, insert_product_bom, insert_substitution, get_db
)
from powetsy.seeds.seed_data import CATEGORIES, AGENT_NODES, REFERENCE_PRODUCTS, SUBSTITUTIONS


def main():
    print('=== POWETSY SEED LOADER ===\n')

    # Categories
    for cat_id, cat_data in CATEGORIES.items():
        upsert_category(cat_id, cat_data['name'], description=cat_data['description'])
    print(f'  Loaded {len(CATEGORIES)} categories')

    # Agent nodes
    for node_id, node_data in AGENT_NODES.items():
        upsert_agent_node(
            node_id, node_data['name'],
            mcu=node_data.get('mcu', ''),
            connectivity=node_data.get('connectivity', ''),
            io_json=json.dumps(node_data.get('io', [])),
            price_usd=node_data.get('price_usd'),
            description=node_data.get('description', '')
        )
    print(f'  Loaded {len(AGENT_NODES)} agent nodes')

    # Products
    for prod_id, prod_data in REFERENCE_PRODUCTS.items():
        upsert_product(
            prod_id, prod_data['name'],
            category_id=prod_data.get('category'),
            description=prod_data.get('description', ''),
            target_price_usd=prod_data.get('target_price_usd'),
            personalization_options=prod_data.get('personalization')
        )
        # BOM
        for item in prod_data.get('bom', []):
            comp_id = item['component']
            upsert_component(comp_id, comp_id)
            insert_product_bom(prod_id, comp_id,
                                quantity=item.get('qty', 1),
                                role=item.get('role', ''))
    print(f'  Loaded {len(REFERENCE_PRODUCTS)} reference products')

    # Substitutions
    for src, dst, stype, conf, notes in SUBSTITUTIONS:
        insert_substitution(src, dst, stype, confidence=conf, notes=notes)
    print(f'  Loaded {len(SUBSTITUTIONS)} substitutions')

    # Status
    print('\n=== DATABASE STATUS ===')
    conn = get_db()
    for t in ['category', 'agent_node', 'product', 'component',
              'product_bom', 'substitution']:
        try:
            count = conn.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
            print(f'  {t:25s} {count:>6}')
        except:
            pass
    conn.close()


if __name__ == '__main__':
    main()

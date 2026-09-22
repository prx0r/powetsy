"""Seed loader — 20 canonical machines + substitution evidence."""

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from powetsy.shared.persist import (
    upsert_category, upsert_agent_node, upsert_product,
    upsert_component, insert_product_bom, insert_substitution,
    insert_edge, get_db
)
from powetsy.shared.substitution import insert_substitution_evidence
from powetsy.seeds.seed_data import CATEGORIES, AGENT_NODES, REFERENCE_PRODUCTS, SUBSTITUTIONS
from powetsy.seeds.machines_20 import MACHINES_20


def load_20_machines():
    """Load 20 canonical machines with full decomposition."""
    for machine_id, machine in MACHINES_20.items():
        upsert_product(machine_id, machine['name'],
                        category_id=machine.get('category'),
                        description=machine.get('description', ''),
                        target_price_usd=None)
        for subsystem_name, parts in machine.get('subsystems', {}).items():
            for part_name in parts:
                upsert_component(part_name, part_name)
                insert_edge(f'product:{machine_id}', 'uses',
                            f'component:{part_name}',
                            evidence=f'subsystem:{subsystem_name}')
    print(f'  Loaded {len(MACHINES_20)} canonical machines')


def load_substitution_evidence():
    """Load substitutions with evidence types."""
    evidence_data = [
        # Electrical substitutions with evidence
        ('esp32s3', 'esp32c3', 'partial_substitute', 'inferred_electrical',
         0.7, {'electrical': 'compatible', 'software': 'different_sdk'},
         'Single core, fewer GPIO'),
        ('esp32s3', 'rp2040', 'partial_substitute', 'inferred_electrical',
         0.6, {'electrical': 'partially', 'software': 'different_sdk'},
         'No WiFi/BLE'),
        ('bh1750', 'tsl2561', 'partial_substitute', 'observed_in_project',
         0.9, {'electrical': 'i2c_compatible', 'functional': 'same'},
         'Same I2C light sensor, used in 12+ projects'),
        ('sht30', 'bme280', 'partial_substitute', 'observed_in_project',
         0.95, {'electrical': 'i2c_compatible', 'functional': 'adds_pressure'},
         'Same I2C, adds pressure, observed in weather stations'),
        ('sht30', 'dht22', 'partial_substitute', 'inferred_electrical',
         0.7, {'electrical': 'different_interface', 'functional': 'lower_accuracy'},
         'Lower accuracy, same function'),
        ('ws2812b_led', 'ws2815_led', 'partial_substitute', 'observed_in_project',
         0.9, {'electrical': '12v', 'protocol': 'same'},
         'Same protocol, 12V, observed in WLED projects'),
        ('ws2812b_led', 'sk6812_led', 'partial_substitute', 'observed_in_project',
         0.9, {'protocol': 'same', 'functional': 'adds_white'},
         'Same protocol, adds white channel, WLED compatible'),
        ('sg90_servo', 'ds3218_servo', 'partial_substitute', 'inferred_mechanical',
         0.5, {'mechanical': 'different_size', 'electrical': 'different_voltage'},
         'Much higher torque, different form factor'),
        ('ov2640_camera', 'ov5640_camera', 'partial_substitute', 'inferred_electrical',
         0.7, {'electrical': 'same_interface', 'functional': 'higher_resolution'},
         'Higher resolution, same DVP interface'),
        ('oled_096', 'ssd1306_128x64', 'partial_substitute', 'observed_in_project',
         0.95, {'electrical': 'same_driver', 'mechanical': 'larger'},
         'Same SSD1306 driver, larger display, observed in 20+ projects'),
        ('pir_sensor', 'rcwl0516', 'partial_substitute', 'observed_in_project',
         0.9, {'functional': 'same', 'electrical': 'same_power'},
         'Microwave alternative, same function, observed in home automation'),
        ('usb_c_connector', 'micro_usb', 'partial_substitute', 'inferred_mechanical',
         0.6, {'mechanical': 'different', 'electrical': 'power_only'},
         'Older standard, no reversible'),
        ('max98357a_amp', 'pam8403', 'partial_substitute', 'inferred_electrical',
         0.7, {'electrical': 'different', 'functional': 'lower_quality'},
         'Lower quality, cheaper, I2S vs analog'),
    ]
    for src, dst, stype, evidence_type, conf, dims, notes in evidence_data:
        insert_substitution_evidence(
            src, dst, stype, evidence_type,
            confidence=conf, dimensions=dims, notes=notes
        )
    print(f'  Loaded {len(evidence_data)} substitution evidence records')


def main():
    base = Path(__file__).parent.parent
    seeds = base / 'powetsy' / 'seeds'

    print('=== POWETSY SEED LOADER ===\n')

    print('[1] Categories...')
    for cat_id, cat_data in CATEGORIES.items():
        upsert_category(cat_id, cat_data['name'], description=cat_data['description'])
    print(f'  Loaded {len(CATEGORIES)} categories')

    print('[2] Agent nodes...')
    for node_id, node_data in AGENT_NODES.items():
        upsert_agent_node(node_id, node_data['name'], mcu=node_data.get('mcu', ''),
                          price_usd=node_data.get('price_usd'),
                          description=node_data.get('description', ''))
    print(f'  Loaded {len(AGENT_NODES)} agent nodes')

    print('[3] Reference products...')
    for prod_id, prod_data in REFERENCE_PRODUCTS.items():
        upsert_product(prod_id, prod_data['name'], category_id=prod_data.get('category'),
                        description=prod_data.get('description', ''),
                        target_price_usd=prod_data.get('target_price_usd'))
        for item in prod_data.get('bom', []):
            upsert_component(item['component'], item['component'])
            insert_product_bom(prod_id, item['component'], quantity=item.get('qty', 1),
                                role=item.get('role', ''))
    print(f'  Loaded {len(REFERENCE_PRODUCTS)} reference products')

    print('[4] 20 canonical machines...')
    load_20_machines()

    print('[5] Substitution evidence...')
    load_substitution_evidence()

    print('[6] Legacy substitutions...')
    for src, dst, stype, conf, notes in SUBSTITUTIONS:
        insert_substitution(src, dst, stype, confidence=conf, notes=notes)
    print(f'  Loaded {len(SUBSTITUTIONS)} legacy substitutions')

    # Status
    print('\n=== DATABASE STATUS ===')
    conn = get_db()
    for t in ['category', 'agent_node', 'product', 'component',
              'product_bom', 'substitution', 'observation', 'edge']:
        try:
            count = conn.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
            if count > 0:
                print(f'  {t:25s} {count:>6}')
        except:
            pass
    conn.close()


if __name__ == '__main__':
    main()

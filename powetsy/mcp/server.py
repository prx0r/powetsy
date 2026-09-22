"""POW MCP Server — physical-agent hardware discovery and routing.

The core API for Muse/ChatGPT to discover, compare, quote and
eventually order physical-agent hardware across multiple suppliers.
"""

import json
from datetime import datetime, timezone
from powetsy.shared.db import get_db, _enable_foreign_keys
from powetsy.shared.persist import (
    upsert_component, insert_observation, insert_edge, get_db as get_persist_db
)


class PowMCP:
    """POW MCP Server — the main interface."""

    def search_capability(self, capability, requirements=None,
                           max_price=None, currency='USD', region=None):
        """Find parts/modules matching functional requirements.

        capability: "vision", "audio", "motion", "compute", "power", "fabrication"
        requirements: {"camera": True, "usb": True, "linux": True}
        """
        conn = get_db()
        # Search components that match capability tags
        query = "SELECT * FROM component WHERE category LIKE ?"
        params = [f'%{capability}%']

        if max_price:
            query += " AND price_usd <= ?"
            params.append(max_price)

        rows = conn.execute(query, params).fetchall()
        conn.close()

        # For now, return raw matches
        # Later: rank by adoption score, compatibility, price
        return [
            {
                'component_id': r[0],
                'name': r[1],
                'category': r[2],
                'mpn': r[3],
                'manufacturer': r[4],
                'price_usd': r[6],
                'interfaces': r[8] if len(r) > 8 else '',
            }
            for r in rows
        ]

    def compare_options(self, options, criteria=None):
        """Side-by-side comparison of candidate solutions."""
        conn = get_db()
        results = []
        for option_id in options:
            row = conn.execute(
                "SELECT * FROM component WHERE component_id=?", (option_id,)
            ).fetchone()
            if row:
                results.append({
                    'component_id': row[0],
                    'name': row[1],
                    'category': row[2],
                    'price_usd': row[7],
                    'voltage': row[8],
                    'interface': row[9],
                })
        conn.close()
        return results

    def get_part(self, part_id):
        """Detailed information about a specific part."""
        conn = get_db()
        row = conn.execute(
            "SELECT * FROM component WHERE component_id=?", (part_id,)
        ).fetchone()
        conn.close()
        if not row:
            return None
        return {
            'component_id': row[0],
            'name': row[1],
            'category': row[2],
            'mpn': row[3],
            'manufacturer': row[4],
            'description': row[5],
            'price_usd': row[6],
            'voltage': row[7],
            'interface': row[8] if len(row) > 8 else '',
        }

    def quote_build(self, build_id, quantities=None):
        """Get pricing for a build at various quantities."""
        if quantities is None:
            quantities = [1, 10, 100, 1000]

        conn = get_db()
        items = conn.execute(
            "SELECT pb.component_id, pb.quantity, c.price_usd, c.name "
            "FROM product_bom pb JOIN component c ON pb.component_id = c.component_id "
            "WHERE pb.product_id=?", (build_id,)
        ).fetchall()
        conn.close()

        quotes = []
        for qty in quantities:
            total = sum(item[2] * item[1] * qty for item in items if item[2])
            quotes.append({
                'quantity': qty,
                'unit_cost': total / qty if qty else 0,
                'total_cost': total,
                'items': len(items),
            })

        return {
            'build_id': build_id,
            'quotes': quotes,
            'items': [{'name': i[3], 'qty': i[1], 'unit_price': i[2]} for i in items],
        }

    def save_build(self, name, parts, metadata=None):
        """Persist a validated build."""
        build_id = f'build:{name.lower().replace(" ", "_")}'
        conn = get_db()
        now = datetime.now(timezone.utc).isoformat()
        conn.execute(
            "INSERT OR REPLACE INTO product (product_id, name, description, "
            "first_seen_at, last_seen_at) VALUES (?, ?, ?, ?, ?)",
            (build_id, name, json.dumps(metadata or {}), now, now)
        )
        for part in parts:
            try:
                conn.execute(
                    "INSERT INTO product_bom (product_id, component_id, quantity, role) "
                    "VALUES (?, ?, ?, ?)",
                    (build_id, part['component_id'], part.get('quantity', 1),
                     part.get('role', ''))
                )
            except Exception:
                pass
        conn.commit()
        conn.close()
        return build_id

    def resolve(self, need, qty=1, target_cost=None, constraints=None):
        """High-level capability resolution.

        Returns viable implementation routes with cost estimates.
        """
        from powetsy.templates.build_templates import TEMPLATES

        # Parse capability requirements from need description
        capabilities = self._parse_need(need)

        # Find matching templates
        matching_templates = []
        for tid, tmpl in TEMPLATES.items():
            template_caps = set(tmpl.get('capabilities', []))
            if template_caps.intersection(set(capabilities)):
                score = len(template_caps.intersection(set(capabilities))) / max(len(capabilities), 1)
                matching_templates.append((score, tid, tmpl))

        matching_templates.sort(key=lambda x: -x[0])

        results = []
        for score, tid, tmpl in matching_templates[:3]:
            # Get cost estimate
            electronics_cost = tmpl.get('estimated_electronics_cost', 0)
            qty_multiplier = {1: 1.0, 10: 0.8, 100: 0.6, 1000: 0.45}.get(qty, 0.6)
            estimated = electronics_cost * qty_multiplier

            # Find available parts for each required module
            parts = []
            for module in tmpl.get('required_modules', []):
                component = self.get_part(f'part:{module}')
                if component:
                    parts.append({
                        'module': module,
                        'name': component['name'],
                        'price': component.get('price_usd', 0),
                    })

            results.append({
                'template': tid,
                'name': tmpl['name'],
                'description': tmpl['description'],
                'capabilities_matched': list(template_caps.intersection(set(capabilities))),
                'estimated_cost_per_unit': estimated,
                'assembly_difficulty': tmpl.get('assembly_difficulty', 'unknown'),
                'evidence': tmpl.get('evidence', ''),
                'parts_count': len(parts),
            })

        # Calculate totals
        if results:
            total = results[0].get('estimated_cost_per_unit', 0) * qty
        else:
            total = 0

        return {
            'need': need,
            'qty': qty,
            'capabilities': capabilities,
            'routes': results,
            'estimated_total': total,
            'estimated_per_unit': total / qty if qty else 0,
        }

    def _parse_need(self, need):
        """Extract capability keywords from natural language need."""
        need_lower = need.lower()
        capabilities = []
        if any(w in need_lower for w in ['camera', 'vision', 'see', 'eyes', 'look']):
            capabilities.append('vision')
        if any(w in need_lower for w in ['mic', 'microphone', 'hear', 'ears', 'listen', 'voice']):
            capabilities.append('audio')
        if any(w in need_lower for w in ['speaker', 'talk', 'speak', 'sound']):
            capabilities.append('audio')
        if any(w in need_lower for w in ['servo', 'motor', 'move', 'turn', 'tilt', 'pan', 'head']):
            capabilities.append('motion')
        if any(w in need_lower for w in ['esp32', 'compute', 'sbc', 'n100', 'brain']):
            capabilities.append('compute')
        if any(w in need_lower for w in ['power', 'battery', 'usb', 'charge']):
            capabilities.append('power')
        if any(w in need_lower for w in ['led', 'light', 'rgb', 'glow']):
            capabilities.append('lighting')
        if any(w in need_lower for w in ['print', 'cnc', 'pcb', 'enclosure']):
            capabilities.append('fabrication')
        if not capabilities:
            capabilities.append('compute')  # default
        return capabilities


# Singleton
_mcp = None

def get_mcp():
    global _mcp
    if _mcp is None:
        _mcp = PowMCP()
    return _mcp

"""Substitution evidence — tracks observed successful substitutions, not just inferred."""

import hashlib
import sqlite3
from datetime import datetime, timezone
from powetsy.shared.db import get_db, _enable_foreign_keys


def insert_substitution_evidence(src_id, dst_id, stype, evidence_type,
                                   confidence=0.5, dimensions=None,
                                   notes='', source='', project_id=None):
    """Record evidence for a substitution.

    evidence_type should be one of:
    - observed_in_project: confirmed used in a real build
    - tested_replacement: physically tested
    - inferred_electrical: same voltage/current/interface
    - inferred_mechanical: similar form factor
    - manufacturer_suggested: OEM says OK
    - community_reported: forum/issue says it works
    """
    raw = f'{src_id}:{dst_id}:{stype}:{evidence_type}:{source}'
    evidence_id = hashlib.sha256(raw.encode()).hexdigest()[:16]
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO substitution (substitution_id, src_component_id, dst_component_id, "
            "substitution_type, confidence, notes, source) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (evidence_id, src_id, dst_id, stype, confidence,
             json.dumps({'evidence_type': evidence_type,
                         'dimensions': dimensions or {},
                         'project_id': project_id,
                         'notes': notes}),
             source)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        # Accumulate evidence on existing substitution
        pass
    conn.close()
    return evidence_id


def get_substitution_confidence(src_id, dst_id):
    """Get aggregate confidence for a substitution based on all evidence."""
    conn = get_db()
    rows = conn.execute(
        "SELECT confidence, notes FROM substitution "
        "WHERE src_component_id=? AND dst_component_id=?",
        (src_id, dst_id)
    ).fetchall()
    conn.close()
    if not rows:
        return 0.0
    # Aggregate: average confidence weighted by evidence count
    total_conf = sum(r[0] for r in rows)
    return min(1.0, total_conf / len(rows))


def get_parts_used_together(part_id, limit=20):
    """Find parts that commonly appear together with this part."""
    conn = get_db()
    rows = conn.execute("""
        SELECT e.object_id, COUNT(*) as cnt
        FROM edge e
        WHERE e.predicate = 'observed_with'
        AND (e.subject_id = ? OR e.object_id = ?)
        GROUP BY CASE WHEN e.subject_id = ? THEN e.object_id ELSE e.subject_id END
        ORDER BY cnt DESC LIMIT ?
    """, (part_id, part_id, part_id, limit)).fetchall()
    conn.close()
    return rows

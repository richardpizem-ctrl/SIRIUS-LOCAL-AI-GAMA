"""
pack_event_adapter.py

GAMA Runtime 3.4.0 – Unified Event Model v3
Adapter that converts Knowledge Pack output into safe semantic meta-data.

Rules:
- No raw OCR/text content.
- No images or binary data.
- Only semantic/meta fields.
- Deterministic structure.
- Fully offline, safe for families and schools.
"""

from typing import Dict, Any


def extract_pack_meta_v3(pack_raw: Dict[str, Any]) -> Dict[str, Any]:
    """
    Converts raw PACK output into a safe meta-data block.

    Expected pack_raw structure (example):
        {
            "pack_ids": ["math_basics", "fractions_v2"],
            "subject": "math",
            "difficulty": "easy",
            "tags": ["fractions", "arithmetic"],
            "schoolwork_meta": {
                "task_type": "equation",
                "expected_steps": 3
            }
        }

    Output (safe):
        {
            "pack_ids": [...],
            "subject_hint": "math",
            "difficulty_hint": "easy",
            "tags": [...],
            "schoolwork_meta": {...}
        }
    """

    if not pack_raw:
        return {
            "pack_ids": [],
            "subject_hint": None,
            "difficulty_hint": None,
            "tags": [],
            "schoolwork_meta": {},
        }

    pack_ids = pack_raw.get("pack_ids", [])
    subject_hint = pack_raw.get("subject")
    difficulty_hint = pack_raw.get("difficulty")
    tags = pack_raw.get("tags", [])
    schoolwork_meta = pack_raw.get("schoolwork_meta", {})

    return {
        "pack_ids": pack_ids,
        "subject_hint": subject_hint,
        "difficulty_hint": difficulty_hint,
        "tags": tags,
        "schoolwork_meta": schoolwork_meta,
    }

"""
context_schema_v3.py

GAMA Runtime 3.4.0 – Runtime Context Schema v3
Defines the deterministic structure of the runtime context record.

Rules:
- No raw OCR/text content.
- No image data.
- Only semantic/meta fields.
- Deterministic structure.
- Fully offline, safe for families and schools.
"""

from typing import Dict, Any


CONTEXT_SCHEMA_VERSION = "3.4.0"


def build_context_record_v3(
    *,
    unified_event: Dict[str, Any],
    trace_meta: Dict[str, Any],
    normalization_meta: Dict[str, Any],
    debug_meta: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Builds a deterministic runtime context record.

    This context is consumed by:
        - SCHOOLWORK reasoning engine
        - VISION reasoning engine
        - PACK reasoning engine
        - trace_logs_v3
        - fallback_normalization_v3
        - Self-Repair Layer (Runtime 4.4+)

    Structure:
        {
            "version": "3.4.0",
            "unified_event": {...},
            "trace_meta": {...},
            "normalization_meta": {...},
            "debug_meta": {...}
        }
    """

    return {
        "version": CONTEXT_SCHEMA_VERSION,
        "unified_event": unified_event,
        "trace_meta": trace_meta,
        "normalization_meta": normalization_meta,
        "debug_meta": debug_meta,
    }

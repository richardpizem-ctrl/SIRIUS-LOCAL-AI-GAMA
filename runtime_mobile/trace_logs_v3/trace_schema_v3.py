"""
trace_schema_v3.py

GAMA Runtime 3.4.0 – Trace Logs v3
Deterministic schema builder for SCHOOLWORK reasoning trace records.

Rules:
- No raw OCR/text content.
- No sensitive user data.
- Only semantic meta-data.
- Deterministic field ordering.
- Fully offline, safe for families and schools.
"""

from typing import Dict, Any
import time


TRACE_SCHEMA_VERSION = "3.4.0"


def build_trace_record_v3(
    *,
    trace_id: str,
    module: str,
    normalized_input_meta: Dict,
    subject_meta: Dict,
    pack_meta: Dict,
    reasoning_steps_meta: Dict,
    fallback_meta: Dict,
    context_meta: Dict,
) -> Dict[str, Any]:
    """
    Builds a deterministic trace record following the v3 schema.

    All *_meta dictionaries must contain ONLY:
    - semantic flags
    - categories
    - IDs
    - technical metadata
    - no raw content
    """

    # Deterministic timestamp (integer seconds)
    timestamp = int(time.time())

    record = {
        "version": TRACE_SCHEMA_VERSION,
        "timestamp": timestamp,
        "trace_id": trace_id,
        "module": module,

        # Meta blocks (safe only)
        "normalized_input_meta": normalized_input_meta,
        "subject_meta": subject_meta,
        "pack_meta": pack_meta,
        "reasoning_steps_meta": reasoning_steps_meta,
        "fallback_meta": fallback_meta,
        "context_meta": context_meta,
    }

    return record

"""
event_schema_v3.py

GAMA Runtime 3.4.0 – Unified Event Model v3
A single deterministic event schema for SCHOOLWORK + VISION + PACK events.

Rules:
- No raw OCR/text content.
- No images or binary data.
- Only semantic/meta fields.
- Deterministic structure.
- Fully offline, safe for families and schools.
"""

from typing import Dict, Any, Optional
import time


EVENT_SCHEMA_VERSION = "3.4.0"


def build_event_v3(
    *,
    event_type: str,
    source: str,
    trace_id: str,
    subject: Optional[str] = None,
    difficulty: Optional[str] = None,
    pack_ids: Optional[list] = None,
    vision_meta: Optional[Dict[str, Any]] = None,
    schoolwork_meta: Optional[Dict[str, Any]] = None,
    context_meta: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Builds a unified event record for SCHOOLWORK + VISION + PACK pipelines.

    event_type:
        "SCHOOLWORK_TEXT"
        "SCHOOLWORK_VISION"
        "SCHOOLWORK_PACK"

    source:
        "user_input", "ocr", "vision_detector", "pack_loader", etc.

    All *_meta fields must contain ONLY:
    - semantic flags
    - categories
    - IDs
    - technical metadata
    """

    timestamp = int(time.time())

    return {
        "version": EVENT_SCHEMA_VERSION,
        "timestamp": timestamp,
        "trace_id": trace_id,
        "event_type": event_type,
        "source": source,

        # Optional semantic fields
        "subject": subject,
        "difficulty": difficulty,
        "pack_ids": pack_ids or [],

        # Meta blocks (safe only)
        "vision_meta": vision_meta or {},
        "schoolwork_meta": schoolwork_meta or {},
        "context_meta": context_meta or {},
    }

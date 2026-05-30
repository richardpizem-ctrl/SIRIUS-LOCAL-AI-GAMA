"""
debug_metadata.py

GAMA Runtime 3.4.0 – Runtime Context v3
Builds safe, deterministic debug metadata for SCHOOLWORK + VISION + PACK pipelines.

Rules:
- No raw OCR/text content.
- No image data.
- Only semantic/meta fields.
- Deterministic structure.
- Fully offline, safe for families and schools.
"""

from typing import Dict, Any


def build_debug_meta_v3(
    *,
    unified_event: Dict[str, Any],
    trace_meta: Dict[str, Any],
    normalization_meta: Dict[str, Any],
    system_meta: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Builds a safe debug metadata block.

    This metadata is used by:
        - trace_logs_v3
        - runtime_context_v3
        - Self-Repair Layer (Runtime 4.4+)

    Contains ONLY:
        - safe flags
        - counters
        - IDs
        - system state indicators
        - pipeline stage info
    """

    return {
        "debug_version": "3.4.0",

        # Unified event info (safe only)
        "event_type": unified_event.get("event_type"),
        "event_source": unified_event.get("source"),
        "event_subject": unified_event.get("subject"),
        "event_difficulty": unified_event.get("difficulty"),

        # Trace metadata (safe)
        "trace_id": trace_meta.get("trace_id"),
        "trace_stage": trace_meta.get("stage"),
        "trace_timestamp": trace_meta.get("timestamp"),

        # Normalization metadata (safe)
        "normalization_primary": normalization_meta.get("primary_applied"),
        "normalization_fallback": normalization_meta.get("fallback_applied"),
        "normalization_reason": normalization_meta.get("fallback_reason"),

        # System metadata (safe)
        "system_runtime": system_meta.get("runtime_version"),
        "system_platform": system_meta.get("platform"),
        "system_mode": system_meta.get("mode"),
        "system_safe_state": system_meta.get("safe_state"),

        # Deterministic pipeline flags
        "pipeline_flags": {
            "has_vision_meta": bool(unified_event.get("vision_meta")),
            "has_pack_meta": bool(unified_event.get("pack_ids")),
            "has_schoolwork_meta": bool(unified_event.get("schoolwork_meta")),
        },
    }

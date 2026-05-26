"""
SIRIUS LOCAL AI GAMA – Event Compatibility Layer v3
Mobile Runtime 3.2.0

This module provides:
- backward compatibility for legacy events
- payload normalization
- safety rules for deprecated event formats
- preparation for Event Engine 4.0
"""

COMPAT_LAYER_VERSION = "3.2.0"


# ---------------------------------------------------------
# Legacy → modern payload converters
# ---------------------------------------------------------

def convert_legacy_analyze(payload: dict) -> dict:
    """
    Convert legacy ANALYZE/ANALYZE_V1 payloads to SCENE format.
    """
    if not payload:
        return {"type": "scene"}

    return {
        "type": "scene",
        "objects": payload.get("objects", []),
        "text": payload.get("text", ""),
        "confidence": payload.get("confidence", 0.0),
    }


def convert_legacy_ocr(payload: dict) -> dict:
    """
    Convert legacy OCR payloads to HOMEWORK format.
    """
    if not payload:
        return {"type": "homework"}

    return {
        "type": "homework",
        "text": payload.get("text", ""),
        "lines": payload.get("lines", []),
        "language": payload.get("language", "unknown"),
    }


# ---------------------------------------------------------
# Compatibility dispatcher
# ---------------------------------------------------------

def normalize_payload(event_name: str, payload: dict) -> dict:
    """
    Normalize payloads for legacy events.
    """
    if event_name in ("ANALYZE", "ANALYZE_V1"):
        return convert_legacy_analyze(payload)

    if event_name == "OCR":
        return convert_legacy_ocr(payload)

    # No conversion needed
    return payload


# ---------------------------------------------------------
# Safety rules for deprecated events
# ---------------------------------------------------------

def is_legacy_event(event_name: str) -> bool:
    """
    Check if the event is considered legacy.
    """
    return event_name in ("ANALYZE", "ANALYZE_V1", "OCR")


def legacy_event_warning(event_name: str) -> str:
    """
    Return a warning message for deprecated events.
    """
    return f"Warning: Event '{event_name}' is deprecated and converted automatically."


# ---------------------------------------------------------
# Main compatibility resolver
# ---------------------------------------------------------

def resolve_compatibility(event_name: str, payload: dict) -> tuple:
    """
    Resolve compatibility:
    - detect legacy events
    - convert payloads
    - return (normalized_event_name, normalized_payload, warning)
    """
    warning = None

    if is_legacy_event(event_name):
        warning = legacy_event_warning(event_name)

    normalized_payload = normalize_payload(event_name, payload)

    # Event name normalization is handled by event_versioning_3
    return event_name, normalized_payload, warning


# ---------------------------------------------------------
# Diagnostics helper
# ---------------------------------------------------------

def get_compat_info() -> dict:
    """
    Return compatibility layer metadata.
    """
    return {
        "version": COMPAT_LAYER_VERSION,
        "legacy_events": ["ANALYZE", "ANALYZE_V1", "OCR"],
    }

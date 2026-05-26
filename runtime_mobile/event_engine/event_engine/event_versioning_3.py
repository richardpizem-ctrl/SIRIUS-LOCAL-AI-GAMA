"""
SIRIUS LOCAL AI GAMA – Event Versioning v3
Mobile Runtime 3.2.0

This module provides:
- event mapping by version
- backward compatibility for 3.0 → 3.1 → 3.2
- event payload validation
- safety rules for legacy events
- preparation for Event Engine 4.0
"""

EVENT_VERSION = "3.2.0"

# ---------------------------------------------------------
# Supported event versions
# ---------------------------------------------------------

SUPPORTED_EVENT_VERSIONS = {
    "3.0": ["TEXT", "VISION", "PACK_QUERY"],
    "3.1": ["TEXT", "VISION", "PACK_QUERY", "PACK_SUGGEST"],
    "3.2": [
        "TEXT",
        "VISION",
        "PACK_QUERY",
        "PACK_SUGGEST",
        "SCENE",
        "HOMEWORK",
        "SECURITY_ALERT",
    ],
}

# ---------------------------------------------------------
# Legacy → new event name mapping
# ---------------------------------------------------------

EVENT_COMPAT_MAP = {
    "ANALYZE": "SCENE",       # old → new
    "ANALYZE_V1": "SCENE",
    "OCR": "HOMEWORK",        # old OCR → new schoolwork mode
}

# ---------------------------------------------------------
# Event validation
# ---------------------------------------------------------

def validate_event(event_name: str, version: str) -> bool:
    """
    Check if the event exists in the given runtime version.
    """
    if version not in SUPPORTED_EVENT_VERSIONS:
        return False

    return event_name in SUPPORTED_EVENT_VERSIONS[version]


# ---------------------------------------------------------
# Normalize legacy event names
# ---------------------------------------------------------

def normalize_event(event_name: str) -> str:
    """
    Convert legacy event names to their modern equivalents.
    """
    return EVENT_COMPAT_MAP.get(event_name, event_name)


# ---------------------------------------------------------
# Main resolver
# ---------------------------------------------------------

def resolve_event(event_name: str, version: str = "3.2") -> str:
    """
    Resolve an event:
    - normalize legacy names
    - validate against version
    - return normalized event or UNSUPPORTED_EVENT
    """
    normalized = normalize_event(event_name)

    if not validate_event(normalized, version):
        return "UNSUPPORTED_EVENT"

    return normalized


# ---------------------------------------------------------
# Diagnostics helper
# ---------------------------------------------------------

def get_supported_events():
    """
    Return all supported events for version 3.2.
    """
    return SUPPORTED_EVENT_VERSIONS["3.2"]

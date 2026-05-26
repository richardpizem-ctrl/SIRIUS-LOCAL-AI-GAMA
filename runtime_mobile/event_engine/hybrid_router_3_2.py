"""
SIRIUS LOCAL AI GAMA – Hybrid-Safe Router v3
Mobile Runtime 3.2.0

This module provides:
- hybrid routing (TEXT + VISION)
- safe fallback routing
- schoolwork mode heuristics
- integration with Event Versioning v3
- preparation for Event Engine 4.0
"""

ROUTER_VERSION = "3.2.0"


# ---------------------------------------------------------
# Event categories
# ---------------------------------------------------------

TEXT_EVENTS = ["TEXT", "PACK_QUERY", "PACK_SUGGEST"]
VISION_EVENTS = ["SCENE", "HOMEWORK"]
SECURITY_EVENTS = ["SECURITY_ALERT"]


# ---------------------------------------------------------
# Hybrid routing logic
# ---------------------------------------------------------

def route_text(input_text: str) -> str:
    """
    Basic text routing logic.
    """
    text = input_text.lower()

    if "homework" in text or "task" in text:
        return "HOMEWORK"

    if "scene" in text or "analyze" in text:
        return "SCENE"

    if "suggest" in text:
        return "PACK_SUGGEST"

    if "search" in text or "find" in text:
        return "PACK_QUERY"

    return "TEXT"


def route_vision(vision_payload: dict) -> str:
    """
    Basic vision routing logic.
    """
    if not vision_payload:
        return "SCENE"

    if vision_payload.get("type") == "homework":
        return "HOMEWORK"

    if vision_payload.get("type") == "scene":
        return "SCENE"

    return "SCENE"


# ---------------------------------------------------------
# Schoolwork safety heuristics
# ---------------------------------------------------------

def schoolwork_safe_check(event_name: str, text: str) -> str:
    """
    Apply schoolwork safety rules.
    """
    if event_name == "HOMEWORK":
        if "solve" in text.lower() or "answer" in text.lower():
            return "SECURITY_ALERT"
    return event_name


# ---------------------------------------------------------
# Main hybrid router
# ---------------------------------------------------------

def hybrid_route(input_text: str = "", vision_payload: dict = None) -> str:
    """
    Hybrid routing:
    - if both text and vision are present → vision has priority
    - if only text → text routing
    - if only vision → vision routing
    - fallback → TEXT
    """
    # Vision has priority
    if vision_payload:
        event = route_vision(vision_payload)
        return event

    # Text routing
    if input_text:
        event = route_text(input_text)
        event = schoolwork_safe_check(event, input_text)
        return event

    # Fallback
    return "TEXT"


# ---------------------------------------------------------
# Diagnostics helper
# ---------------------------------------------------------

def get_router_info() -> dict:
    """
    Return router metadata.
    """
    return {
        "version": ROUTER_VERSION,
        "text_events": TEXT_EVENTS,
        "vision_events": VISION_EVENTS,
        "security_events": SECURITY_EVENTS,
    }

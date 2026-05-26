"""
SIRIUS LOCAL AI GAMA – Event Engine Entry Point
Mobile Runtime 3.2.0

This module connects:
- Event Versioning v3
- Hybrid-Safe Router v3
- Event Compatibility Layer v3
- Event Diagnostics v3

It provides a unified entry point for the entire event engine.
"""

from .event_versioning_3 import resolve_event
from .hybrid_router_3_2 import hybrid_route
from .event_compatibility import resolve_compatibility
from .event_diagnostics_v3 import (
    track_event,
    track_pack_usage,
    track_vision,
    track_security_alert,
    track_legacy_conversion,
    log_routing,
)

ENGINE_ENTRY_VERSION = "3.2.0"


# ---------------------------------------------------------
# Main event engine entry point
# ---------------------------------------------------------

def process_event(input_text: str = "", vision_payload: dict = None, pack_name: str = None):
    """
    Full event processing pipeline:
    1. Hybrid routing (TEXT + VISION)
    2. Event normalization (legacy → modern)
    3. Event version resolution
    4. Diagnostics tracking
    5. Return final event + payload
    """

    # Step 1: Hybrid routing
    routed_event = hybrid_route(input_text, vision_payload)

    # Step 2: Compatibility layer
    normalized_event, normalized_payload, warning = resolve_compatibility(
        routed_event, vision_payload
    )

    if warning:
        track_legacy_conversion()

    # Step 3: Version resolution
    final_event = resolve_event(normalized_event)

    # Step 4: Diagnostics
    track_event(final_event)
    log_routing(input_text, vision_payload, final_event)

    if pack_name:
        track_pack_usage(pack_name)

    if final_event == "SECURITY_ALERT":
        track_security_alert()

    if final_event in ("SCENE", "HOMEWORK"):
        track_vision(final_event)

    # Step 5: Return final result
    return {
        "event": final_event,
        "payload": normalized_payload,
        "warning": warning,
    }


# ---------------------------------------------------------
# Metadata
# ---------------------------------------------------------

def get_engine_info() -> dict:
    """
    Return metadata for the event engine entry point.
    """
    return {
        "version": ENGINE_ENTRY_VERSION,
        "modules": [
            "event_versioning_3",
            "hybrid_router_3_2",
            "event_compatibility",
            "event_diagnostics_v3",
        ],
    }

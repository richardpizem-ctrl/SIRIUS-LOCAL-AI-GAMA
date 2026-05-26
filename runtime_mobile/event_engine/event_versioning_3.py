"""
SIRIUS LOCAL AI GAMA – Event Versioning v3
Mobile Runtime 3.2.0

Resolves:
- final event version
- normalization of event names
- compatibility with VisionEngineV3
"""

from runtime_mobile.core.event_types import MobileEventTypes


VERSIONING_VERSION = "3.2.0"


# ---------------------------------------------------------
# Event Version Resolution
# ---------------------------------------------------------

def resolve_event(event_type: str) -> str:
    """
    Normalize event names and ensure they match MobileEventTypes.
    """

    if not event_type:
        return "UNKNOWN"

    # Normalize to uppercase
    event_type = event_type.upper()

    # Direct matches
    if event_type in (
        MobileEventTypes.SCENE,
        MobileEventTypes.DETECT,
        MobileEventTypes.OCR,
        MobileEventTypes.HOMEWORK,
        "TEXT",
    ):
        return event_type

    # Legacy → Modern fallback
    legacy_map = {
        "VISION_SCENE": MobileEventTypes.SCENE,
        "VISION_DETECT": MobileEventTypes.DETECT,
        "VISION_OCR": MobileEventTypes.OCR,
        "VISION_HOMEWORK": MobileEventTypes.HOMEWORK,
        "IMG_SCENE": MobileEventTypes.SCENE,
        "IMG_DETECT": MobileEventTypes.DETECT,
        "IMG_OCR": MobileEventTypes.OCR,
        "IMG_HW": MobileEventTypes.HOMEWORK,
    }

    if event_type in legacy_map:
        return legacy_map[event_type]

    # Unknown event
    return "UNKNOWN"


# ---------------------------------------------------------
# Metadata
# ---------------------------------------------------------

def get_versioning_info() -> dict:
    return {
        "version": VERSIONING_VERSION,
        "supports": [
            "vision_events",
            "legacy_conversion",
            "text_events",
            "normalized_event_names",
        ],
    }

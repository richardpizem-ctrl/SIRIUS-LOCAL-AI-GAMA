"""
SIRIUS LOCAL AI GAMA – Event Compatibility Layer v3
Mobile Runtime 3.2.0

Converts:
- legacy events → modern events
- legacy payloads → normalized payloads

Ensures compatibility with:
- Hybrid Router 3.2
- VisionEngineV3
- Event Diagnostics v3
"""

from runtime_mobile.core.event_types import MobileEventTypes


COMPAT_VERSION = "3.2.0"


# ---------------------------------------------------------
# Compatibility Resolution
# ---------------------------------------------------------

def resolve_compatibility(event_type: str, payload: dict):
    """
    Convert legacy event names and payload formats into
    modern MobileEventTypes and normalized payloads.
    """

    warning = None

    # -----------------------------------------------------
    # Legacy → Modern Vision Events
    # -----------------------------------------------------

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
        warning = f"Legacy event '{event_type}' converted to '{legacy_map[event_type]}'"
        event_type = legacy_map[event_type]

    # -----------------------------------------------------
    # Normalize payload
    # -----------------------------------------------------

    if payload is None:
        payload = {}

    # Ensure payload contains image if needed
    if event_type in (
        MobileEventTypes.SCENE,
        MobileEventTypes.DETECT,
        MobileEventTypes.OCR,
        MobileEventTypes.HOMEWORK,
    ):
        if "image" not in payload:
            payload["image"] = None

    return event_type, payload, warning


# ---------------------------------------------------------
# Metadata
# ---------------------------------------------------------

def get_compat_info() -> dict:
    return {
        "version": COMPAT_VERSION,
        "supports": [
            "legacy_vision_events",
            "modern_vision_events",
            "payload_normalization",
        ],
    }

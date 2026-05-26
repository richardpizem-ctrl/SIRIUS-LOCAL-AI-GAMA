"""
SIRIUS LOCAL AI GAMA – Hybrid Router v3.2
Mobile Runtime 3.2.0

Routes:
- TEXT input → NL event
- VISION payload → SCENE / DETECT / OCR / HOMEWORK
"""

from runtime_mobile.core.event_types import MobileEventTypes


ROUTER_VERSION = "3.2.0"


# ---------------------------------------------------------
# Hybrid Routing
# ---------------------------------------------------------

def hybrid_route(input_text: str = "", vision_payload: dict = None) -> str:
    """
    Decide whether the event is TEXT-based or VISION-based.
    """

    # -----------------------------------------------------
    # 1. VISION routing
    # -----------------------------------------------------
    if vision_payload:

        # OCR
        if vision_payload.get("mode") == "OCR":
            return MobileEventTypes.OCR

        # DETECT
        if vision_payload.get("mode") == "DETECT":
            return MobileEventTypes.DETECT

        # SCENE
        if vision_payload.get("mode") == "SCENE":
            return MobileEventTypes.SCENE

        # HOMEWORK
        if vision_payload.get("mode") == "HOMEWORK":
            return MobileEventTypes.HOMEWORK

        # Default fallback
        return MobileEventTypes.SCENE

    # -----------------------------------------------------
    # 2. TEXT routing
    # -----------------------------------------------------
    if input_text:
        # NL router will handle this later
        return "TEXT"

    # -----------------------------------------------------
    # 3. No input
    # -----------------------------------------------------
    return "UNKNOWN"

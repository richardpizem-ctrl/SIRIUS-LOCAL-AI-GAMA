# SIRIUS LOCAL AI GAMA - Mobile NL Router

from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.core.event import MobileEvent

class MobileNLRouter:
    """
    Lightweight intent router for the mobile runtime.
    Converts natural language into MobileEvent objects.
    """

    def route(self, text: str):
        if not text:
            return MobileEvent(MobileEventTypes.UNKNOWN)

        t = text.lower()

        # --- VISION ---
        if any(k in t for k in ["scan", "photo", "ocr", "camera"]):
            return MobileEvent(MobileEventTypes.OCR)

        if any(k in t for k in ["analyze", "what is in the picture"]):
            return MobileEvent(MobileEventTypes.ANALYZE)

        # --- KNOWLEDGE PACKS ---
        if any(k in t for k in ["how", "why", "what", "explain"]):
            return MobileEvent(MobileEventTypes.PACK_LOOKUP, key="query")

        # --- SECURITY ---
        if "permission" in t or "allow" in t or "deny" in t:
            return MobileEvent(MobileEventTypes.SECURITY)

        if "restricted" in t:
            enabled = "on" in t or "enable" in t
            return MobileEvent(MobileEventTypes.RESTRICTED_MODE, enabled=enabled)

        # --- HELP ---
        if "help" in t:
            return MobileEvent(MobileEventTypes.SHOW_HELP)

        # Default fallback
        return MobileEvent(MobileEventTypes.UNKNOWN)

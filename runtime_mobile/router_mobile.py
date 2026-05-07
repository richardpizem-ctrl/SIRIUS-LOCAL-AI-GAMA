# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile NL Router
# Version: 3.0.0-pre
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.core.mobile_event import MobileEvent


class MobileNLRouter:
    """
    Lightweight intent router for the mobile runtime.
    Converts natural language into MobileEvent objects.
    """

    def route(self, text: str):
        if not text:
            return MobileEvent(MobileEventTypes.UNKNOWN)

        t = text.lower()

        # --------------------------------------------------------
        # VISION
        # --------------------------------------------------------
        if any(k in t for k in ["scan", "photo", "ocr", "camera"]):
            return MobileEvent(MobileEventTypes.OCR)

        if any(k in t for k in ["analyze", "what is in the picture"]):
            return MobileEvent(MobileEventTypes.ANALYZE)

        # --------------------------------------------------------
        # KNOWLEDGE PACKS
        # --------------------------------------------------------
        if any(k in t for k in ["how", "why", "what is", "explain"]):
            return MobileEvent(MobileEventTypes.PACK_QUERY, key=t)

        # --------------------------------------------------------
        # TEXT QUERY / ASSISTANT
        # --------------------------------------------------------
        if any(k in t for k in ["write", "summarize", "translate", "answer"]):
            return MobileEvent(MobileEventTypes.TEXT_QUERY, query=t)

        if any(k in t for k in ["assistant", "ai", "help me with"]):
            return MobileEvent(MobileEventTypes.ASSISTANT, query=t)

        # --------------------------------------------------------
        # SECURITY
        # --------------------------------------------------------
        if any(k in t for k in ["permission", "allow", "deny"]):
            return MobileEvent(MobileEventTypes.SECURITY)

        if "restricted" in t:
            enabled = "on" in t or "enable" in t
            return MobileEvent(MobileEventTypes.RESTRICTED_MODE, enabled=enabled)

        # --------------------------------------------------------
        # SYSTEM / RUNTIME
        # --------------------------------------------------------
        if "runtime" in t or "system info" in t:
            return MobileEvent(MobileEventTypes.RUNTIME_INFO)

        # --------------------------------------------------------
        # LAN SYNC
        # --------------------------------------------------------
        if "sync" in t or "lan" in t:
            return MobileEvent(MobileEventTypes.LAN_SYNC)

        # --------------------------------------------------------
        # HELP
        # --------------------------------------------------------
        if "help" in t:
            return MobileEvent(MobileEventTypes.SHOW_HELP)

        # --------------------------------------------------------
        # DEFAULT
        # --------------------------------------------------------
        return MobileEvent(MobileEventTypes.UNKNOWN)

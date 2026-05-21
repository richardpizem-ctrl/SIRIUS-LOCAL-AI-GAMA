# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile NL Router
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Lightweight intent router for the mobile runtime.
# Converts natural language into MobileEvent objects.
# Fully compatible with MobileEventTypes 3.1.0.
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.core.mobile_event import MobileEvent


class MobileNLRouter:
    """
    Natural language → MobileEvent router.
    Handles:
    - Vision intents
    - Knowledge Pack queries
    - Assistant / text queries
    - Security
    - System/runtime
    - LAN bridge
    """

    VERSION = "3.1.0"

    # ------------------------------------------------------------
    # Main routing function
    # ------------------------------------------------------------

    def route(self, text: str):
        if not text or not isinstance(text, str):
            return MobileEvent(MobileEventTypes.UNKNOWN)

        t = text.lower().strip()

        # --------------------------------------------------------
        # VISION
        # --------------------------------------------------------
        if any(k in t for k in ["scan", "photo", "ocr", "camera"]):
            return MobileEvent(MobileEventTypes.OCR, query=t)

        if any(k in t for k in ["detect", "object", "recognize"]):
            return MobileEvent(MobileEventTypes.DETECT, query=t)

        if any(k in t for k in ["scene", "environment", "context"]):
            return MobileEvent(MobileEventTypes.SCENE, query=t)

        if any(k in t for k in ["analyze", "what is in the picture"]):
            return MobileEvent(MobileEventTypes.ANALYZE, query=t)

        # --------------------------------------------------------
        # KNOWLEDGE PACKS
        # --------------------------------------------------------
        if any(k in t for k in ["how", "why", "what is", "explain"]):
            return MobileEvent(MobileEventTypes.PACK_QUERY, key=t)

        if t.startswith("suggest "):
            prefix = t.replace("suggest", "").strip()
            return MobileEvent(MobileEventTypes.PACK_SUGGEST, prefix=prefix)

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
            return MobileEvent(MobileEventTypes.SECURITY, query=t)

        if "restricted" in t:
            enabled = "on" in t or "enable" in t
            return MobileEvent(MobileEventTypes.RESTRICTED_MODE, enabled=enabled)

        # --------------------------------------------------------
        # SYSTEM / RUNTIME
        # --------------------------------------------------------
        if "runtime" in t or "system info" in t:
            return MobileEvent(MobileEventTypes.RUNTIME_INFO)

        if "state" in t or "status" in t:
            return MobileEvent(MobileEventTypes.APP_STATE)

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
        return MobileEvent(MobileEventTypes.UNKNOWN, query=t)

# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile NL Router
# Version: 3.0.0-pre
# ============================================================

from typing import Dict, Any
from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileNLRouter:

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main entry
    # ------------------------------------------------------------

    def route(self, text: str) -> MobileEvent:

        if not text or not isinstance(text, str):
            return MobileEvent(MobileEventTypes.UNKNOWN)

        intent = self._classify_intent(text)
        return self._build_event(intent, text)

    # ------------------------------------------------------------
    # Intent classification
    # ------------------------------------------------------------

    def _classify_intent(self, text: str) -> str:

        t = text.lower().strip()

        # Diagnostics
        if "battery" in t:
            return "CHECK_BATTERY"
        if "temperature" in t or "hot" in t:
            return "CHECK_THERMAL"
        if "memory" in t or "ram" in t:
            return "CHECK_MEMORY"
        if "storage" in t or "space" in t:
            return "CHECK_STORAGE"
        if "diagnostic" in t:
            return "DIAGNOSTICS_REPORT"

        # Vision
        if "ocr" in t or "read" in t:
            return "OCR"
        if "detect" in t:
            return "DETECT"
        if "scene" in t:
            return "SCENE"
        if "homework" in t:
            return "HOMEWORK"

        # Knowledge Packs
        if "lookup" in t:
            return "PACK_LOOKUP"
        if "pack info" in t:
            return "PACK_INFO"
        if "ask" in t or "query" in t:
            return "PACK_QUERY"

        # Security
        if "permission" in t:
            return "PERMISSION_CHECK"
        if "restricted" in t:
            return "RESTRICTED_MODE"

        # App control
        if "open" in t:
            return "OPEN_APP"
        if "help" in t:
            return "SHOW_HELP"

        return "ASSISTANT"

    # ------------------------------------------------------------
    # Event builder
    # ------------------------------------------------------------

    def _build_event(self, intent: str, text: str) -> MobileEvent:

        mapping = {
            "CHECK_BATTERY": MobileEventTypes.CHECK_BATTERY,
            "CHECK_THERMAL": MobileEventTypes.CHECK_THERMAL,
            "CHECK_MEMORY": MobileEventTypes.CHECK_MEMORY,
            "CHECK_STORAGE": MobileEventTypes.CHECK_STORAGE,
            "DIAGNOSTICS_REPORT": MobileEventTypes.DIAGNOSTICS_REPORT,

            "OCR": MobileEventTypes.OCR,
            "DETECT": MobileEventTypes.DETECT,
            "SCENE": MobileEventTypes.SCENE,
            "HOMEWORK": MobileEventTypes.HOMEWORK,

            "PACK_LOOKUP": MobileEventTypes.PACK_LOOKUP,
            "PACK_INFO": MobileEventTypes.PACK_INFO,
            "PACK_QUERY": MobileEventTypes.PACK_QUERY,

            "PERMISSION_CHECK": MobileEventTypes.PERMISSION_CHECK,
            "RESTRICTED_MODE": MobileEventTypes.RESTRICTED_MODE,

            "OPEN_APP": MobileEventTypes.OPEN_APP,
            "SHOW_HELP": MobileEventTypes.SHOW_HELP,

            "ASSISTANT": MobileEventTypes.ASSISTANT,
        }

        event_type = mapping.get(intent, MobileEventTypes.ASSISTANT)

        return MobileEvent(
            event_type,
            text=text,
            intent=intent
        )

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> Dict[str, Any]:
        return {
            "module": "nl_router",
            "version": self.MODULE_VERSION,
            "context_attached": self.context is not None
        }

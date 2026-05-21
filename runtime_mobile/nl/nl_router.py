# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile NL Router
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for GAMA Runtime 3.1:
# - MobileEvent 3.1 metadata (intent, normalized_input, source)
# - SCENE v1 routing
# - Hybrid Schoolwork v1
# - Diagnostics v3
# - Multi-intent routing v1
# ============================================================

from typing import Dict, Any
from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileNLRouter:

    MODULE_VERSION = "3.1.0"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main entry
    # ------------------------------------------------------------

    def route(self, text: str) -> MobileEvent:

        if not text or not isinstance(text, str):
            return MobileEvent(
                MobileEventTypes.UNKNOWN,
                raw_input=text,
                normalized_input="",
                source="nlrouter"
            )

        t = text.lower().strip()
        intent = self._classify_intent(t)

        return self._build_event(intent, text, t)

    # ------------------------------------------------------------
    # Intent classification (3.1)
    # ------------------------------------------------------------

    def _classify_intent(self, t: str) -> str:

        # Diagnostics v3
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

        # Vision v3
        if "ocr" in t or "read" in t:
            return "OCR"
        if "detect" in t:
            return "DETECT"
        if "scene" in t or "what is in the picture" in t:
            return "SCENE"
        if "homework" in t:
            return "HOMEWORK"

        # Hybrid Schoolwork v1
        if "schoolwork" in t or "hybrid" in t:
            return "SCHOOLWORK_HYBRID"

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

        # Multi-intent fallback
        if " and " in t or "," in t:
            return "MULTI_INTENT"

        return "ASSISTANT"

    # ------------------------------------------------------------
    # Event builder (3.1)
    # ------------------------------------------------------------

    def _build_event(self, intent: str, raw_text: str, normalized: str) -> MobileEvent:

        mapping = {
            # Diagnostics
            "CHECK_BATTERY": MobileEventTypes.CHECK_BATTERY,
            "CHECK_THERMAL": MobileEventTypes.CHECK_THERMAL,
            "CHECK_MEMORY": MobileEventTypes.CHECK_MEMORY,
            "CHECK_STORAGE": MobileEventTypes.CHECK_STORAGE,
            "DIAGNOSTICS_REPORT": MobileEventTypes.DIAGNOSTICS_REPORT,

            # Vision
            "OCR": MobileEventTypes.OCR,
            "DETECT": MobileEventTypes.DETECT,
            "SCENE": MobileEventTypes.SCENE,
            "HOMEWORK": MobileEventTypes.HOMEWORK,
            "SCHOOLWORK_HYBRID": MobileEventTypes.SCHOOLWORK_HYBRID,

            # Knowledge Packs
            "PACK_LOOKUP": MobileEventTypes.PACK_LOOKUP,
            "PACK_INFO": MobileEventTypes.PACK_INFO,
            "PACK_QUERY": MobileEventTypes.PACK_QUERY,

            # Security
            "PERMISSION_CHECK": MobileEventTypes.PERMISSION_CHECK,
            "RESTRICTED_MODE": MobileEventTypes.RESTRICTED_MODE,

            # App control
            "OPEN_APP": MobileEventTypes.OPEN_APP,
            "SHOW_HELP": MobileEventTypes.SHOW_HELP,

            # Multi-intent
            "MULTI_INTENT": MobileEventTypes.MULTI_INTENT,

            # Assistant fallback
            "ASSISTANT": MobileEventTypes.ASSISTANT,
        }

        event_type = mapping.get(intent, MobileEventTypes.ASSISTANT)

        return MobileEvent(
            event_type,
            raw_input=raw_text,
            normalized_input=normalized,
            intent=intent,
            source="nlrouter"
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

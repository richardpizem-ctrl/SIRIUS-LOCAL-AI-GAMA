# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile NL Router
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Natural-language router for the mobile runtime.
# Responsibilities:
#   - interpret text commands
#   - classify intent
#   - route to assistant / packs / vision / diagnostics
#   - provide fallback responses
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

from typing import Dict, Any

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileNLRouter:
    """
    Natural-language router for mobile runtime.
    Converts raw text input into structured MobileEvent objects.
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main entry
    # ------------------------------------------------------------

    def route(self, text: str) -> Dict[str, Any]:
        """
        Main NL routing method.
        Converts text → MobileEvent → runtime dispatch.
        """

        if not text or not isinstance(text, str):
            return {
                "status": "error",
                "reason": "invalid_text"
            }

        intent = self._classify_intent(text)
        event = self._build_event(intent, text)

        # Dispatch event through runtime
        try:
            result = self.context.runtime.handle_event(event)
        except Exception as e:
            return {
                "status": "error",
                "reason": "runtime_failure",
                "error": str(e)
            }

        return result

    # ------------------------------------------------------------
    # Intent classification
    # ------------------------------------------------------------

    def _classify_intent(self, text: str) -> str:
        """
        Simple rule-based intent classifier.
        GAMA 3.x allows replacing this with ML model later.
        """

        t = text.lower().strip()

        # Diagnostics
        if "battery" in t:
            return "CHECK_BATTERY"
        if "temperature" in t or "hot" in t:
            return "CHECK_THERMAL"
        if "storage" in t or "space" in t:
            return "CHECK_STORAGE"
        if "diagnostic" in t:
            return "DIAGNOSTICS_REPORT"

        # Vision
        if "ocr" in t:
            return "OCR"
        if "detect" in t:
            return "DETECT"
        if "scene" in t:
            return "SCENE"
        if "homework" in t:
            return "HOMEWORK"

        # Packs
        if "pack" in t and "load" in t:
            return "PACK_LOAD"
        if "pack" in t and "info" in t:
            return "PACK_INFO"
        if "pack" in t and ("ask" in t or "query" in t):
            return "PACK_QUERY"

        # Security
        if "permission" in t:
            return "PERMISSION_CHECK"
        if "restricted" in t:
            return "RESTRICTED_MODE"

        # Default → assistant
        return "ASSISTANT"

    # ------------------------------------------------------------
    # Event builder
    # ------------------------------------------------------------

    def _build_event(self, intent: str, text: str) -> MobileEvent:
        """
        Convert intent + text into MobileEvent.
        """

        # Map intent → MobileEventTypes
        mapping = {
            "CHECK_BATTERY": MobileEventTypes.CHECK_BATTERY,
            "CHECK_THERMAL": MobileEventTypes.CHECK_THERMAL,
            "CHECK_STORAGE": MobileEventTypes.CHECK_STORAGE,
            "DIAGNOSTICS_REPORT": MobileEventTypes.DIAGNOSTICS_REPORT,

            "OCR": MobileEventTypes.OCR,
            "DETECT": MobileEventTypes.DETECT,
            "SCENE": MobileEventTypes.SCENE,
            "HOMEWORK": MobileEventTypes.HOMEWORK,

            "PACK_LOAD": MobileEventTypes.PACK_LOAD,
            "PACK_INFO": MobileEventTypes.PACK_INFO,
            "PACK_QUERY": MobileEventTypes.PACK_QUERY,

            "PERMISSION_CHECK": MobileEventTypes.PERMISSION_CHECK,
            "RESTRICTED_MODE": MobileEventTypes.RESTRICTED_MODE,

            "ASSISTANT": MobileEventTypes.ASSISTANT,
        }

        event_type = mapping.get(intent, MobileEventTypes.ASSISTANT)

        return MobileEvent(
            type=event_type,
            payload={
                "text": text,
                "intent": intent
            }
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

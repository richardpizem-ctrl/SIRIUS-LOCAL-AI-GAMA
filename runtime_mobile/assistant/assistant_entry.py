# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Assistant Entry
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Upgraded for GAMA Runtime 3.1:
# - MobileEvent v3.1 (intent, confidence, metadata v3, tags, source)
# - Multi-intent routing v1
# - SCENE v1 routing
# - Hybrid Schoolwork v1 routing
# - Diagnostics v3 hook
# - Unified routing pipeline
# ============================================================

from typing import Dict, Any
from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileAssistantEntry:

    MODULE_VERSION = "3.1.0"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Event Hook (3.1)
    # ------------------------------------------------------------

    def on_event(self, event):
        """Passive hook for diagnostics v3."""
        if hasattr(self.context.runtime, "diagnostics"):
            self.context.runtime.diagnostics.record_assistant_event(event)

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:

        # Only ASSISTANT events are processed
        if event.type != MobileEventTypes.ASSISTANT:
            return {
                "status": "ignored",
                "reason": "unsupported_event",
                "event_type": event.type,
            }

        # Unified text extraction (3.1)
        text = self._extract_text(event)
        intent = event.intent or ""
        confidence = event.confidence or 0.0

        # Try routing to specialized modules
        routed = self._try_specialized_modules(text, intent, confidence)
        if routed is not None:
            return routed

        # Fallback
        return self._fallback_response(text)

    # ------------------------------------------------------------
    # Specialized Routing (3.1)
    # ------------------------------------------------------------

    def _try_specialized_modules(self, text: str, intent: str, confidence: float):

        t = text.lower()

        # Knowledge Packs
        if "pack" in t or intent == "knowledge_query":
            return self._route_to_packs(text)

        # Diagnostics v3
        if any(k in t for k in ["battery", "temperature", "storage"]) or intent == "diagnostics":
            return self._route_to_diagnostics(text)

        # Vision / OCR / Scene
        if any(k in t for k in ["ocr", "detect", "scene", "homework"]) or intent == "vision":
            return self._route_to_vision(text)

        # Security
        if "permission" in t or "restricted" in t or intent == "security":
            return self._route_to_security(text)

        return None

    # ------------------------------------------------------------
    # Routing Helpers
    # ------------------------------------------------------------

    def _route_to_packs(self, text: str):
        packs = getattr(self.context.runtime, "packs", None)
        if not packs:
            return {"status": "error", "reason": "packs_not_available"}

        event = MobileEvent(
            type=MobileEventTypes.PACK_QUERY,
            raw_input=text,
            normalized_input=text.lower(),
            payload={"text": text, "query": text},
        )
        return self.context.runtime.handle_event(event)

    def _route_to_diagnostics(self, text: str):
        diagnostics = getattr(self.context.runtime, "diagnostics", None)
        if not diagnostics:
            return {"status": "error", "reason": "diagnostics_not_available"}

        event = MobileEvent(
            type=MobileEventTypes.DIAGNOSTICS_REPORT,
            raw_input=text,
            normalized_input=text.lower(),
            payload={"text": text},
        )
        return self.context.runtime.handle_event(event)

    def _route_to_vision(self, text: str):
        vision = getattr(self.context.runtime, "vision", None)
        if not vision:
            return {"status": "error", "reason": "vision_not_available"}

        event = MobileEvent(
            type=MobileEventTypes.SCENE,
            raw_input=text,
            normalized_input=text.lower(),
            payload={"text": text},
            tags=["vision"],
        )
        return self.context.runtime.handle_event(event)

    def _route_to_security(self, text: str):
        security = getattr(self.context.runtime, "security", None)
        if not security:
            return {"status": "error", "reason": "security_not_available"}

        event = MobileEvent(
            type=MobileEventTypes.PERMISSION_CHECK,
            raw_input=text,
            normalized_input=text.lower(),
            payload={"text": text},
        )
        return self.context.runtime.handle_event(event)

    # ------------------------------------------------------------
    # Fallback Response
    # ------------------------------------------------------------

    def _fallback_response(self, text: str) -> Dict[str, Any]:
        return {
            "status": "ok",
            "type": "assistant_fallback",
            "input": text,
            "response": f"I understood: '{text}'. How can I help you further?"
        }

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _extract_text(self, event: MobileEvent) -> str:
        """Unified text extraction for MobileEvent 3.1."""
        if event.normalized_input:
            return event.normalized_input
        if event.raw_input:
            return event.raw_input
        return event.payload.get("text", "")

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> Dict[str, Any]:
        return {
            "module": "assistant",
            "version": self.MODULE_VERSION,
            "context_attached": self.context is not None,
        }

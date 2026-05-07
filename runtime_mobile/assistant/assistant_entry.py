# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Assistant Entry
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Central assistant logic for the mobile runtime.
# Responsibilities:
#   - interpret NL events
#   - route to packs / diagnostics / vision / security
#   - provide fallback responses
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

from typing import Dict, Any

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileAssistantEntry:
    """
    Central assistant logic for the mobile runtime.
    Handles ASSISTANT events and provides fallback responses.
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:
        """
        Main processing method for assistant events.
        """

        if event.type != MobileEventTypes.ASSISTANT:
            return {
                "status": "ignored",
                "reason": "unsupported_event",
                "event_type": event.type,
            }

        text = event.payload.get("text", "")
        intent = event.payload.get("intent", "")

        # Try routing to specialized modules
        routed = self._try_specialized_modules(text, intent)
        if routed is not None:
            return routed

        # Fallback → generic assistant response
        return self._fallback_response(text)

    # ------------------------------------------------------------
    # Specialized Routing
    # ------------------------------------------------------------

    def _try_specialized_modules(self, text: str, intent: str):
        """
        Try routing to packs, diagnostics, vision, or security
        based on text patterns.
        """

        t = text.lower()

        # Packs
        if "pack" in t:
            return self._route_to_packs(text)

        # Diagnostics
        if "battery" in t or "temperature" in t or "storage" in t:
            return self._route_to_diagnostics(text)

        # Vision
        if "ocr" in t or "detect" in t or "scene" in t or "homework" in t:
            return self._route_to_vision(text)

        # Security
        if "permission" in t or "restricted" in t:
            return self._route_to_security(text)

        return None

    # ------------------------------------------------------------
    # Routing Helpers
    # ------------------------------------------------------------

    def _route_to_packs(self, text: str):
        if not self.context.packs:
            return {"status": "error", "reason": "packs_not_available"}

        event = MobileEvent(
            type=MobileEventTypes.PACK_QUERY,
            payload={"text": text, "query": text, "pack_id": "default"}
        )
        return self.context.runtime.handle_event(event)

    def _route_to_diagnostics(self, text: str):
        if not self.context.diagnostics:
            return {"status": "error", "reason": "diagnostics_not_available"}

        event = MobileEvent(
            type=MobileEventTypes.DIAGNOSTICS_REPORT,
            payload={"text": text}
        )
        return self.context.runtime.handle_event(event)

    def _route_to_vision(self, text: str):
        if not self.context.vision:
            return {"status": "error", "reason": "vision_not_available"}

        event = MobileEvent(
            type=MobileEventTypes.SCENE,
            payload={"text": text, "image": None}
        )
        return self.context.runtime.handle_event(event)

    def _route_to_security(self, text: str):
        if not self.context.security:
            return {"status": "error", "reason": "security_not_available"}

        event = MobileEvent(
            type=MobileEventTypes.PERMISSION_CHECK,
            payload={"text": text, "permission": text}
        )
        return self.context.runtime.handle_event(event)

    # ------------------------------------------------------------
    # Fallback Response
    # ------------------------------------------------------------

    def _fallback_response(self, text: str) -> Dict[str, Any]:
        """
        Default assistant response when no module handles the request.
        """

        return {
            "status": "ok",
            "type": "assistant_fallback",
            "input": text,
            "response": f"I understood: '{text}'. How can I help you further?"
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> Dict[str, Any]:
        return {
            "module": "assistant",
            "version": self.MODULE_VERSION,
            "context_attached": self.context is not None,
        }

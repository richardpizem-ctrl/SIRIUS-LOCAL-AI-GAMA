# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Assistant Entry
# Version: 3.0.0-pre
# ============================================================

from typing import Dict, Any
from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileAssistantEntry:

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Event Hook (3.x)
    # ------------------------------------------------------------

    def on_event(self, event):
        """Passive hook (optional)."""
        pass

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:

        if event.type != MobileEventTypes.ASSISTANT:
            return {
                "status": "ignored",
                "reason": "unsupported_event",
                "event_type": event.type,
            }

        text = event.payload.get("text", "")
        intent = event.payload.get("intent", "")

        routed = self._try_specialized_modules(text, intent)
        if routed is not None:
            return routed

        return self._fallback_response(text)

    # ------------------------------------------------------------
    # Specialized Routing
    # ------------------------------------------------------------

    def _try_specialized_modules(self, text: str, intent: str):

        t = text.lower()

        if "pack" in t:
            return self._route_to_packs(text)

        if "battery" in t or "temperature" in t or "storage" in t:
            return self._route_to_diagnostics(text)

        if "ocr" in t or "detect" in t or "scene" in t or "homework" in t:
            return self._route_to_vision(text)

        if "permission" in t or "restricted" in t:
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
            payload={"text": text, "query": text}
        )
        return self.context.runtime.handle_event(event)

    def _route_to_diagnostics(self, text: str):

        diagnostics = getattr(self.context.runtime, "diagnostics", None)
        if not diagnostics:
            return {"status": "error", "reason": "diagnostics_not_available"}

        event = MobileEvent(
            type=MobileEventTypes.DIAGNOSTICS_REPORT,
            payload={"text": text}
        )
        return self.context.runtime.handle_event(event)

    def _route_to_vision(self, text: str):

        vision = getattr(self.context.runtime, "vision", None)
        if not vision:
            return {"status": "error", "reason": "vision_not_available"}

        event = MobileEvent(
            type=MobileEventTypes.SCENE,
            payload={"text": text}
        )
        return self.context.runtime.handle_event(event)

    def _route_to_security(self, text: str):

        security = getattr(self.context.runtime, "security", None)
        if not security:
            return {"status": "error", "reason": "security_not_available"}

        event = MobileEvent(
            type=MobileEventTypes.PERMISSION_CHECK,
            payload={"text": text}
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
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> Dict[str, Any]:
        return {
            "module": "assistant",
            "version": self.MODULE_VERSION,
            "context_attached": self.context is not None,
        }

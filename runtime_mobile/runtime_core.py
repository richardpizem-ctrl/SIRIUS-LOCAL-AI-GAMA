# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Core
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.core.mobile_event import MobileEvent


class MobileRuntimeCore:
    """
    Core execution engine for SIRIUS LOCAL AI GAMA.
    Handles initialization, module loading, event dispatching,
    and communication with the mobile NL Router.
    """

    CORE_VERSION = "3.1.0"

    def __init__(self, context, dispatcher, router):
        self.context = context
        self.dispatcher = dispatcher
        self.router = router
        self.initialized = False

        # Link router → dispatcher + context
        self.router.dispatcher = dispatcher
        self.router.context = context

        # Optional back-reference
        self.context.runtime_core = self

    # ------------------------------------------------------------
    # Module Loading
    # ------------------------------------------------------------

    def load_modules(
        self,
        vision,
        security,
        packs,
        diagnostics=None,
        governor=None,
        workflow=None,
        lan_bridge=None,
        pack_manager=None,
        assistant=None,
    ):
        self.context.vision_engine = vision
        self.context.security = security
        self.context.knowledge_packs = packs
        self.context.diagnostics = diagnostics
        self.context.energy_governor = governor
        self.context.workflow = workflow
        self.context.lan_bridge = lan_bridge
        self.context.assistant = assistant

        if pack_manager is not None:
            self.context.pack_manager = pack_manager

    # ------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------

    def initialize(self):
        required = [
            self.router,
            self.dispatcher,
            self.context.vision_engine,
            self.context.security,
            self.context.knowledge_packs,
        ]

        if not all(required):
            raise RuntimeError("Runtime modules not fully loaded.")

        self.initialized = True
        self.context.mark_initialized()

        return {
            "status": "initialized",
            "core_version": self.CORE_VERSION,
        }

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def on_event(self, payload):
        """
        Main event handler for mobile runtime.
        Accepts:
          - str (natural language) → routed via NL router
          - MobileEvent → dispatched directly
        Pipeline:
          text → MobileEvent → security → governor → dispatch → result
        """

        if not self.initialized:
            raise RuntimeError("Runtime not initialized.")

        # 1. Normalize input to MobileEvent
        if isinstance(payload, MobileEvent):
            event = payload
        elif isinstance(payload, str):
            try:
                event = self.router.route(payload)
            except Exception as e:
                return {
                    "status": "error",
                    "reason": "routing_failed",
                    "error": str(e),
                }
        else:
            return {
                "status": "error",
                "reason": "invalid_input_type",
                "type": type(payload).__name__,
            }

        # 2. Update context
        self.context.update_last_event(event)

        # 3. Security pipeline
        if self.context.security is not None:
            sec = self.context.security.on_event(event)
            if isinstance(sec, dict) and sec.get("allowed") is False:
                return {
                    "status": "blocked",
                    "reason": "security_denied",
                    "event": event.type,
                }

        # 4. Energy governor (optional)
        if self.context.energy_governor is not None:
            gov = self.context.energy_governor.on_event(event)
            if isinstance(gov, dict) and gov.get("blocked") is True:
                return {
                    "status": "blocked",
                    "reason": "governor_blocked",
                    "event": event.type,
                }

        # 5. Dispatch event to correct module
        try:
            result = self.dispatcher.dispatch(event)
        except Exception as e:
            return {
                "status": "error",
                "reason": "dispatch_failed",
                "error": str(e),
                "event_type": getattr(event, "type", None),
            }

        # 6. Track active module
        if isinstance(result, dict) and "module" in result:
            self.context.set_active_module(result["module"])

        return result

    # ------------------------------------------------------------
    # Convenience: runtime info event
    # ------------------------------------------------------------

    def runtime_info(self):
        """Return runtime info in the same shape as a dispatched event."""
        return {
            "status": "ok",
            "type": MobileEventTypes.RUNTIME_INFO,
            "core_version": self.CORE_VERSION,
            "context": self.context.get_info(),
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "core_version": self.CORE_VERSION,
            "initialized": self.initialized,
            "context": self.context.get_info(),
        }

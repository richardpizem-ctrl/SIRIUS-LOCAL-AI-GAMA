# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Core
# Version: 3.0.0-pre
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.core.mobile_event import MobileEvent


class MobileRuntimeCore:
    """
    Core execution engine for SIRIUS LOCAL AI GAMA.
    Handles initialization, module loading, event dispatching,
    and communication with the mobile NL Router.
    """

    CORE_VERSION = "3.0.0-pre"

    def __init__(self, context, dispatcher, router):
        self.context = context
        self.dispatcher = dispatcher
        self.router = router
        self.initialized = False

        # Link router → dispatcher
        self.router.dispatcher = dispatcher
        self.router.context = context

    # ------------------------------------------------------------
    # Module Loading
    # ------------------------------------------------------------

    def load_modules(self, vision, security, packs,
                     diagnostics=None, governor=None,
                     workflow=None, lan_bridge=None):

        self.context.vision_engine = vision
        self.context.security = security
        self.context.knowledge_packs = packs
        self.context.diagnostics = diagnostics
        self.context.energy_governor = governor
        self.context.workflow = workflow
        self.context.lan_bridge = lan_bridge

    # ------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------

    def initialize(self):
        required = [
            self.router,
            self.dispatcher,
            self.context.vision_engine,
            self.context.security,
            self.context.knowledge_packs
        ]

        if not all(required):
            raise RuntimeError("Runtime modules not fully loaded.")

        self.initialized = True
        self.context.state["initialized"] = True

        return {"status": "initialized", "core_version": self.CORE_VERSION}

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def on_event(self, text: str):
        """
        Main event handler for mobile runtime.
        Converts text → MobileEvent → security → dispatch → result.
        """

        if not self.initialized:
            raise RuntimeError("Runtime not initialized.")

        # 1. Route text to event
        event = self.router.route(text)

        # 2. Update context
        self.context.update_last_event(event)

        # 3. Security pipeline
        sec = self.context.security.on_event(event)
        if isinstance(sec, dict) and sec.get("allowed") is False:
            return {
                "status": "blocked",
                "reason": "security_denied",
                "event": event.type
            }

        # 4. Dispatch event to correct module
        result = self.dispatcher.dispatch(event)

        # 5. Track active module
        if isinstance(result, dict) and "module" in result:
            self.context.set_active_module(result["module"])

        return result

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "core_version": self.CORE_VERSION,
            "initialized": self.initialized,
            "context": self.context.get_info(),
        }

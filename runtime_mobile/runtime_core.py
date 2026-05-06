# SIRIUS LOCAL AI GAMA - Mobile Runtime Core
# Main runtime controller for the mobile offline execution environment.

from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.core.event import MobileEvent

class MobileRuntimeCore:
    """
    Core execution engine for SIRIUS LOCAL AI GAMA.
    Handles initialization, module loading, event dispatching,
    and communication with the mobile NL Router.
    """

    def __init__(self, context, dispatcher, router):
        self.context = context
        self.dispatcher = dispatcher
        self.router = router
        self.initialized = False

    def load_modules(self, vision, security, packs):
        """Attach core modules to the runtime and context."""
        self.context.vision_engine = vision
        self.context.security_engine = security
        self.context.knowledge_packs = packs

    def initialize(self):
        """Initialize the mobile runtime."""
        if not all([
            self.router,
            self.dispatcher,
            self.context.vision_engine,
            self.context.security_engine,
            self.context.knowledge_packs
        ]):
            raise RuntimeError("Runtime modules not fully loaded.")

        self.initialized = True

    def handle_event(self, text: str):
        """
        Main event handler for mobile runtime.
        Converts text → MobileEvent → dispatch → module result.
        """
        if not self.initialized:
            raise RuntimeError("Runtime not initialized.")

        # 1. Route text to event
        event = self.router.route(text)

        # 2. Update context
        self.context.update_last_event(event)

        # 3. Security check
        decision = self.context.security_engine.evaluate(event)
        if decision == "deny":
            return {"status": "blocked", "reason": "security"}

        # 4. Dispatch event to correct module
        return self.dispatcher.dispatch(event)

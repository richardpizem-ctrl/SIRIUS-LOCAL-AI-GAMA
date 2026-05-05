# SIRIUS LOCAL AI GAMA - Mobile Runtime Core
# Main runtime controller for the mobile offline execution environment.

class MobileRuntimeCore:
    """
    Core execution engine for SIRIUS LOCAL AI GAMA.
    Handles initialization, module loading, event dispatching,
    and communication with the mobile NL Router.
    """

    def __init__(self):
        self.router = None
        self.vision = None
        self.security = None
        self.packs = None
        self.initialized = False

    def load_modules(self, router, vision, security, packs):
        """Attach core modules to the runtime."""
        self.router = router
        self.vision = vision
        self.security = security
        self.packs = packs

    def initialize(self):
        """Initialize the mobile runtime."""
        if not all([self.router, self.vision, self.security, self.packs]):
            raise RuntimeError("Runtime modules not fully loaded.")

        self.initialized = True

    def handle_event(self, event):
        """
        Main event handler for mobile runtime.
        Routes events through security, router, and module logic.
        """
        if not self.initialized:
            raise RuntimeError("Runtime not initialized.")

        # 1. Security check
        decision = self.security.evaluate(event)
        if decision == "deny":
            return {"status": "blocked", "reason": "security"}

        # 2. Route event
        intent = self.router.route(event)

        # 3. Execute intent
        return self.execute_intent(intent, event)

    def execute_intent(self, intent, event):
        """Execute routed intent using the appropriate module."""
        if intent == "vision":
            return self.vision.process(event)

        if intent == "knowledge":
            return self.packs.query(event)

        return {"status": "unknown_intent", "intent": intent}

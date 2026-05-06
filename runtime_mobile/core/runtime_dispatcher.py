class MobileRuntimeDispatcher:
    """
    Dispatcher for the GAMA mobile runtime.
    Routes events to registered module handlers.
    """

    def __init__(self, context):
        self.context = context
        self.handlers = {}

        # Automatically register all module handlers
        self.register_handlers()

    def register_handler(self, event_type: str, handler):
        """
        Registers a handler for a specific event type.
        Handler must be a callable object.
        """
        self.handlers[event_type] = handler

    def register_handlers(self):
        """
        Registers handlers for all mobile runtime modules.
        """

        # SECURITY MODULE
        if hasattr(self.context, "security"):
            self.register_handler(
                "security",
                self.context.security.evaluate
            )

        # VISION MODULE
        if hasattr(self.context, "vision"):
            self.register_handler(
                "vision",
                self.context.vision.process
            )

        # KNOWLEDGE PACKS MODULE
        if hasattr(self.context, "packs"):
            self.register_handler(
                "packs",
                self.context.packs.get
            )

    def dispatch(self, event):
        """
        Dispatches an event based on its type.
        If a handler exists → it is executed.
        If not → returns None.
        """
        event_type = event.get("type")
        handler = self.handlers.get(event_type)

        if handler:
            return handler(event)

        return {
            "status": "ignored",
            "reason": "no_handler",
            "event_type": event_type
        }

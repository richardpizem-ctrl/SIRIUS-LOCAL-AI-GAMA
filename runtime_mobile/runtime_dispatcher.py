# SIRIUS LOCAL AI GAMA - Mobile Runtime Dispatcher

class MobileRuntimeDispatcher:
    """
    Dispatches events to the runtime core.
    Acts as a bridge between UI layer and MobileRuntimeCore.
    """

    def __init__(self, runtime_core, context):
        self.runtime = runtime_core
        self.context = context

    def dispatch(self, event):
        """Main entry point for incoming events."""
        self.context.update_last_event(event)
        return self.runtime.handle_event(event)

# SIRIUS LOCAL AI GAMA - Mobile Runtime Dispatcher

from runtime_mobile.core.event_types import MobileEventTypes

class MobileRuntimeDispatcher:
    """
    Dispatches MobileEvent objects to the correct runtime module.
    Acts as a bridge between the NL Router and runtime modules.
    """

    def __init__(self, context):
        self.context = context

    def dispatch(self, event):
        """Dispatch event to the correct module based on event type."""
        self.context.update_last_event(event)

        etype = event.type

        # --- Vision ---
        if etype in [MobileEventTypes.OCR, MobileEventTypes.ANALYZE]:
            return self.context.vision_engine.process(event)

        # --- Knowledge Packs ---
        if etype == MobileEventTypes.PACK_LOOKUP:
            return self.context.knowledge_packs.handle_event(event)

        # --- Security ---
        if etype in [MobileEventTypes.SECURITY, MobileEventTypes.RESTRICTED_MODE]:
            return self.context.security_engine.handle(event)

        # --- Help ---
        if etype == MobileEventTypes.SHOW_HELP:
            return {"status": "ok", "help": "Available commands: scan, explain, security, help"}

        # --- Unknown ---
        return {
            "status": "unknown_event",
            "event_type": etype
        }

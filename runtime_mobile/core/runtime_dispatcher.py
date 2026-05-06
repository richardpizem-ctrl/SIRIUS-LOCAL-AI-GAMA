from runtime_mobile.core.event_types import MobileEventTypes


class MobileRuntimeDispatcher:
    """
    Central dispatcher for the GAMA mobile runtime.
    Routes MobileEvent objects to the correct module.
    """

    def __init__(self, context):
        self.context = context

    def dispatch(self, event):
        """
        Dispatches an event to the correct module based on event.type.
        Returns the module response.
        """

        # --- SECURITY MODULE ---
        if event.type in (
            MobileEventTypes.SECURITY,
            MobileEventTypes.RESTRICTED_MODE
        ):
            return self.context.security.handle_event(event)

        # --- VISION MODULE ---
        if event.type in (
            MobileEventTypes.OCR,
            MobileEventTypes.ANALYZE
        ):
            return self.context.vision.handle_event(event)

        # --- KNOWLEDGE PACKS MODULE ---
        if event.type == MobileEventTypes.PACK_LOOKUP:
            return self.context.packs.handle_event(event)

        # --- APP CONTROL ---
        if event.type == MobileEventTypes.OPEN_APP:
            return {
                "status": "ok",
                "action": "open_app"
            }

        # --- DEVICE STATUS ---
        if event.type == MobileEventTypes.CHECK_BATTERY:
            return {
                "status": "ok",
                "battery": "unknown"
            }

        if event.type == MobileEventTypes.CHECK_WIFI:
            return {
                "status": "ok",
                "wifi": "unknown"
            }

        # --- HELP ---
        if event.type == MobileEventTypes.SHOW_HELP:
            return {
                "status": "ok",
                "help": "Available commands: lookup, open, battery, wifi, read, analyze"
            }

        # --- UNKNOWN ---
        return {
            "status": "error",
            "reason": "unknown_event",
            "event_type": event.type
        }

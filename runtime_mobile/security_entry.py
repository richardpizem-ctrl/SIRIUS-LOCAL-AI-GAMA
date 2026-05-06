# SIRIUS LOCAL AI GAMA - Mobile Security Layer

from runtime_mobile.core.event_types import MobileEventTypes

class MobileSecurityEntry:
    """
    Mobile security evaluation layer.
    Handles permission checks, restricted mode, and unsafe text filtering.
    """

    def __init__(self, context):
        self.context = context

    def evaluate(self, event):
        etype = event.type

        # --- Restricted Mode Toggle ---
        if etype == MobileEventTypes.RESTRICTED_MODE:
            enabled = event.get("enabled", False)
            self.context.state.set_restricted_mode(enabled)
            return "allow"

        # --- Permission Check ---
        if etype == MobileEventTypes.SECURITY:
            permission = event.get("permission")
            allowed = self.context.permissions.is_allowed(permission)
            return "allow" if allowed else "deny"

        # --- Text Safety Filter ---
        text = event.get("text", "").lower()
        forbidden = ["hack", "bypass", "cheat", "exploit"]

        if any(word in text for word in forbidden):
            return "deny"

        return "allow"

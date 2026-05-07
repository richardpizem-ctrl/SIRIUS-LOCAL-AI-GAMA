# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Security Entry
# Version: 3.0.0-pre
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes


class MobileSecurityEntry:
    """
    Mobile security evaluation layer.
    Handles permission checks, restricted mode, and unsafe text filtering.
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context
        self.security_profile = "OWNER"  # OWNER / FAMILY / STRANGER

    # ------------------------------------------------------------
    # Main Event Handler (required by runtime)
    # ------------------------------------------------------------

    def on_event(self, event):
        et = event.type

        # Restricted Mode Toggle
        if et == MobileEventTypes.RESTRICTED_MODE:
            return self._handle_restricted_mode(event)

        # Permission Check
        if et == MobileEventTypes.PERMISSION_CHECK:
            return self._check_permission(event)

        # Text Safety Filter (only for text-based events)
        if hasattr(event, "text") and isinstance(event.text, str):
            return self._text_safety(event)

        return {"status": "ok", "allowed": True}

    # ------------------------------------------------------------
    # Restricted Mode
    # ------------------------------------------------------------

    def _handle_restricted_mode(self, event):
        enabled = getattr(event, "enabled", False)
        self.context.set_restricted_mode(enabled)

        return {
            "status": "ok",
            "restricted_mode": enabled,
            "profile": self.security_profile
        }

    # ------------------------------------------------------------
    # Permission Check
    # ------------------------------------------------------------

    def _check_permission(self, event):
        permission = getattr(event, "permission", "generic")

        if not hasattr(self.context, "permissions"):
            return {
                "status": "error",
                "reason": "permissions_not_configured",
                "allowed": False
            }

        allowed = self.context.permissions.is_allowed(permission)

        return {
            "status": "ok",
            "permission": permission,
            "allowed": allowed,
            "profile": self.security_profile
        }

    # ------------------------------------------------------------
    # Text Safety Filter
    # ------------------------------------------------------------

    def _text_safety(self, event):
        text = event.text.lower()

        forbidden = ["hack", "bypass", "cheat", "exploit"]

        if any(w in text for w in forbidden):
            return {
                "status": "blocked",
                "reason": "unsafe_text",
                "allowed": False
            }

        return {"status": "ok", "allowed": True}

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "module": "security",
            "version": self.MODULE_VERSION,
            "profile": self.security_profile,
            "restricted_mode": self.context.state.get("restricted_mode")
        }

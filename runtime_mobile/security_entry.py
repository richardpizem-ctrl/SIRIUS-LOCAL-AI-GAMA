# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Security Entry
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes


class MobileSecurityEntry:
    """
    Mobile security evaluation layer.
    Handles:
    - permission checks
    - restricted mode
    - unsafe text filtering
    - security alerts
    """

    MODULE_VERSION = "3.1.0"

    def __init__(self, context):
        self.context = context
        self.security_profile = "OWNER"  # OWNER / FAMILY / STRANGER

        # Forbidden keywords (expandable)
        self.forbidden_keywords = [
            "hack", "bypass", "cheat", "exploit",
            "root", "jailbreak", "ddos", "breach"
        ]

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def on_event(self, event):
        et = getattr(event, "type", None)

        # Restricted Mode Toggle
        if et == MobileEventTypes.RESTRICTED_MODE:
            return self._handle_restricted_mode(event)

        # Permission Check
        if et == MobileEventTypes.PERMISSION_CHECK:
            return self._check_permission(event)

        # Security Alert
        if et == MobileEventTypes.SECURITY_ALERT:
            return self._security_alert(event)

        # Text Safety Filter (only for text-based events)
        if hasattr(event, "text") and isinstance(event.text, str):
            return self._text_safety(event)

        return {"status": "ok", "allowed": True}

    # ------------------------------------------------------------
    # Restricted Mode
    # ------------------------------------------------------------

    def _handle_restricted_mode(self, event):
        enabled = getattr(event, "enabled", False)
        self.context.set_restricted_mode(bool(enabled))

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

        try:
            allowed = self.context.permissions.is_allowed(permission)
        except Exception as e:
            return {
                "status": "error",
                "reason": "permission_check_failed",
                "error": str(e),
                "allowed": False
            }

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

        if any(w in text for w in self.forbidden_keywords):
            return {
                "status": "blocked",
                "reason": "unsafe_text",
                "allowed": False
            }

        # Restricted mode blocks all assistant/text queries except safe ones
        if self.context.state.get("restricted_mode"):
            if any(k in text for k in ["search", "explain", "write", "generate"]):
                return {
                    "status": "blocked",
                    "reason": "restricted_mode_active",
                    "allowed": False
                }

        return {"status": "ok", "allowed": True}

    # ------------------------------------------------------------
    # Security Alert
    # ------------------------------------------------------------

    def _security_alert(self, event):
        message = getattr(event, "message", "unknown_alert")
        self.context.log(f"SECURITY ALERT: {message}")

        return {
            "status": "ok",
            "alert": message,
            "profile": self.security_profile
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "module": "security",
            "version": self.MODULE_VERSION,
            "profile": self.security_profile,
            "restricted_mode": self.context.state.get("restricted_mode"),
            "forbidden_keywords": list(self.forbidden_keywords)
        }

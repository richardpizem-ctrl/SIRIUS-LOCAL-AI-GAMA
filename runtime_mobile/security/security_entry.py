# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Security Entry
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Entry point for the mobile security module.
# Responsibilities:
#   - permission checks
#   - restricted mode handling
#   - security profile logic (OWNER / FAMILY / STRANGER)
#   - safe event evaluation
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes


class MobileSecurityEntry:
    """
    Entry point for the mobile security module.
    Handles permission checks, safety evaluation and restricted-mode logic.
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

        # Default security profile (runtime may override)
        self.security_profile = "OWNER"  # OWNER / FAMILY / STRANGER

    # ------------------------------------------------------------
    # Main Evaluation
    # ------------------------------------------------------------

    def handle_event(self, event):
        """
        Main evaluation method for security events.
        """

        et = event.type

        if et == MobileEventTypes.PERMISSION_CHECK:
            return self._check_permission(event)

        if et == MobileEventTypes.RESTRICTED_MODE:
            return self._handle_restricted_mode(event)

        return {
            "status": "ignored",
            "reason": "unknown_event",
            "event_type": et
        }

    # ------------------------------------------------------------
    # Permission Check
    # ------------------------------------------------------------

    def _check_permission(self, event):
        permission = event.get("permission")

        # If permissions system is missing → deny by default
        if not self.context.permissions:
            return {
                "status": "error",
                "reason": "permissions_not_configured",
                "permission": permission
            }

        allowed = self.context.permissions.is_allowed(permission)

        return {
            "status": "ok",
            "permission": permission,
            "allowed": allowed,
            "profile": self.security_profile
        }

    # ------------------------------------------------------------
    # Restricted Mode
    # ------------------------------------------------------------

    def _handle_restricted_mode(self, event):
        enabled = event.get("enabled", False)

        # Update runtime state
        self.context.set_restricted_mode(enabled)

        return {
            "status": "ok",
            "restricted_mode": enabled,
            "profile": self.security_profile
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        """Return module metadata."""
        return {
            "module": "security",
            "version": self.MODULE_VERSION,
            "profile": self.security_profile,
            "restricted_mode": self.context.state.get("restricted_mode"),
        }

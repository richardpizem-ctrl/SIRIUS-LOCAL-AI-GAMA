# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Security Entry
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for GAMA Runtime 3.1:
# - unified restricted_mode pipeline
# - MobilePermissions v3 sync
# - MobileEvent 3.1 metadata compatibility
# - stable structured responses
# ============================================================

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileSecurityEntry:

    MODULE_VERSION = "3.1.0"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main Evaluation
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent):

        et = event.type

        if et == MobileEventTypes.PERMISSION_CHECK:
            return self._check_permission(event)

        if et == MobileEventTypes.RESTRICTED_MODE:
            return self._handle_restricted_mode(event)

        if et == MobileEventTypes.SECURITY:
            return self._handle_security_event(event)

        return {
            "status": "ignored",
            "reason": "unknown_event",
            "event_type": et
        }

    # ------------------------------------------------------------
    # Permission Check (3.1)
    # ------------------------------------------------------------

    def _check_permission(self, event: MobileEvent):

        permission = event.get("permission")

        if not self.context.permissions:
            return {
                "status": "error",
                "reason": "permissions_not_configured",
                "permission": permission
            }

        # Restricted mode → STRANGER → deny
        if self.context.is_restricted_mode():
            allowed = False
            profile = "STRANGER"
        else:
            allowed = self.context.permissions.is_allowed(permission)
            profile = self.context.permissions.get_profile()

        return {
            "status": "ok",
            "permission": permission,
            "allowed": allowed,
            "profile": profile
        }

    # ------------------------------------------------------------
    # Restricted Mode (3.1)
    # ------------------------------------------------------------

    def _handle_restricted_mode(self, event: MobileEvent):

        enabled = event.get("enabled", False)

        # Update runtime state
        self.context.set_restricted_mode(enabled)

        # Sync permissions profile
        if enabled:
            self.context.permissions.set_profile("STRANGER")
        else:
            self.context.permissions.set_profile("OWNER")

        return {
            "status": "ok",
            "restricted_mode": enabled,
            "profile": self.context.permissions.get_profile()
        }

    # ------------------------------------------------------------
    # SECURITY (generic)
    # ------------------------------------------------------------

    def _handle_security_event(self, event: MobileEvent):
        return {
            "status": "ok",
            "type": "security_event",
            "restricted_mode": self.context.is_restricted_mode(),
            "profile": self.context.permissions.get_profile()
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "module": "security",
            "version": self.MODULE_VERSION,
            "profile": self.context.permissions.get_profile(),
            "restricted_mode": self.context.is_restricted_mode(),
        }

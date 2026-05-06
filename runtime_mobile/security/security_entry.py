class MobileSecurityEntry:
    """
    Entry point for the mobile security module.
    Handles permission checks, safety evaluation and restricted-mode logic.
    """

    def __init__(self, context):
        self.context = context

    def evaluate(self, event):
        """
        Main evaluation method for security events.
        Returns a SecurityResult object or boolean depending on implementation.
        """
        event_type = event.get("type")

        if event_type == "permission_check":
            return self._check_permission(event)

        if event_type == "restricted_mode":
            return self._handle_restricted_mode(event)

        return {"status": "ignored", "reason": "unknown_event"}

    def _check_permission(self, event):
        permission = event.get("permission")
        allowed = self.context.permissions.is_allowed(permission)

        return {
            "permission": permission,
            "allowed": allowed
        }

    def _handle_restricted_mode(self, event):
        enabled = event.get("enabled", False)
        self.context.state.set_restricted_mode(enabled)

        return {
            "restricted_mode": enabled,
            "status": "updated"
        }

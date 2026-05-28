"""
sandbox_core.py
----------------
Core sandbox controller for SIRIUS Mobile Runtime 3.3.0.

Responsibilities:
- Enforce strict sandbox boundaries
- Control allowed operations for each module
- Provide deterministic decision-making
- Block unauthorized actions immediately
- Integrate with SandboxMonitor and SandboxViolationHandler

This module is fully deterministic:
- No dynamic imports
- No reflection
- No eval/exec
Prepared for Self‑Repair Layer 4.4.
"""

from .sandbox_permissions import SandboxPermissions
from .sandbox_monitor import SandboxMonitor
from .sandbox_violation_handler import SandboxViolationHandler


class SandboxCore:
    """
    Central sandbox enforcement engine.
    All modules must pass through this layer before performing sensitive actions.
    """

    def __init__(self):
        self.permissions = SandboxPermissions()
        self.monitor = SandboxMonitor()
        self.violation_handler = SandboxViolationHandler()

    # -------------------------------------------------------------

    def check_permission(self, module_name: str, action: str) -> bool:
        """
        Main permission check.
        Returns True if allowed, False if blocked.
        """

        # Step 1: Monitor the request
        self.monitor.record_request(module_name, action)

        # Step 2: Permission lookup
        allowed = self.permissions.is_allowed(module_name, action)

        if not allowed:
            # Step 3: Log violation
            self.violation_handler.handle_violation(
                module_name=module_name,
                action=action,
                reason="permission_denied"
            )
            return False

        return True

    # -------------------------------------------------------------

    def enforce(self, module_name: str, action: str):
        """
        Raises an exception if the action is not allowed.
        Used by high‑security modules.
        """

        if not self.check_permission(module_name, action):
            raise PermissionError(
                f"[SANDBOX BLOCKED] Module '{module_name}' attempted forbidden action '{action}'."
            )

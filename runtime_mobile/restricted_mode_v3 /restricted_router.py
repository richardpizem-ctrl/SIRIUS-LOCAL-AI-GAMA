"""
restricted_router.py
--------------------
Router for Restricted Mode v3.

Responsibilities:
- Enforce behavioral restrictions
- Apply policy rules deterministically
- Filter unsafe or disallowed actions
- Integrate with Sandbox Enforcement v3
- Support SchoolMode v2 and Family Security 3.x

This module is fully deterministic:
- No dynamic imports
- No reflection
- No eval/exec
Prepared for Self‑Repair Layer 4.4.
"""

from .restricted_policy import RestrictedPolicy
from .restricted_filters import RestrictedFilters


class RestrictedRouter:
    """
    Main enforcement router for Restricted Mode v3.
    Evaluates actions against policy rules and filters.
    """

    def __init__(self):
        self.policy = RestrictedPolicy()
        self.filters = RestrictedFilters()

    # -------------------------------------------------------------

    def process_action(self, module_name: str, action: str, payload: dict) -> dict:
        """
        Main entry point for restricted mode evaluation.

        Returns:
            {
                "allowed": True/False,
                "reason": "...",
                "payload": payload (possibly sanitized)
            }
        """

        # Step 1: Policy check (hard rules)
        policy_result = self.policy.check(module_name, action)

        if not policy_result["allowed"]:
            return {
                "allowed": False,
                "reason": policy_result["reason"],
                "payload": None
            }

        # Step 2: Filter payload (soft rules)
        filtered_payload = self.filters.apply_filters(payload)

        if filtered_payload is None:
            return {
                "allowed": False,
                "reason": "filtered_blocked",
                "payload": None
            }

        # Passed all checks
        return {
            "allowed": True,
            "reason": None,
            "payload": filtered_payload
        }

"""
restricted_policy.py
--------------------
Policy layer for Restricted Mode v3.

Responsibilities:
- Define hard allow/deny rules for modules and actions
- Provide deterministic policy evaluation
- Integrate with RestrictedRouter
- Support SchoolMode v2 and Family Security 3.x

This module is fully deterministic:
- No dynamic imports
- No reflection
- No eval/exec
Prepared for Self‑Repair Layer 4.4.
"""


class RestrictedPolicy:
    """
    Deterministic policy engine for Restricted Mode v3.
    """

    # -------------------------------------------------------------
    # STATIC POLICY MATRIX (HARD RULES)
    # -------------------------------------------------------------
    POLICY = {
        "vision_engine": {
            "generate_image": True,
            "access_raw_files": False,
            "network_call": False,
        },

        "schoolwork_reasoning": {
            "solve_task": True,
            "bypass_restrictions": False,
            "access_system_files": False,
        },

        "event_engine": {
            "dispatch_event": True,
            "modify_security": False,
        },

        "sandbox_enforcement": {
            "enforce_sandbox": True,
            "disable_sandbox": False,
        },

        "quarantine_pipeline": {
            "quarantine_event": True,
            "delete_quarantine": False,
        },
    }

    # -------------------------------------------------------------

    def check(self, module_name: str, action: str) -> dict:
        """
        Evaluates whether a module is allowed to perform an action.

        Returns:
            {
                "allowed": True/False,
                "reason": "..."
            }
        """

        module = self.POLICY.get(module_name)
        if module is None:
            return self._deny("unknown_module")

        allowed = module.get(action)
        if allowed is None:
            return self._deny("action_not_defined")

        if not allowed:
            return self._deny("action_denied")

        return {"allowed": True, "reason": None}

    # -------------------------------------------------------------

    def _deny(self, reason: str) -> dict:
        return {"allowed": False, "reason": reason}

"""
sandbox_permissions.py
----------------------
Permission matrix for Sandbox Enforcement v3.

Responsibilities:
- Define allowed actions for each runtime module
- Provide deterministic permission lookup
- Prevent unauthorized operations
- No dynamic imports, no reflection, no eval/exec

This module is part of SIRIUS Mobile Runtime 3.3.0.
Prepared for Self‑Repair Layer 4.4.
"""


class SandboxPermissions:
    """
    Deterministic permission controller.
    Defines which module may perform which action.
    """

    # -------------------------------------------------------------
    # STATIC PERMISSION MATRIX (DETERMINISTIC)
    # -------------------------------------------------------------
    PERMISSIONS = {
        "vision_engine": {
            "read_image": True,
            "write_file": False,
            "network_access": False,
            "modify_packs": False,
        },

        "event_engine": {
            "dispatch_event": True,
            "write_file": False,
            "network_access": False,
        },

        "schoolwork_reasoning": {
            "compute": True,
            "write_file": False,
            "network_access": False,
        },

        "pack_manager": {
            "read_pack": True,
            "write_pack": False,
            "network_access": False,
        },

        "restricted_mode": {
            "enforce_policy": True,
            "write_file": False,
            "network_access": False,
        },

        "quarantine_pipeline": {
            "store_event": True,
            "write_file": True,
            "network_access": False,
        },
    }

    # -------------------------------------------------------------

    def is_allowed(self, module_name: str, action: str) -> bool:
        """
        Deterministic permission lookup.
        Returns True if module_name is allowed to perform action.
        """

        module = self.PERMISSIONS.get(module_name)
        if module is None:
            return False  # unknown module → blocked

        return module.get(action, False)

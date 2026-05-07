# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Permissions
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Minimal permission system for the mobile runtime.
# Provides a stable API for the security module.
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

class MobilePermissions:
    """
    Minimal permission system placeholder for GAMA 3.0.0-pre.
    Can be extended later with real policies.
    """

    def __init__(self, profile: str = "OWNER"):
        # Security profile:
        #   OWNER   – full access
        #   FAMILY  – limited access (future)
        #   STRANGER – restricted (future)
        self.profile = profile

    def is_allowed(self, permission: str) -> bool:
        """
        Determines whether a given permission is allowed.
        For now, OWNER always allows everything.
        Other profiles can be extended later.
        """

        if self.profile == "OWNER":
            return True

        # Future: implement real permission rules
        return True

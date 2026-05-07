# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Permissions
# Version: 3.0.0-pre
# ============================================================

class MobilePermissions:
    """
    Minimal permission system placeholder for GAMA 3.0.0-pre.
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, profile: str = "OWNER"):
        self.profile = profile  # OWNER / FAMILY / STRANGER

    # ------------------------------------------------------------
    # Profile Management
    # ------------------------------------------------------------

    def set_profile(self, profile: str):
        """Set active security profile."""
        self.profile = profile

    def get_profile(self) -> str:
        """Return current security profile."""
        return self.profile

    # ------------------------------------------------------------
    # Permission Evaluation
    # ------------------------------------------------------------

    def is_allowed(self, permission: str) -> bool:
        """
        Determines whether a given permission is allowed.
        """

        # OWNER → full access
        if self.profile == "OWNER":
            return True

        # FAMILY → medium access (allow for now)
        if self.profile == "FAMILY":
            return True

        # STRANGER → deny by default
        if self.profile == "STRANGER":
            return False

        # Unknown profile → safest option
        return False

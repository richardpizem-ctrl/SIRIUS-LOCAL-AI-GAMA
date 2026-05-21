# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Permissions
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for GAMA Runtime 3.1:
# - OWNER / FAMILY / STRANGER profiles
# - Restricted Mode v3 compatibility
# - Stable permission evaluation API
# - Clean integration with SecurityModule 3.1
# ============================================================

class MobilePermissions:
    """
    Lightweight permission system for GAMA 3.1.
    Provides:
    - profile management
    - restricted mode compatibility
    - unified permission evaluation
    """

    MODULE_VERSION = "3.1.0"

    def __init__(self, profile: str = "OWNER", restricted: bool = False):
        self.profile = profile.upper()       # OWNER / FAMILY / STRANGER
        self.restricted_mode = restricted    # Hard override

    # ------------------------------------------------------------
    # Profile Management
    # ------------------------------------------------------------

    def set_profile(self, profile: str):
        """Set active security profile."""
        self.profile = profile.upper()

    def get_profile(self) -> str:
        """Return current security profile."""
        return self.profile

    def set_restricted(self, state: bool):
        """Enable or disable restricted mode."""
        self.restricted_mode = bool(state)

    def is_restricted(self) -> bool:
        return self.restricted_mode

    # ------------------------------------------------------------
    # Permission Evaluation (3.1)
    # ------------------------------------------------------------

    def is_allowed(self, permission: str) -> bool:
        """
        Determines whether a given permission is allowed.
        Restricted mode overrides profiles.
        """

        # Restricted Mode v3 → deny everything except safe ops
        if self.restricted_mode:
            return False

        # OWNER → full access
        if self.profile == "OWNER":
            return True

        # FAMILY → medium access (allowed for now)
        if self.profile == "FAMILY":
            return True

        # STRANGER → deny by default
        if self.profile == "STRANGER":
            return False

        # Unknown profile → safest option
        return False

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
        return {
            "module": "permissions",
            "version": self.MODULE_VERSION,
            "profile": self.profile,
            "restricted_mode": self.restricted_mode,
        }

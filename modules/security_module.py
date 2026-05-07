# ============================================================
# SIRIUS LOCAL AI GAMA - Security Module
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Unified security evaluation module for mobile runtime.
# Provides:
#   - text safety evaluation
#   - restricted mode enforcement
#   - OWNER / FAMILY / STRANGER profiles
#   - event-level filtering
#   - runtime integration hooks
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

from typing import Dict, Any
from .base_module import BaseModule


class SecurityModule(BaseModule):
    """
    Security evaluation module for GAMA mobile runtime.

    Responsibilities:
    - evaluate text and event safety
    - enforce restricted mode
    - apply user profile rules (OWNER / FAMILY / STRANGER)
    - integrate with runtime security family
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self):
        super().__init__("security")

        # Forbidden keywords (expandable in 3.x)
        self.forbidden_keywords = [
            "hack",
            "bypass",
            "exploit",
            "cheat",
            "ddos",
            "malware",
            "keylogger",
        ]

        # Security Family mode (injected by runtime)
        self.security_profile = "OWNER"  # OWNER / FAMILY / STRANGER
        self.restricted_mode = False

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_load(self):
        """Load security configuration from runtime if available."""
        if self.runtime:
            if hasattr(self.runtime, "get_security_profile"):
                self.security_profile = self.runtime.get_security_profile()

            if hasattr(self.runtime, "is_restricted_mode"):
                self.restricted_mode = self.runtime.is_restricted_mode()

    def on_unload(self):
        """Reset security state."""
        self.security_profile = "OWNER"
        self.restricted_mode = False

    # ------------------------------------------------------------
    # Main Evaluation
    # ------------------------------------------------------------

    def evaluate(self, event: Dict[str, Any]) -> str:
        """
        Evaluate event safety.

        Returns:
            "allow"
            "deny"
            "restricted"
        """

        text = event.get("text", "").lower()

        # 1) Restricted Mode overrides everything
        if self.restricted_mode:
            if self._contains_forbidden(text):
                return "deny"
            return "restricted"

        # 2) STRANGER profile = strictest
        if self.security_profile == "STRANGER":
            if self._contains_forbidden(text):
                return "deny"
            if len(text) > 200:
                return "restricted"
            return "allow"

        # 3) FAMILY profile = medium strict
        if self.security_profile == "FAMILY":
            if self._contains_forbidden(text):
                return "deny"
            return "allow"

        # 4) OWNER profile = full access except forbidden
        if self._contains_forbidden(text):
            return "deny"

        return "allow"

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _contains_forbidden(self, text: str) -> bool:
        """Check if text contains forbidden keywords."""
        return any(word in text for word in self.forbidden_keywords)

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
        """Extend base metadata with security info."""
        base = super().get_info()
        base.update({
            "security_profile": self.security_profile,
            "restricted_mode": self.restricted_mode,
            "forbidden_keywords": self.forbidden_keywords,
        })
        return base

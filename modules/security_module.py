# ============================================================
# SIRIUS LOCAL AI GAMA - Security Module
# Version: 3.0.0-pre
# ============================================================

from typing import Dict, Any
from .base_module import BaseModule


class SecurityModule(BaseModule):

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self):
        super().__init__("security")

        self.forbidden_keywords = [
            "hack",
            "bypass",
            "exploit",
            "cheat",
            "ddos",
            "malware",
            "keylogger",
        ]

        self.security_profile = "OWNER"
        self.restricted_mode = False

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_load(self):
        if self.runtime:
            if hasattr(self.runtime, "get_security_profile"):
                self.security_profile = self.runtime.get_security_profile()

            if hasattr(self.runtime, "is_restricted_mode"):
                self.restricted_mode = self.runtime.is_restricted_mode()

    def on_unload(self):
        self.security_profile = "OWNER"
        self.restricted_mode = False

    # ------------------------------------------------------------
    # Event Hook (3.x)
    # ------------------------------------------------------------

    def on_event(self, event):
        """Passive event hook (optional)."""
        pass

    # ------------------------------------------------------------
    # Main Evaluation
    # ------------------------------------------------------------

    def evaluate(self, event: Any) -> str:
        """
        Evaluate event safety.
        Supports both dict and MobileEvent.
        """

        # MobileEvent support
        if hasattr(event, "payload"):
            text = event.payload.get("text", "").lower()
        else:
            text = event.get("text", "").lower()

        # Restricted mode overrides everything
        if self.restricted_mode:
            if self._contains_forbidden(text):
                return "deny"
            return "restricted"

        # STRANGER = strictest
        if self.security_profile == "STRANGER":
            if self._contains_forbidden(text):
                return "deny"
            return "allow"

        # FAMILY = medium strict
        if self.security_profile == "FAMILY":
            if self._contains_forbidden(text):
                return "deny"
            return "allow"

        # OWNER = full access except forbidden
        if self._contains_forbidden(text):
            return "deny"

        return "allow"

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _contains_forbidden(self, text: str) -> bool:
        return any(word in text for word in self.forbidden_keywords)

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
        base = super().get_info()
        base.update({
            "security_profile": self.security_profile,
            "restricted_mode": self.restricted_mode,
            "forbidden_keywords": self.forbidden_keywords,
        })
        return base

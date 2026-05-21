# ============================================================
# SIRIUS LOCAL AI GAMA - Security Module
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Upgraded for GAMA Runtime 3.1:
# - MobileEvent v3.1 support (intent, confidence, metadata v3)
# - Multi-source text extraction (OCR, vision, hybrid)
# - Security Profiles v3 (OWNER / FAMILY / STRANGER)
# - Restricted Mode v3
# - Diagnostics v3 hooks
# - Unified evaluation pipeline
# ============================================================

from typing import Any, Dict
from .base_module import BaseModule


class SecurityModule(BaseModule):

    MODULE_VERSION = "3.1.0"

    def __init__(self):
        super().__init__("security")

        # Forbidden keywords (v3 extended)
        self.forbidden_keywords = [
            "hack", "bypass", "exploit", "cheat",
            "ddos", "malware", "keylogger",
            "backdoor", "inject", "payload"
        ]

        # Runtime‑controlled state
        self.security_profile = "OWNER"      # OWNER / FAMILY / STRANGER
        self.restricted_mode = False         # Hard override

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_load(self):
        """Load security profile + restricted mode from runtime."""
        if not self.runtime:
            return

        if hasattr(self.runtime, "get_security_profile"):
            self.security_profile = self.runtime.get_security_profile()

        if hasattr(self.runtime, "is_restricted_mode"):
            self.restricted_mode = self.runtime.is_restricted_mode()

    def on_unload(self):
        """Reset to defaults."""
        self.security_profile = "OWNER"
        self.restricted_mode = False

    # ------------------------------------------------------------
    # Event Hook (3.1)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Passive hook for diagnostics v3.
        Does not block anything — evaluation happens in evaluate().
        """
        if hasattr(self.runtime, "diagnostics"):
            self.runtime.diagnostics.record_security_event(event)

    # ------------------------------------------------------------
    # Main Evaluation (3.1)
    # ------------------------------------------------------------

    def evaluate(self, event: Any) -> str:
        """
        Evaluate event safety.
        Supports:
        - MobileEvent 3.1
        - dict-based events (legacy)
        """

        text = self._extract_text(event)

        # 1) Restricted Mode = hard override
        if self.restricted_mode:
            if self._contains_forbidden(text):
                return "deny"
            return "restricted"

        # 2) Profile-based evaluation
        profile = self.security_profile.upper()

        if profile == "STRANGER":
            return self._eval_stranger(text)

        if profile == "FAMILY":
            return self._eval_family(text)

        # OWNER (default)
        return self._eval_owner(text)

    # ------------------------------------------------------------
    # Profile Evaluators
    # ------------------------------------------------------------

    def _eval_stranger(self, text: str) -> str:
        """Strictest profile."""
        if self._contains_forbidden(text):
            return "deny"
        return "allow"

    def _eval_family(self, text: str) -> str:
        """Medium strictness."""
        if self._contains_forbidden(text):
            return "deny"
        return "allow"

    def _eval_owner(self, text: str) -> str:
        """Full access except forbidden."""
        if self._contains_forbidden(text):
            return "deny"
        return "allow"

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _extract_text(self, event: Any) -> str:
        """
        Unified text extraction for:
        - MobileEvent 3.1 (raw_input, normalized_input, metadata)
        - OCR / Vision tags
        - Legacy dict events
        """

        # MobileEvent 3.1
        if hasattr(event, "payload"):
            payload = event.payload

            # Priority: normalized_input → raw_input → text
            if getattr(event, "normalized_input", None):
                return str(event.normalized_input).lower()

            if getattr(event, "raw_input", None):
                return str(event.raw_input).lower()

            if "text" in payload:
                return str(payload.get("text", "")).lower()

            # OCR / Vision tags
            if "ocr_text" in payload:
                return str(payload.get("ocr_text", "")).lower()

            if "vision_text" in payload:
                return str(payload.get("vision_text", "")).lower()

            return ""

        # Legacy dict event
        if isinstance(event, dict):
            return str(event.get("text", "")).lower()

        return ""

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

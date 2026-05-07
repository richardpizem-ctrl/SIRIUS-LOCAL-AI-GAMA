# ============================================================
# SIRIUS LOCAL AI GAMA - Knowledge Module
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Unified knowledge module for mobile runtime.
# Provides:
#   - access to offline knowledge packs
#   - text query interface
#   - fallback responses
#   - runtime integration
#   - versioned metadata
#
# This module is fully prepared for GAMA 3.x architecture.
# ============================================================

from typing import Optional, Dict, Any
from .base_module import BaseModule


class KnowledgeModule(BaseModule):
    """
    Offline Knowledge Pack Module (GAMA 3-ready)

    Responsibilities:
    - load/unload knowledge packs
    - provide unified query() interface
    - fallback answers when no pack matches
    - integrate with runtime_mobile
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self):
        super().__init__("knowledge")
        self.packs = {}  # dict: pack_name -> pack_instance

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_load(self):
        """Load all available knowledge packs."""
        # Runtime injects pack loader if available
        if self.runtime and hasattr(self.runtime, "load_knowledge_packs"):
            self.packs = self.runtime.load_knowledge_packs()
        else:
            self.packs = {}

    def on_unload(self):
        """Unload all packs."""
        self.packs.clear()

    # ------------------------------------------------------------
    # Query Interface
    # ------------------------------------------------------------

    def query(self, text: str) -> Dict[str, Any]:
        """
        Main query interface for offline knowledge packs.

        Steps:
        1. Normalize text
        2. Route to appropriate pack (if any)
        3. Return structured response
        """
        if not text or not isinstance(text, str):
            return self._error("Invalid input")

        normalized = text.strip().lower()

        # Try each pack
        for pack_name, pack in self.packs.items():
            if hasattr(pack, "can_answer") and pack.can_answer(normalized):
                try:
                    answer = pack.query(normalized)
                    return {
                        "status": "ok",
                        "type": "knowledge_result",
                        "pack": pack_name,
                        "answer": answer,
                    }
                except Exception as e:
                    return self._error(f"Pack '{pack_name}' failed: {e}")

        # No pack matched → fallback
        return self._fallback(normalized)

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _fallback(self, text: str) -> Dict[str, Any]:
        """Fallback response when no pack can answer."""
        return {
            "status": "fallback",
            "type": "knowledge_result",
            "answer": f"No knowledge pack found for: '{text}'",
        }

    def _error(self, message: str) -> Dict[str, Any]:
        """Error response."""
        return {
            "status": "error",
            "type": "knowledge_result",
            "error": message,
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
        """Extend base metadata with pack info."""
        base = super().get_info()
        base.update({
            "packs_loaded": list(self.packs.keys()),
        })
        return base

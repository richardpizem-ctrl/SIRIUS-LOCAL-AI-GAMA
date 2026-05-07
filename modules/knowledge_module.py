# ============================================================
# SIRIUS LOCAL AI GAMA - Knowledge Module
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
# ============================================================

from typing import Dict, Any
from .base_module import BaseModule


class KnowledgeModule(BaseModule):
    """
    Offline Knowledge Pack Module (GAMA 3-ready)
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self):
        super().__init__("knowledge")
        self.packs = {}

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_load(self):
        if self.runtime and hasattr(self.runtime, "load_knowledge_packs"):
            self.packs = self.runtime.load_knowledge_packs()
        else:
            self.packs = {}

    def on_unload(self):
        self.packs.clear()

    # ------------------------------------------------------------
    # Event Hook (3.x)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Passive event hook (optional for 3.x).
        """
        pass

    # ------------------------------------------------------------
    # Query Interface
    # ------------------------------------------------------------

    def query(self, text: str) -> Dict[str, Any]:
        if not text or not isinstance(text, str):
            return self._error("Invalid input")

        normalized = text.strip().lower()

        for pack_name, pack in self.packs.items():
            if hasattr(pack, "can_answer") and pack.can_answer(normalized):

                if not hasattr(pack, "query"):
                    return self._error(f"Pack '{pack_name}' missing query()")

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

        return self._fallback(normalized)

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _fallback(self, text: str) -> Dict[str, Any]:
        return {
            "status": "fallback",
            "type": "knowledge_result",
            "answer": f"No knowledge pack found for: '{text}'",
        }

    def _error(self, message: str) -> Dict[str, Any]:
        return {
            "status": "error",
            "type": "knowledge_result",
            "error": message,
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
        base = super().get_info()
        base.update({
            "packs_loaded": list(self.packs.keys()),
        })
        return base

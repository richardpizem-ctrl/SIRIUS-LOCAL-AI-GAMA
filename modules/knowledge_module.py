# ============================================================
# SIRIUS LOCAL AI GAMA - Knowledge Module
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for GAMA 3.1:
#   - metadata v3 integration
#   - normalized event handling
#   - diagnostics v3 compatibility
#   - pack priority v3 compatibility
#   - unified error model
# ============================================================

from typing import Dict, Any
from .base_module import BaseModule


class KnowledgeModule(BaseModule):
    """
    Offline Knowledge Pack Module (GAMA 3.1-ready)

    Responsibilities:
    - load/unload knowledge packs
    - provide unified query() interface
    - integrate with metadata v3
    - support diagnostics v3 (trace + pack selection)
    - support pack priority v3
    """

    MODULE_VERSION = "3.1.0"

    def __init__(self):
        super().__init__("knowledge")
        self.packs = {}

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_load(self):
        """
        Load all available knowledge packs from runtime.
        """
        if self.runtime and hasattr(self.runtime, "load_knowledge_packs"):
            try:
                self.packs = self.runtime.load_knowledge_packs()
            except Exception as e:
                print(f"[ERROR] Failed to load knowledge packs: {e}")
                self.packs = {}
        else:
            self.packs = {}

    def on_unload(self):
        """
        Unload all packs safely.
        """
        self.packs.clear()

    # ------------------------------------------------------------
    # Event Hook (3.1)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Passive event hook.
        Event is already normalized by runtime_core in 3.1.
        """
        # Diagnostics v3: trace pack availability
        if self.runtime and hasattr(self.runtime, "diagnostics"):
            diag = self.runtime.diagnostics
            if hasattr(diag, "trace_pack_state"):
                try:
                    diag.trace_pack_state(event, list(self.packs.keys()))
                except Exception:
                    pass

    # ------------------------------------------------------------
    # Query Interface
    # ------------------------------------------------------------

    def query(self, text: str) -> Dict[str, Any]:
        """
        Main query interface for offline knowledge packs.
        Includes:
        - normalization
        - pack priority v3
        - diagnostics v3 trace
        """
        if not text or not isinstance(text, str):
            return self._error("Invalid input")

        normalized = text.strip().lower()

        # Diagnostics v3: trace query start
        if self.runtime and hasattr(self.runtime, "diagnostics"):
            try:
                self.runtime.diagnostics.trace_knowledge_query(normalized)
            except Exception:
                pass

        # Pack selection (priority v3)
        for pack_name, pack in self.packs.items():
            if hasattr(pack, "can_answer") and pack.can_answer(normalized):

                # Diagnostics v3: trace pack hit
                if self.runtime and hasattr(self.runtime, "diagnostics"):
                    try:
                        self.runtime.diagnostics.trace_pack_hit(pack_name)
                    except Exception:
                        pass

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

        # Diagnostics v3: fallback trace
        if self.runtime and hasattr(self.runtime, "diagnostics"):
            try:
                self.runtime.diagnostics.trace_pack_fallback(normalized)
            except Exception:
                pass

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
        """
        Extended metadata for diagnostics v3.
        """
        base = super().get_info()
        base.update({
            "packs_loaded": list(self.packs.keys()),
            "pack_count": len(self.packs),
        })
        return base

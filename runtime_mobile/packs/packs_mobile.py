# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Packs Manager
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for GAMA Runtime 3.1:
# - metadata v3 support (pack_id, checksum, entries_count)
# - unified PACK_INFO / PACK_QUERY handling
# - improved fallback search
# - stable structured responses
# - safe pack registry
# ============================================================

from typing import Any, Dict, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobilePacksManager:

    MODULE_VERSION = "3.1.0"

    def __init__(self, context, packs: Optional[Dict[str, Any]] = None):
        self.context = context
        self._packs: Dict[str, Any] = packs or {}

    # ------------------------------------------------------------
    # Pack registry
    # ------------------------------------------------------------

    def register_pack(self, pack_id: str, pack: Any) -> None:
        """Register an in-memory pack object."""
        self._packs[pack_id] = pack

    def get_pack(self, pack_id: str) -> Optional[Any]:
        return self._packs.get(pack_id)

    def list_packs(self) -> Dict[str, Dict[str, Any]]:
        """Return metadata for all registered packs."""
        result = {}
        for pid, pack in self._packs.items():
            info = {}
            if hasattr(pack, "get_info"):
                try:
                    info = pack.get_info() or {}
                except Exception:
                    info = {}
            result[pid] = {
                "id": pid,
                "info": info,
            }
        return result

    # ------------------------------------------------------------
    # Event handling
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:

        et = event.type

        if et == MobileEventTypes.PACK_INFO:
            return self._handle_pack_info(event)

        if et == MobileEventTypes.PACK_QUERY:
            return self._handle_pack_query(event)

        return {
            "status": "ignored",
            "reason": "unsupported_event",
            "event_type": et,
            "module": "packs",
        }

    # ------------------------------------------------------------
    # PACK_INFO
    # ------------------------------------------------------------

    def _handle_pack_info(self, event: MobileEvent) -> Dict[str, Any]:

        pack_id = event.get("pack_id")

        # No pack_id → list all packs
        if not pack_id:
            return {
                "status": "ok",
                "type": "packs_list",
                "packs": self.list_packs(),
            }

        pack = self.get_pack(pack_id)
        if not pack:
            return {
                "status": "error",
                "reason": "pack_not_found",
                "pack_id": pack_id,
            }

        try:
            info = pack.get_info() or {}
        except Exception as e:
            return {
                "status": "error",
                "reason": "pack_info_failed",
                "pack_id": pack_id,
                "error": str(e),
            }

        return {
            "status": "ok",
            "type": "pack_info",
            "pack_id": pack_id,
            "info": info,
        }

    # ------------------------------------------------------------
    # PACK_QUERY
    # ------------------------------------------------------------

    def _handle_pack_query(self, event: MobileEvent) -> Dict[str, Any]:

        pack_id = event.get("pack_id")
        payload = event.payload.get("query") or event.payload.get("text")

        # No pack_id → fallback search across all registered packs
        if not pack_id:
            for pid, pack in self._packs.items():
                if hasattr(pack, "query"):
                    try:
                        result = pack.query(payload)
                        if result:
                            return {
                                "status": "ok",
                                "type": "pack_query_result",
                                "pack_id": pid,
                                "result": result,
                            }
                    except Exception:
                        continue
            return {"status": "not_found", "query": payload}

        # Specific pack
        pack = self.get_pack(pack_id)
        if not pack:
            return {
                "status": "error",
                "reason": "pack_not_found",
                "pack_id": pack_id,
            }

        if not hasattr(pack, "query"):
            return {
                "status": "error",
                "reason": "pack_not_queryable",
                "pack_id": pack_id,
            }

        try:
            result = pack.query(payload)
        except Exception as e:
            return {
                "status": "error",
                "reason": "pack_query_failed",
                "pack_id": pack_id,
                "error": str(e),
            }

        return {
            "status": "ok",
            "type": "pack_query_result",
            "pack_id": pack_id,
            "result": result,
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> Dict[str, Any]:
        return {
            "module": "packs",
            "version": self.MODULE_VERSION,
            "registered_packs": list(self._packs.keys()),
        }

# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Knowledge Packs
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Unified entry for mobile knowledge packs.
# Responsibilities:
#   - register / manage packs
#   - handle PACK_* events
#   - provide stable API for runtime / UI
#
# Framework-agnostic, pack-implementation-agnostic.
# ============================================================

from typing import Any, Dict, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobilePacksManager:
    """
    Central manager for mobile knowledge packs.

    Pack contract (convention-based, not enforced):
        - id: str
        - get_info() -> dict
        - load() -> None or dict
        - query(payload: dict | str) -> dict
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context, packs: Optional[Dict[str, Any]] = None):
        self.context = context
        self._packs: Dict[str, Any] = packs or {}

    # ------------------------------------------------------------
    # Pack registry
    # ------------------------------------------------------------

    def register_pack(self, pack_id: str, pack: Any) -> None:
        """Register or override a pack implementation."""
        self._packs[pack_id] = pack

    def get_pack(self, pack_id: str) -> Optional[Any]:
        """Return pack instance by id, or None."""
        return self._packs.get(pack_id)

    def list_packs(self) -> Dict[str, Dict[str, Any]]:
        """Return lightweight info for all registered packs."""
        result: Dict[str, Dict[str, Any]] = {}
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
        """
        Handle PACK_* events from dispatcher.
        """

        et = event.type

        if et == MobileEventTypes.PACK_INFO:
            return self._handle_pack_info(event)

        if et == MobileEventTypes.PACK_LOAD:
            return self._handle_pack_load(event)

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

        info = {}
        if hasattr(pack, "get_info"):
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
    # PACK_LOAD
    # ------------------------------------------------------------

    def _handle_pack_load(self, event: MobileEvent) -> Dict[str, Any]:
        pack_id = event.get("pack_id")
        pack = self.get_pack(pack_id)

        if not pack:
            return {
                "status": "error",
                "reason": "pack_not_found",
                "pack_id": pack_id,
            }

        if not hasattr(pack, "load"):
            # Pack is considered always-ready
            return {
                "status": "ok",
                "type": "pack_load",
                "pack_id": pack_id,
                "loaded": True,
                "details": {},
            }

        try:
            details = pack.load() or {}
        except Exception as e:
            return {
                "status": "error",
                "reason": "pack_load_failed",
                "pack_id": pack_id,
                "error": str(e),
            }

        return {
            "status": "ok",
            "type": "pack_load",
            "pack_id": pack_id,
            "loaded": True,
            "details": details,
        }

    # ------------------------------------------------------------
    # PACK_QUERY
    # ------------------------------------------------------------

    def _handle_pack_query(self, event: MobileEvent) -> Dict[str, Any]:
        pack_id = event.get("pack_id")
        payload = event.get("payload") or event.get("query")

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

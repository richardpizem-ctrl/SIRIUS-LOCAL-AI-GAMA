# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Knowledge Packs Entry
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.core.mobile_event import MobileEvent


class MobileKnowledgePacks:
    """
    Entry point for the mobile knowledge packs system.
    Handles loading, validation and retrieval of offline knowledge packs.
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context
        self.loaded_packs = {}

    # ------------------------------------------------------------
    # Pack Loading
    # ------------------------------------------------------------

    def load_pack(self, pack_name: str):
        if not hasattr(self.context, "pack_manager"):
            return {"status": "error", "reason": "pack_manager_missing"}

        pack = self.context.pack_manager.load(pack_name)

        if pack is None:
            return {"status": "error", "reason": "pack_not_found", "pack": pack_name}

        # Basic validation
        if "entries" not in pack or not isinstance(pack["entries"], dict):
            return {"status": "error", "reason": "invalid_pack_format"}

        self.loaded_packs[pack_name] = pack

        return {
            "status": "ok",
            "pack": pack_name,
            "entries": len(pack["entries"]),
            "version": pack.get("version", "unknown")
        }

    # ------------------------------------------------------------
    # Event Handler (required by runtime)
    # ------------------------------------------------------------

    def on_event(self, event: MobileEvent):
        etype = event.type

        if etype == MobileEventTypes.PACK_LOOKUP:
            return self.get(event.pack, event.key)

        if etype == MobileEventTypes.PACK_INFO:
            return self.info(event.pack)

        return {
            "status": "ignored",
            "reason": "unknown_event",
            "event_type": etype
        }

    # ------------------------------------------------------------
    # Pack Query
    # ------------------------------------------------------------

    def get(self, pack_name: str, key: str):
        if pack_name not in self.loaded_packs:
            load_result = self.load_pack(pack_name)
            if load_result.get("status") != "ok":
                return load_result

        pack = self.loaded_packs[pack_name]
        entries = pack["entries"]

        return {
            "status": "ok",
            "pack": pack_name,
            "key": key,
            "value": entries.get(key),
            "exists": key in entries
        }

    # ------------------------------------------------------------
    # Pack Info
    # ------------------------------------------------------------

    def info(self, pack_name: str):
        if pack_name not in self.loaded_packs:
            load_result = self.load_pack(pack_name)
            if load_result.get("status") != "ok":
                return load_result

        pack = self.loaded_packs[pack_name]

        return {
            "status": "ok",
            "pack": pack_name,
            "version": pack.get("version", "unknown"),
            "entries": list(pack["entries"].keys())
        }

    # ------------------------------------------------------------
    # List Loaded Packs
    # ------------------------------------------------------------

    def list_loaded(self):
        return {
            "status": "ok",
            "loaded_packs": list(self.loaded_packs.keys())
        }

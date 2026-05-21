# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Knowledge Packs Entry
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.core.mobile_event import MobileEvent


class MobileKnowledgePacks:
    """
    Entry point for the mobile knowledge packs system.
    Handles loading, validation and retrieval of offline knowledge packs.
    Fully compatible with PACK_LOOKUP / PACK_INFO / PACK_QUERY / PACK_SUGGEST.
    """

    MODULE_VERSION = "3.1.0"

    def __init__(self, context):
        self.context = context
        self.loaded_packs = {}

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _ensure_manager(self):
        if not hasattr(self.context, "pack_manager"):
            return None, {"status": "error", "reason": "pack_manager_missing"}
        return self.context.pack_manager, None

    def _ensure_loaded(self, pack_name: str):
        """
        Ensure pack is loaded; auto-load if needed.
        """
        if pack_name in self.loaded_packs:
            return self.loaded_packs[pack_name], None

        load_result = self.load_pack(pack_name)
        if load_result.get("status") != "ok":
            return None, load_result

        return self.loaded_packs[pack_name], None

    # ------------------------------------------------------------
    # Pack Loading
    # ------------------------------------------------------------

    def load_pack(self, pack_name: str):
        manager, err = self._ensure_manager()
        if err:
            return err

        pack = manager.load(pack_name)
        if pack is None:
            return {"status": "error", "reason": "pack_not_found", "pack": pack_name}

        # Validation v3
        if "entries" not in pack or not isinstance(pack["entries"], dict):
            return {"status": "error", "reason": "invalid_pack_format"}

        # Optional metadata
        if "meta" in pack and not isinstance(pack["meta"], dict):
            return {"status": "error", "reason": "invalid_pack_metadata"}

        self.loaded_packs[pack_name] = pack

        return {
            "status": "ok",
            "pack": pack_name,
            "entries": len(pack["entries"]),
            "version": pack.get("version", "unknown"),
            "has_meta": "meta" in pack
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

        if etype == MobileEventTypes.PACK_QUERY:
            return self.query(event.pack, event.key)

        if etype == MobileEventTypes.PACK_SUGGEST:
            return self.suggest(event.pack, event.prefix)

        return {
            "status": "ignored",
            "reason": "unknown_event",
            "event_type": etype
        }

    # ------------------------------------------------------------
    # Pack Query (direct lookup)
    # ------------------------------------------------------------

    def get(self, pack_name: str, key: str):
        pack, err = self._ensure_loaded(pack_name)
        if err:
            return err

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
        pack, err = self._ensure_loaded(pack_name)
        if err:
            return err

        return {
            "status": "ok",
            "pack": pack_name,
            "version": pack.get("version", "unknown"),
            "entries": list(pack["entries"].keys()),
            "meta": pack.get("meta", None)
        }

    # ------------------------------------------------------------
    # Pack Query (search by substring)
    # ------------------------------------------------------------

    def query(self, pack_name: str, key: str):
        pack, err = self._ensure_loaded(pack_name)
        if err:
            return err

        entries = pack["entries"]
        matches = {
            k: v for k, v in entries.items()
            if key.lower() in k.lower()
        }

        return {
            "status": "ok",
            "pack": pack_name,
            "query": key,
            "matches": matches,
            "count": len(matches)
        }

    # ------------------------------------------------------------
    # Pack Suggest (prefix search)
    # ------------------------------------------------------------

    def suggest(self, pack_name: str, prefix: str):
        pack, err = self._ensure_loaded(pack_name)
        if err:
            return err

        entries = pack["entries"]
        suggestions = [
            k for k in entries.keys()
            if k.lower().startswith(prefix.lower())
        ]

        return {
            "status": "ok",
            "pack": pack_name,
            "prefix": prefix,
            "suggestions": suggestions,
            "count": len(suggestions)
        }

    # ------------------------------------------------------------
    # List Loaded Packs
    # ------------------------------------------------------------

    def list_loaded(self):
        return {
            "status": "ok",
            "loaded_packs": list(self.loaded_packs.keys())
        }

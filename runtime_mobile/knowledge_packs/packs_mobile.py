# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Knowledge Packs Entry
# Version: 3.0.0-pre
# ============================================================

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileKnowledgePacks:

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

        self.loaded_packs[pack_name] = pack

        return {
            "status": "ok",
            "pack": pack_name,
            "entries": len(pack.get("entries", {})),
            "version": pack.get("version", "unknown"),
            "priority": pack.get("priority", 0),
            "language": pack.get("language", "en"),
            "tags": pack.get("tags", []),
        }

    # ------------------------------------------------------------
    # Event Handler
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent):

        et = event.type

        if et == MobileEventTypes.PACK_LOOKUP:
            return self._handle_lookup(event)

        if et == MobileEventTypes.PACK_INFO:
            return self._handle_info(event)

        if et == MobileEventTypes.PACK_QUERY:
            return self._handle_query(event)

        return {"status": "ignored", "reason": "unknown_event", "event_type": et}

    # ------------------------------------------------------------
    # PACK LOOKUP
    # ------------------------------------------------------------

    def _handle_lookup(self, event: MobileEvent):

        pack_name = event.get("pack", "default")
        key = event.get("key", "query")

        # auto-load
        if pack_name not in self.loaded_packs:
            load_result = self.load_pack(pack_name)
            if load_result.get("status") != "ok":
                return load_result

        pack = self.loaded_packs[pack_name]
        entries = pack.get("entries", {})

        if key in entries:
            return {
                "status": "ok",
                "pack": pack_name,
                "key": key,
                "value": entries[key],
                "exists": True,
            }

        # fallback search
        fallback = self.context.pack_manager.search_in_packs(key)
        if fallback is not None:
            return {
                "status": "ok",
                "pack": "fallback",
                "key": key,
                "value": fallback,
                "exists": True,
            }

        return {"status": "not_found", "pack": pack_name, "key": key, "exists": False}

    # ------------------------------------------------------------
    # PACK INFO
    # ------------------------------------------------------------

    def _handle_info(self, event: MobileEvent):

        pack_name = event.get("pack", "default")

        if pack_name not in self.loaded_packs:
            load_result = self.load_pack(pack_name)
            if load_result.get("status") != "ok":
                return load_result

        pack = self.loaded_packs[pack_name]

        return {
            "status": "ok",
            "pack": pack_name,
            "version": pack.get("version", "unknown"),
            "priority": pack.get("priority", 0),
            "language": pack.get("language", "en"),
            "tags": pack.get("tags", []),
            "entries": list(pack.get("entries", {}).keys()),
        }

    # ------------------------------------------------------------
    # PACK QUERY (text-based)
    # ------------------------------------------------------------

    def _handle_query(self, event: MobileEvent):

        text = event.get("text", "").strip().lower()

        value = self.context.pack_manager.search_in_packs(text)

        if value is None:
            return {"status": "not_found", "query": text}

        return {"status": "ok", "query": text, "value": value}

    # ------------------------------------------------------------
    # List Loaded Packs
    # ------------------------------------------------------------

    def list_loaded(self):
        return {"status": "ok", "loaded_packs": list(self.loaded_packs.keys())}

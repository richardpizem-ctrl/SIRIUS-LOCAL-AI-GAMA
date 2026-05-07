# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Knowledge Packs Entry
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Entry point for the mobile knowledge packs system.
# Responsibilities:
#   - loading JSON knowledge packs
#   - caching
#   - validation
#   - event-based lookup
#   - safe fallback responses
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

from runtime_mobile.core.event_types import MobileEvent, MobileEventTypes


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
        """
        Loads a knowledge pack by name.
        """

        if not hasattr(self.context, "pack_manager"):
            return {
                "status": "error",
                "reason": "pack_manager_missing"
            }

        pack = self.context.pack_manager.load(pack_name)

        if pack is None:
            return {
                "status": "error",
                "reason": "pack_not_found",
                "pack": pack_name
            }

        # Cache loaded pack
        self.loaded_packs[pack_name] = pack

        return {
            "status": "ok",
            "pack": pack_name,
            "entries": len(pack.get("entries", {})),
            "version": pack.get("version", "unknown")
        }

    # ------------------------------------------------------------
    # Event Handler
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent):
        """
        Main entry point for dispatcher → packs module.
        """

        if event.type == MobileEventTypes.PACK_LOOKUP:
            pack_name = event.get("pack")
            key = event.get("key")
            return self.get(pack_name, key)

        if event.type == MobileEventTypes.PACK_INFO:
            pack_name = event.get("pack")
            return self.info(pack_name)

        return {
            "status": "ignored",
            "reason": "unknown_event",
            "event_type": event.type
        }

    # ------------------------------------------------------------
    # Pack Query
    # ------------------------------------------------------------

    def get(self, pack_name: str, key: str):
        """
        Retrieves a value from a knowledge pack.
        Automatically loads the pack if not already loaded.
        """

        # Auto-load pack if missing
        if pack_name not in self.loaded_packs:
            load_result = self.load_pack(pack_name)

            if load_result.get("status") != "ok":
                return load_result  # return the error

        pack = self.loaded_packs.get(pack_name)
        entries = pack.get("entries", {})

        value = entries.get(key)

        return {
            "status": "ok",
            "pack": pack_name,
            "key": key,
            "value": value,
            "exists": key in entries
        }

    # ------------------------------------------------------------
    # Pack Info
    # ------------------------------------------------------------

    def info(self, pack_name: str):
        """
        Returns metadata about a loaded or available pack.
        """

        # Auto-load if needed
        if pack_name not in self.loaded_packs:
            load_result = self.load_pack(pack_name)
            if load_result.get("status") != "ok":
                return load_result

        pack = self.loaded_packs.get(pack_name)

        return {
            "status": "ok",
            "pack": pack_name,
            "version": pack.get("version", "unknown"),
            "entries": list(pack.get("entries", {}).keys()),
        }

    # ------------------------------------------------------------
    # List Loaded Packs
    # ------------------------------------------------------------

    def list_loaded(self):
        """
        Returns a list of currently loaded knowledge packs.
        """
        return {
            "status": "ok",
            "loaded_packs": list(self.loaded_packs.keys())
        }

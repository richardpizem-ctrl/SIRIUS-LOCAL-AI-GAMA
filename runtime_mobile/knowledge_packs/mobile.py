# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Knowledge Packs
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Handles PACK_LOOKUP and PACK_INFO events.
# Uses MobilePackManager for loading JSON packs.
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes


class MobileKnowledgePacks:
    """
    Entry point for knowledge pack lookups.
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def handle_event(self, event):
        et = event.type

        if et == MobileEventTypes.PACK_LOOKUP:
            return self._handle_lookup(event)

        if et == MobileEventTypes.PACK_INFO:
            return self._handle_info(event)

        return {
            "status": "ignored",
            "reason": "unknown_pack_event",
            "event_type": et
        }

    # ------------------------------------------------------------
    # PACK LOOKUP
    # ------------------------------------------------------------

    def _handle_lookup(self, event):
        pack_name = event.get("pack", "default")
        key = event.get("key", "query")

        pack = self.context.pack_manager.load(pack_name)

        if not pack:
            return {
                "status": "error",
                "reason": "pack_not_found",
                "pack": pack_name
            }

        value = pack.get(key)

        if value is None:
            return {
                "status": "not_found",
                "pack": pack_name,
                "key": key
            }

        return {
            "status": "ok",
            "pack": pack_name,
            "key": key,
            "value": value
        }

    # ------------------------------------------------------------
    # PACK INFO
    # ------------------------------------------------------------

    def _handle_info(self, event):
        pack_name = event.get("pack", "default")
        pack = self.context.pack_manager.load(pack_name)

        if not pack:
            return {
                "status": "error",
                "reason": "pack_not_found",
                "pack": pack_name
            }

        return {
            "status": "ok",
            "pack": pack_name,
            "keys": list(pack.keys()),
            "version": self.MODULE_VERSION
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "module": "knowledge_packs",
            "version": self.MODULE_VERSION
        }

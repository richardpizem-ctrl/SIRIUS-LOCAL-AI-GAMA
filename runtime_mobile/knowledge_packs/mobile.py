# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Knowledge Packs
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for GAMA Runtime 3.1:
# - metadata v3 support (pack_id, checksum, entries_count)
# - improved fallback search
# - unified event handling
# - stable structured responses
# ============================================================

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileKnowledgePacks:

    MODULE_VERSION = "3.1.0"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent):

        et = event.type

        if et == MobileEventTypes.PACK_LOOKUP:
            return self._handle_lookup(event)

        if et == MobileEventTypes.PACK_INFO:
            return self._handle_info(event)

        if et == MobileEventTypes.PACK_QUERY:
            return self._handle_query(event)

        return {
            "status": "ignored",
            "reason": "unknown_pack_event",
            "event_type": et
        }

    # ------------------------------------------------------------
    # PACK LOOKUP
    # ------------------------------------------------------------

    def _handle_lookup(self, event: MobileEvent):

        pack_name = event.get("pack", "default")
        key = event.get("key", "query")

        pack = self.context.pack_manager.load(pack_name)

        if not pack:
            return {
                "status": "error",
                "reason": "pack_not_found",
                "pack": pack_name
            }

        # Direct lookup
        value = pack["entries"].get(key)

        if value is None:
            # Fallback search across all packs
            fallback = self.context.pack_manager.search_in_packs(key)
            if fallback is not None:
                return {
                    "status": "ok",
                    "pack": "fallback",
                    "key": key,
                    "value": fallback
                }

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

    def _handle_info(self, event: MobileEvent):

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
            "pack_id": pack.get("pack_id", pack_name),
            "version": pack.get("version", "unknown"),
            "priority": pack.get("priority", 0),
            "entries_count": pack.get("entries_count", len(pack["entries"])),
            "entries": list(pack["entries"].keys()),
            "checksum": pack.get("checksum", None),
        }

    # ------------------------------------------------------------
    # PACK QUERY (text-based)
    # ------------------------------------------------------------

    def _handle_query(self, event: MobileEvent):

        text = event.get("text", "").strip().lower()

        if not text:
            return {
                "status": "error",
                "reason": "empty_query"
            }

        # Simple heuristic: use text as key
        value = self.context.pack_manager.search_in_packs(text)

        if value is None:
            return {
                "status": "not_found",
                "query": text
            }

        return {
            "status": "ok",
            "query": text,
            "value": value
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "module": "knowledge_packs",
            "version": self.MODULE_VERSION
        }

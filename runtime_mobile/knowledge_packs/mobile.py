# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Knowledge Packs
# Version: 3.0.0-pre
# ============================================================

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileKnowledgePacks:

    MODULE_VERSION = "3.0.0-pre"

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

        value = pack["entries"].get(key)

        if value is None:
            # fallback search across all packs
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
            "entries": list(pack["entries"].keys()),
            "priority": pack.get("priority", 0),
            "version": pack.get("version", "unknown")
        }

    # ------------------------------------------------------------
    # PACK QUERY (text-based)
    # ------------------------------------------------------------

    def _handle_query(self, event: MobileEvent):

        text = event.get("text", "").strip().lower()

        # simple heuristic: use text as key
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

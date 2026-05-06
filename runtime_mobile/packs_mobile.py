from runtime_mobile.core.event_types import MobileEvent, MobileEventTypes

class MobileKnowledgePacks:
    """
    Entry point for the mobile knowledge packs system.
    Handles loading, validation and retrieval of offline knowledge packs.
    """

    def __init__(self, context):
        self.context = context
        self.loaded_packs = {}

    def load_pack(self, pack_name: str):
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

        self.loaded_packs[pack_name] = pack

        return {
            "status": "ok",
            "pack": pack_name
        }

    def handle_event(self, event: MobileEvent):
        if event.type == MobileEventTypes.PACK_LOOKUP:
            pack_name = event.get("pack")
            key = event.get("key")
            return self.get(pack_name, key)

        return {
            "status": "ignored",
            "reason": "unknown_event",
            "event_type": event.type
        }

    def get(self, pack_name: str, key: str):
        pack = self.loaded_packs.get(pack_name)

        if pack is None:
            return {
                "status": "error",
                "reason": "pack_not_loaded",
                "pack": pack_name
            }

        value = pack.get(key)

        return {
            "status": "ok",
            "pack": pack_name,
            "key": key,
            "value": value
        }

    def list_loaded(self):
        return {
            "status": "ok",
            "loaded_packs": list(self.loaded_packs.keys())
        }

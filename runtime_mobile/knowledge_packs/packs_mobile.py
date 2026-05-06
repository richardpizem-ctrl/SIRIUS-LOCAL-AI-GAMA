class MobileKnowledgePacks:
    """
    Entry point for the mobile knowledge packs system.
    Handles loading, validation and retrieval of offline knowledge packs.
    """

    def __init__(self, context):
        self.context = context
        self.loaded_packs = {}

    def load_pack(self, pack_name):
        """
        Loads a knowledge pack by name.
        """
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

    def get(self, pack_name, key):
        """
        Retrieves a value from a loaded knowledge pack.
        """
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
        """
        Returns a list of currently loaded knowledge packs.
        """
        return {
            "status": "ok",
            "loaded_packs": list(self.loaded_packs.keys())
        }

# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Pack Manager
# Version: 3.0.0-pre
# ============================================================

class MobilePackManager:
    """
    Minimal pack manager for GAMA 3.0.0-pre.
    Handles registration and loading of JSON knowledge packs.
    """

    def __init__(self):
        # In future: filesystem / assets / embedded packs
        self._packs = {}

    # ------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------

    def register(self, name: str, pack: dict):
        """
        Register a pack programmatically.
        Used for testing or embedded packs.
        """

        # Basic validation
        if not isinstance(pack, dict):
            return {"status": "error", "reason": "invalid_pack_type"}

        if "entries" not in pack or not isinstance(pack["entries"], dict):
            return {"status": "error", "reason": "invalid_entries"}

        # Store pack
        self._packs[name] = pack

        return {
            "status": "registered",
            "pack": name,
            "entries": len(pack["entries"])
        }

    # ------------------------------------------------------------
    # Loading
    # ------------------------------------------------------------

    def load(self, name: str):
        """
        Load a pack by name.
        For now: returns from in-memory registry only.
        """
        pack = self._packs.get(name)

        if pack is None:
            return None

        return pack

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "registered_packs": list(self._packs.keys()),
            "count": len(self._packs)
        }

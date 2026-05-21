# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Pack Manager
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Minimal pack manager for GAMA 3.1.0.
# Handles registration, validation and loading of JSON knowledge packs.
# Fully compatible with PACK_LOOKUP / PACK_INFO / PACK_QUERY.
# ============================================================

class MobilePackManager:
    """
    Pack manager for GAMA Mobile Runtime 3.1.0.
    Handles registration, validation and loading of JSON knowledge packs.
    """

    VERSION = "3.1.0"

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

        # Optional metadata validation (3.1)
        if "meta" in pack and not isinstance(pack["meta"], dict):
            return {"status": "error", "reason": "invalid_metadata"}

        # Store pack
        self._packs[name] = pack

        return {
            "status": "registered",
            "pack": name,
            "entries": len(pack["entries"]),
            "has_meta": "meta" in pack
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
    # Lookup (3.1)
    # ------------------------------------------------------------

    def lookup(self, pack_name: str, key: str):
        """
        Direct entry lookup inside a pack.
        """
        pack = self._packs.get(pack_name)
        if not pack:
            return None

        return pack["entries"].get(key)

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "version": self.VERSION,
            "registered_packs": list(self._packs.keys()),
            "count": len(self._packs),
            "packs_with_meta": [
                name for name, p in self._packs.items() if "meta" in p
            ]
        }

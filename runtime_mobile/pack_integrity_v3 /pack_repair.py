"""
pack_repair.py
--------------
Auto‑repair module for Pack Integrity v3.

Responsibilities:
- Attempt deterministic repair of corrupted packs
- Restore missing metadata fields
- Ensure stable behavior for Self‑Repair Layer 4.4
- Fully offline, no dynamic imports or reflection

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""


class PackRepair:
    """
    Deterministic repair logic for knowledge packs.
    """

    DEFAULT_META = {
        "version": "unknown",
        "type": "generic"
    }

    def repair(self, pack: dict) -> dict:
        """
        Attempts to repair a corrupted pack.
        Only fills missing metadata fields.
        Never modifies pack data.
        """

        if not isinstance(pack, dict):
            return {
                "repaired": False,
                "error": "invalid_pack_type"
            }

        if "meta" not in pack or not isinstance(pack["meta"], dict):
            pack["meta"] = {}

        # Fill missing metadata keys
        for key, value in self.DEFAULT_META.items():
            if key not in pack["meta"]:
                pack["meta"][key] = value

        return {
            "repaired": True,
            "pack": pack
        }

# ============================================================
# SIRIUS LOCAL AI GAMA - Pack Manager
# Version: 3.0.0-pre
# ============================================================

import json
import os
from typing import Dict, Any, Optional, List


class PackManager:

    PACK_MANAGER_VERSION = "3.0.0-pre"

    def __init__(self, base_path: str):
        self.base_path = base_path
        self.cache: Dict[str, Dict[str, Any]] = {}

    # ------------------------------------------------------------
    # Pack Loading
    # ------------------------------------------------------------

    def load(self, pack_name: str) -> Optional[Dict[str, Any]]:

        if pack_name in self.cache:
            return self.cache[pack_name]

        file_path = os.path.join(self.base_path, f"{pack_name}.json")

        if not os.path.exists(file_path):
            return None

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not self._validate_pack(data):
                print(f"[ERROR] Invalid pack structure: {pack_name}")
                return None

            self.cache[pack_name] = data
            return data

        except Exception as e:
            print(f"[ERROR] Failed to load pack '{pack_name}': {e}")
            return None

    # ------------------------------------------------------------
    # Pack Listing
    # ------------------------------------------------------------

    def list_packs(self) -> List[str]:
        if not os.path.exists(self.base_path):
            return []
        return [
            f.replace(".json", "")
            for f in os.listdir(self.base_path)
            if f.endswith(".json")
        ]

    # ------------------------------------------------------------
    # Entry Access
    # ------------------------------------------------------------

    def get_entry(self, pack_name: str, key: str) -> Optional[Any]:
        pack = self.load(pack_name)
        if not pack:
            return None
        return pack["entries"].get(key)

    def search_in_packs(self, key: str) -> Optional[Any]:
        """Search key across all packs by priority."""
        packs = []
        for name in self.list_packs():
            pack = self.load(name)
            if pack:
                packs.append(pack)

        packs.sort(key=lambda p: p.get("priority", 0), reverse=True)

        for pack in packs:
            if key in pack["entries"]:
                return pack["entries"][key]

        return None

    # ------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------

    def _validate_pack(self, data: Dict[str, Any]) -> bool:

        if not isinstance(data, dict):
            return False

        required = ["name", "version", "entries"]
        for r in required:
            if r not in data:
                return False

        if not isinstance(data["entries"], dict):
            return False

        # Optional metadata defaults
        data.setdefault("priority", 0)
        data.setdefault("pack_type", "static")
        data.setdefault("language", "en")
        data.setdefault("tags", [])

        return True

    # ------------------------------------------------------------
    # Cache Control
    # ------------------------------------------------------------

    def reload(self, pack_name: str):
        if pack_name in self.cache:
            del self.cache[pack_name]
        return self.load(pack_name)

    def reload_all(self):
        self.cache.clear()
        return [self.load(name) for name in self.list_packs()]

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
        return {
            "pack_manager_version": self.PACK_MANAGER_VERSION,
            "base_path": self.base_path,
            "cached_packs": list(self.cache.keys()),
        }

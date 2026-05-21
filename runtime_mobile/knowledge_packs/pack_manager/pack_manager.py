# ============================================================
# SIRIUS LOCAL AI GAMA - Pack Manager
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Upgraded for GAMA Runtime 3.1:
# - metadata v3 support (pack_id, checksum, entries_count)
# - strict validation mode
# - improved error handling
# - caching optimizations
# - compatibility with PackGraph / PackLinker / PackValidator 3.1
# ============================================================

import json
import os
import hashlib
from typing import Dict, Any, Optional, List


class PackManager:

    PACK_MANAGER_VERSION = "3.1.0"

    def __init__(self, base_path: str):
        self.base_path = base_path
        self.cache: Dict[str, Dict[str, Any]] = {}

    # ------------------------------------------------------------
    # Pack Loading
    # ------------------------------------------------------------

    def load(self, pack_name: str) -> Optional[Dict[str, Any]]:

        # Cached?
        if pack_name in self.cache:
            return self.cache[pack_name]

        file_path = os.path.join(self.base_path, f"{pack_name}.json")

        if not os.path.exists(file_path):
            print(f"[WARN] Pack not found: {pack_name}")
            return None

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Validate structure
            if not self._validate_pack(data):
                print(f"[ERROR] Invalid pack structure: {pack_name}")
                return None

            # Auto-fill metadata
            self._apply_metadata_defaults(data)

            # Cache
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

        # Sort by priority DESC
        packs.sort(key=lambda p: p.get("priority", 0), reverse=True)

        for pack in packs:
            if key in pack["entries"]:
                return pack["entries"][key]

        return None

    # ------------------------------------------------------------
    # Validation (3.1 strict mode)
    # ------------------------------------------------------------

    def _validate_pack(self, data: Dict[str, Any]) -> bool:

        if not isinstance(data, dict):
            return False

        required = ["name", "version", "entries"]
        for r in required:
            if r not in data:
                print(f"[ERROR] Missing required field: {r}")
                return False

        if not isinstance(data["entries"], dict):
            print("[ERROR] entries must be a dict")
            return False

        return True

    # ------------------------------------------------------------
    # Metadata Defaults (3.1)
    # ------------------------------------------------------------

    def _apply_metadata_defaults(self, data: Dict[str, Any]):

        # Priority
        data.setdefault("priority", 0)

        # Pack type
        data.setdefault("pack_type", "static")

        # Language
        data.setdefault("language", "en")

        # Tags
        data.setdefault("tags", [])

        # Pack ID
        data.setdefault("pack_id", data["name"])

        # Entries count
        data["entries_count"] = len(data["entries"])

        # Checksum
        if data.get("checksum") in (None, "auto"):
            data["checksum"] = self._compute_checksum(data)

    def _compute_checksum(self, data: Dict[str, Any]) -> str:
        """Compute SHA-256 checksum of entries."""
        raw = json.dumps(data["entries"], sort_keys=True).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

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

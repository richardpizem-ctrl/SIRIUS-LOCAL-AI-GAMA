# ============================================================
# SIRIUS LOCAL AI GAMA - Pack Manager
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Loads and manages offline JSON knowledge packs for the GAMA
# mobile runtime.
#
# GAMA 3-ready features:
#   - safe JSON loading
#   - caching
#   - metadata extraction
#   - pack validation
#   - priority support (future)
#   - clean error handling
# ============================================================

import json
import os
from typing import Dict, Any, Optional, List


class PackManager:
    """
    Loads and manages offline JSON knowledge packs for the GAMA mobile runtime.
    """

    PACK_MANAGER_VERSION = "3.0.0-pre"

    def __init__(self, base_path: str):
        """
        base_path: directory where JSON packs are stored.
        Example: runtime_mobile/knowledge_packs/data/
        """
        self.base_path = base_path
        self.cache: Dict[str, Dict[str, Any]] = {}

    # ------------------------------------------------------------
    # Pack Loading
    # ------------------------------------------------------------

    def load(self, pack_name: str) -> Optional[Dict[str, Any]]:
        """
        Loads a JSON knowledge pack by name.
        Returns a dictionary or None if not found or invalid.
        """

        # Return from cache if already loaded
        if pack_name in self.cache:
            return self.cache[pack_name]

        file_path = os.path.join(self.base_path, f"{pack_name}.json")

        if not os.path.exists(file_path):
            return None

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Validate structure
            if not self._validate_pack(data):
                return None

            # Cache the loaded pack
            self.cache[pack_name] = data
            return data

        except Exception as e:
            print(f"[ERROR] Failed to load pack '{pack_name}': {e}")
            return None

    # ------------------------------------------------------------
    # Pack Listing
    # ------------------------------------------------------------

    def list_packs(self) -> List[str]:
        """
        Returns a list of available JSON pack names in the base directory.
        """
        if not os.path.exists(self.base_path):
            return []

        files = os.listdir(self.base_path)
        return [
            f.replace(".json", "")
            for f in files
            if f.endswith(".json")
        ]

    # ------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------

    def _validate_pack(self, data: Dict[str, Any]) -> bool:
        """
        Validates the structure of a knowledge pack.
        GAMA 3.x requires:
            - "name": str
            - "version": str
            - "entries": dict
        """

        if not isinstance(data, dict):
            return False

        if "entries" not in data:
            return False

        if not isinstance(data["entries"], dict):
            return False

        # Optional metadata
        if "name" not in data:
            data["name"] = "unknown"

        if "version" not in data:
            data["version"] = "1.0.0"

        return True

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
        """Returns metadata about the pack manager."""
        return {
            "pack_manager_version": self.PACK_MANAGER_VERSION,
            "base_path": self.base_path,
            "cached_packs": list(self.cache.keys()),
        }

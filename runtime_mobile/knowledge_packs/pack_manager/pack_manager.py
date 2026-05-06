import json
import os


class PackManager:
    """
    Loads and manages offline JSON knowledge packs for the GAMA mobile runtime.
    """

    def __init__(self, base_path):
        """
        base_path: directory where JSON packs are stored.
        Example: runtime_mobile/knowledge_packs/data/
        """
        self.base_path = base_path
        self.cache = {}

    def load(self, pack_name: str):
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

            # Cache the loaded pack
            self.cache[pack_name] = data
            return data

        except Exception:
            return None

    def list_packs(self):
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

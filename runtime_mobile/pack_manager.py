# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Pack Manager
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Minimal knowledge pack manager for the mobile runtime.
# Provides a stable API for MobileKnowledgePacks.
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

class MobilePackManager:
    """
    Minimal pack manager for GAMA 3.0.0-pre.
    Placeholder for loading JSON knowledge packs.
    """

    def __init__(self):
        # In future: filesystem / assets / embedded packs
        self._packs = {}

    def register(self, name: str, pack: dict):
        """
        Register a pack programmatically.
        Used for testing or embedded packs.
        """
        self._packs[name] = pack

    def load(self, name: str):
        """
        Load a pack by name.
        For now: returns from in-memory registry only.
        """
        return self._packs.get(name)

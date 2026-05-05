# SIRIUS LOCAL AI GAMA - Base Module Class

class BaseModule:
    """Base class for all mobile modules."""

    def __init__(self, name: str):
        self.name = name
        self.loaded = False

    def load(self):
        """Load module resources."""
        self.loaded = True

    def unload(self):
        """Unload module resources."""
        self.loaded = False

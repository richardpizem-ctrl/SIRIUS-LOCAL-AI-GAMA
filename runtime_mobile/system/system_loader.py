"""
SIRIUS LOCAL AI GAMA – System Loader
Mobile Runtime 3.2.0

Initializes:
- core runtime context
- event engine
- vision engine
- security modules
- UI modules
- NL router
"""

from vision import VisionEngineV3
from runtime_mobile.event_engine.event_router_entry import EventRouterEntry
from runtime_mobile.vision.vision_entry import VisionEntry


class SystemContext:
    """
    Global runtime context shared across modules.
    """
    def __init__(self):
        self.vision_engine = None
        self.event_router = None
        self.vision_entry = None

        # other runtime components can be added here
        self.security = None
        self.ui = None
        self.nl = None


class SystemLoader:
    """
    Main system loader for Mobile Runtime 3.2.0.
    Responsible for initializing all runtime components.
    """

    VERSION = "3.2.0"

    def __init__(self):
        self.context = SystemContext()

    # ---------------------------------------------------------
    # Vision Engine
    # ---------------------------------------------------------

    def _load_vision_engine(self):
        """
        Load VisionEngineV3 and attach it to context.
        """
        try:
            engine = VisionEngineV3()
            self.context.vision_engine = engine
            print("[SystemLoader] VisionEngineV3 loaded.")
        except Exception as e:
            print("[SystemLoader] Failed to load VisionEngineV3:", e)

    # ---------------------------------------------------------
    # Vision Entry
    # ---------------------------------------------------------

    def _load_vision_entry(self):
        """
        Load VisionEntry and attach it to context.
        """
        try:
            entry = VisionEntry(self.context)
            self.context.vision_entry = entry
            print("[SystemLoader] VisionEntry loaded.")
        except Exception as e:
            print("[SystemLoader] Failed to load VisionEntry:", e)

    # ---------------------------------------------------------
    # Event Engine
    # ---------------------------------------------------------

    def _load_event_engine(self):
        """
        Load EventRouterEntry and attach it to context.
        """
        try:
            router = EventRouterEntry(self.context)
            self.context.event_router = router
            print("[SystemLoader] EventRouterEntry loaded.")
        except Exception as e:
            print("[SystemLoader] Failed to load EventRouterEntry:", e)

    # ---------------------------------------------------------
    # Main Loader
    # ---------------------------------------------------------

    def load_all(self):
        """
        Load all runtime components.
        """
        print("[SystemLoader] Loading Mobile Runtime 3.2.0...")

        self._load_vision_engine()
        self._load_vision_entry()
        self._load_event_engine()

        print("[SystemLoader] Runtime initialization complete.")
        return self.context

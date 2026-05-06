from runtime_mobile.security.security_entry import MobileSecurityEntry
from runtime_mobile.vision.vision_entry import MobileVisionEntry
from runtime_mobile.knowledge_packs.packs_mobile import MobileKnowledgePacks
from runtime_mobile.knowledge_packs.pack_manager.pack_manager import PackManager


class MobileRuntimeContext:
    """
    Base context for the GAMA mobile runtime.
    Stores runtime state, configuration and module instances.
    """

    def __init__(self):
        # Runtime state
        self.state = {
            "initialized": False,
            "active_module": None,
            "last_event": None,
            "restricted_mode": False
        }

        # Runtime configuration
        self.config = {
            "version": "1.0.0",
            "platform": "mobile",
            "debug": False,
        }

        # Permissions placeholder (extend later)
        self.permissions = None

        # Module instances (created after load)
        self.security = None
        self.vision = None
        self.packs = None

        # Knowledge pack manager
        self.pack_manager = PackManager(
            "runtime_mobile/knowledge_packs/data"
        )

    def load(self):
        """
        Initializes the runtime context.
        Loads modules and prepares the runtime environment.
        """

        # Mark runtime as initialized
        self.state["initialized"] = True

        # Initialize modules
        self.security = MobileSecurityEntry(self)
        self.vision = MobileVisionEntry(self)
        self.packs = MobileKnowledgePacks(self)

    def set_active_module(self, module_name: str):
        """Sets the currently active module."""
        self.state["active_module"] = module_name

    def update_last_event(self, event_type: str):
        """Stores the last processed event type."""
        self.state["last_event"] = event_type

    def set_restricted_mode(self, enabled: bool):
        """Enables or disables restricted mode."""
        self.state["restricted_mode"] = enabled

    def get_state(self):
        """Returns the full runtime state."""
        return self.state

    def get_config(self):
        """Returns the runtime configuration."""
        return self.config

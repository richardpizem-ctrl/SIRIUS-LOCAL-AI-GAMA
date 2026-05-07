# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Context
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Stores:
#   - runtime state
#   - configuration
#   - module instances
#   - security profile
#   - restricted mode
#   - knowledge pack manager
#
# GAMA 3-ready features:
#   - diagnostics module slot
#   - energy governor slot
#   - unified module initialization
#   - versioned metadata
#   - clean runtime injection
# ============================================================

from runtime_mobile.security.security_entry import MobileSecurityEntry
from runtime_mobile.vision.vision_entry import MobileVisionEntry
from runtime_mobile.knowledge_packs.packs_mobile import MobileKnowledgePacks
from runtime_mobile.knowledge_packs.pack_manager.pack_manager import PackManager


class MobileRuntimeContext:
    """
    Base context for the GAMA mobile runtime.
    Stores runtime state, configuration and module instances.
    """

    CONTEXT_VERSION = "3.0.0-pre"

    def __init__(self):
        # --------------------------------------------------------
        # Runtime State
        # --------------------------------------------------------
        self.state = {
            "initialized": False,
            "active_module": None,
            "last_event": None,
            "restricted_mode": False,
        }

        # --------------------------------------------------------
        # Runtime Configuration
        # --------------------------------------------------------
        self.config = {
            "version": "3.0.0-pre",
            "platform": "mobile",
            "debug": False,
        }

        # Permissions placeholder
        self.permissions = None

        # --------------------------------------------------------
        # Module Instances (injected on load)
        # --------------------------------------------------------
        self.security = None
        self.vision = None
        self.packs = None

        # Future modules (GAMA 2.0 → 3.0)
        self.diagnostics = None
        self.energy_governor = None
        self.workflow = None
        self.lan_bridge = None

        # --------------------------------------------------------
        # Knowledge Pack Manager
        # --------------------------------------------------------
        self.pack_manager = PackManager(
            "runtime_mobile/knowledge_packs/data"
        )

    # ------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------

    def load(self):
        """
        Initializes the runtime context.
        Loads modules and prepares the runtime environment.
        """

        self.state["initialized"] = True

        # Initialize core modules
        self.security = MobileSecurityEntry(self)
        self.vision = MobileVisionEntry(self)
        self.packs = MobileKnowledgePacks(self)

        # Optional modules (attached later by runtime)
        # diagnostics, governor, workflow, lan_bridge

    # ------------------------------------------------------------
    # State Management
    # ------------------------------------------------------------

    def set_active_module(self, module_name: str):
        """Sets the currently active module."""
        self.state["active_module"] = module_name

    def update_last_event(self, event_type: str):
        """Stores the last processed event type."""
        self.state["last_event"] = event_type

    def set_restricted_mode(self, enabled: bool):
        """Enables or disables restricted mode."""
        self.state["restricted_mode"] = enabled

    # ------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------

    def get_state(self):
        """Returns the full runtime state."""
        return self.state

    def get_config(self):
        """Returns the runtime configuration."""
        return self.config

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
        """Return context metadata for diagnostics/UI."""
        return {
            "context_version": self.CONTEXT_VERSION,
            "initialized": self.state["initialized"],
            "restricted_mode": self.state["restricted_mode"],
            "active_module": self.state["active_module"],
            "modules": {
                "security": self.security is not None,
                "vision": self.vision is not None,
                "packs": self.packs is not None,
                "diagnostics": self.diagnostics is not None,
                "energy_governor": self.energy_governor is not None,
                "workflow": self.workflow is not None,
                "lan_bridge": self.lan_bridge is not None,
            }
        }

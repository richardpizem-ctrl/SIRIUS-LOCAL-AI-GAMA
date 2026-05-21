# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Context
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
# ============================================================

from runtime_mobile.security.security_module import SecurityModule
from runtime_mobile.vision.vision_module import VisionModule
from runtime_mobile.knowledge.knowledge_module import KnowledgeModule
from runtime_mobile.permissions.permissions import MobilePermissions
from runtime_mobile.knowledge_packs.pack_manager.pack_manager import PackManager


class MobileRuntimeContext:

    CONTEXT_VERSION = "3.1.0"

    def __init__(self):

        self.loaded = False

        # Runtime State
        self.state = {
            "initialized": False,
            "active_module": None,
            "last_event": None,
            "restricted_mode": False,
        }

        # Runtime Configuration
        self.config = {
            "version": "3.1.0",
            "platform": "mobile",
            "debug": False,
        }

        # Permissions (3.1: profile + restricted mode)
        self.permissions = MobilePermissions(profile="OWNER", restricted=False)

        # Module Instances
        self.security = None
        self.vision = None
        self.packs = None

        # Optional modules
        self.diagnostics = None
        self.energy_governor = None
        self.workflow = None
        self.lan_bridge = None

        # Knowledge Pack Manager
        self.pack_manager = PackManager("runtime_mobile/knowledge_packs/data")

    # ------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------

    def load(self):
        self.loaded = True
        self.state["initialized"] = True

        # Core modules
        self.security = SecurityModule()
        self.vision = VisionModule()
        self.packs = KnowledgeModule()

        # Attach runtime reference + load
        for module in (self.security, self.vision, self.packs):
            module.attach_runtime(self)
            module.load()

    # ------------------------------------------------------------
    # State Management
    # ------------------------------------------------------------

    def set_active_module(self, module_name: str):
        self.state["active_module"] = module_name

    def update_last_event(self, event_type: str):
        self.state["last_event"] = event_type

    def set_restricted_mode(self, enabled: bool):
        self.state["restricted_mode"] = bool(enabled)
        # Keep permissions in sync with context
        self.permissions.set_restricted(bool(enabled))

    # ------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------

    def get_security_profile(self):
        return self.permissions.get_profile()

    def is_restricted_mode(self):
        return self.state["restricted_mode"]

    def get_state(self):
        return self.state

    def get_config(self):
        return self.config

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
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

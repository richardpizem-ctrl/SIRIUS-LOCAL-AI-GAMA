# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Context
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Holds runtime state, session data, module references,
# and metadata for the mobile execution environment.
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

class MobileRuntimeContext:
    """
    Holds temporary state, session data, module references,
    and runtime metadata for the mobile execution environment.
    """

    CONTEXT_VERSION = "3.0.0-pre"

    def __init__(self):
        # --------------------------------------------------------
        # Session & State
        # --------------------------------------------------------
        self.session_id = None
        self.language = "en"
        self.last_event = None

        # Runtime state dictionary
        self.state = {
            "restricted_mode": False,
            "initialized": False,
            "active_module": None,
        }

        # --------------------------------------------------------
        # Device metadata
        # --------------------------------------------------------
        self.device_info = {}

        # --------------------------------------------------------
        # Runtime modules (injected by MobileRuntimeCore)
        # --------------------------------------------------------
        self.pack_manager = None
        self.vision_engine = None
        self.security = None
        self.knowledge_packs = None
        self.diagnostics = None
        self.energy_governor = None
        self.workflow = None
        self.lan_bridge = None

    # ------------------------------------------------------------
    # State setters
    # ------------------------------------------------------------

    def set_device_info(self, info):
        self.device_info = info

    def update_last_event(self, event):
        self.last_event = event

    def set_language(self, lang):
        self.language = lang

    def set_restricted_mode(self, enabled: bool):
        self.state["restricted_mode"] = enabled

    def set_active_module(self, module_name: str):
        self.state["active_module"] = module_name

    # ------------------------------------------------------------
    # Getters
    # ------------------------------------------------------------

    def get_state(self):
        return self.state

    def get_config(self):
        return {
            "version": self.CONTEXT_VERSION,
            "language": self.language,
            "restricted_mode": self.state["restricted_mode"],
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        """Returns full runtime metadata."""
        return {
            "context_version": self.CONTEXT_VERSION,
            "session_id": self.session_id,
            "language": self.language,
            "restricted_mode": self.state["restricted_mode"],
            "device_info": self.device_info,
            "modules_attached": {
                "pack_manager": self.pack_manager is not None,
                "vision_engine": self.vision_engine is not None,
                "security": self.security is not None,
                "knowledge_packs": self.knowledge_packs is not None,
                "diagnostics": self.diagnostics is not None,
                "energy_governor": self.energy_governor is not None,
                "workflow": self.workflow is not None,
                "lan_bridge": self.lan_bridge is not None,
            }
        }

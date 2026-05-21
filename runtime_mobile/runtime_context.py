# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Context
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
# ============================================================

class MobileRuntimeContext:
    """
    Holds temporary state, session data, module references,
    and runtime metadata for the mobile execution environment.
    """

    CONTEXT_VERSION = "3.1.0"

    def __init__(self):
        # --------------------------------------------------------
        # Session & State
        # --------------------------------------------------------
        self.session_id = None
        self.language = "en"
        self.last_event = None

        self.state = {
            "restricted_mode": False,
            "initialized": False,
            "active_module": None,
            "app_state": "cold_start",   # foreground / background / suspended / cold_start
        }

        # --------------------------------------------------------
        # Device metadata
        # --------------------------------------------------------
        self.device_info = {}

        # --------------------------------------------------------
        # Runtime modules (attached by MobileRuntimeCore)
        # --------------------------------------------------------
        self.pack_manager = None
        self.vision_engine = None
        self.security = None
        self.knowledge_packs = None
        self.diagnostics = None
        self.energy_governor = None
        self.workflow = None
        self.lan_bridge = None
        self.assistant = None

        # --------------------------------------------------------
        # Debug log buffer
        # --------------------------------------------------------
        self._debug_log = []

    # ------------------------------------------------------------
    # State setters
    # ------------------------------------------------------------

    def set_device_info(self, info):
        self.device_info = info

    def update_last_event(self, event):
        self.last_event = event
        etype = getattr(event, "type", None) or getattr(event, "event_type", None)
        if etype:
            self._debug_log.append(f"EVENT: {etype}")

    def set_language(self, lang):
        self.language = lang

    def set_restricted_mode(self, enabled: bool):
        self.state["restricted_mode"] = bool(enabled)

    def set_active_module(self, module_name: str):
        self.state["active_module"] = module_name

    def set_app_state(self, state: str):
        """
        Update high-level app state.
        Expected values: foreground / background / suspended / cold_start
        """
        self.state["app_state"] = state

    def mark_initialized(self):
        self.state["initialized"] = True

    # ------------------------------------------------------------
    # Debug log
    # ------------------------------------------------------------

    def get_debug_log(self):
        return list(self._debug_log)

    def log(self, message: str):
        """Generic debug log entry."""
        self._debug_log.append(str(message))

    # ------------------------------------------------------------
    # Reset
    # ------------------------------------------------------------

    def reset(self):
        self.session_id = None
        self.last_event = None
        self.device_info = {}
        self.state["active_module"] = None
        self.state["restricted_mode"] = False
        self.state["initialized"] = False
        self.state["app_state"] = "cold_start"
        self._debug_log.clear()

    # ------------------------------------------------------------
    # Getters
    # ------------------------------------------------------------

    def get_state(self):
        return dict(self.state)

    def get_config(self):
        return {
            "version": self.CONTEXT_VERSION,
            "language": self.language,
            "restricted_mode": self.state["restricted_mode"],
            "app_state": self.state["app_state"],
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "context_version": self.CONTEXT_VERSION,
            "session_id": self.session_id,
            "language": self.language,
            "restricted_mode": self.state["restricted_mode"],
            "initialized": self.state["initialized"],
            "app_state": self.state["app_state"],
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
                "assistant": self.assistant is not None,
            },
            "debug_log_size": len(self._debug_log),
        }

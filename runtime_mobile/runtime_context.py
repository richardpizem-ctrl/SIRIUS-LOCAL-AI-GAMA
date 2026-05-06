# SIRIUS LOCAL AI GAMA - Mobile Runtime Context

class MobileRuntimeContext:
    """
    Holds temporary state, session data, module references,
    and runtime metadata for the mobile execution environment.
    """

    def __init__(self):
        # Session & state
        self.session_id = None
        self.language = "en"
        self.last_event = None

        # Device metadata
        self.device_info = {}

        # Runtime modules (injected by MobileRuntimeCore)
        self.pack_manager = None
        self.vision_engine = None
        self.security_engine = None
        self.knowledge_packs = None

    # --- State setters ---
    def set_device_info(self, info):
        self.device_info = info

    def update_last_event(self, event):
        self.last_event = event

    def set_language(self, lang):
        self.language = lang

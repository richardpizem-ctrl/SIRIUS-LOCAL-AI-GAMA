# SIRIUS LOCAL AI GAMA - Mobile Runtime Context

class MobileRuntimeContext:
    """
    Holds temporary state, session data, and runtime metadata
    for the mobile execution environment.
    """

    def __init__(self):
        self.session_id = None
        self.device_info = {}
        self.last_event = None
        self.language = "en"

    def set_device_info(self, info):
        self.device_info = info

    def update_last_event(self, event):
        self.last_event = event

    def set_language(self, lang):
        self.language = lang

class MobileEvent:
    """
    Base event class for the GAMA mobile runtime.
    Each event contains a type and an optional payload dictionary.
    """

    def __init__(self, event_type: str, payload=None):
        self.type = event_type
        self.payload = payload if payload is not None else {}

    def get(self, key, default=None):
        """
        Safe getter for payload values.
        """
        return self.payload.get(key, default)

    def to_dict(self):
        """
        Converts the event into a serializable dictionary.
        """
        return {
            "type": self.type,
            "payload": self.payload
        }

    def __repr__(self):
        return f"<MobileEvent type={self.type} payload={self.payload}>"


class MobileEventTypes:
    """
    Centralized list of event type constants for the mobile runtime.
    Used by NL router, dispatcher, and all modules.
    """

    # System / Runtime
    UNKNOWN = "UNKNOWN"
    OPEN_APP = "OPEN_APP"
    SHOW_HELP = "SHOW_HELP"

    # Device status
    CHECK_BATTERY = "CHECK_BATTERY"
    CHECK_WIFI = "CHECK_WIFI"

    # Security module
    SECURITY = "security"
    PERMISSION_CHECK = "permission_check"
    RESTRICTED_MODE = "restricted_mode"

    # Vision module
    VISION = "vision"
    OCR = "ocr"
    ANALYZE = "analyze"

    # Knowledge packs
    PACK_LOOKUP = "pack_lookup"

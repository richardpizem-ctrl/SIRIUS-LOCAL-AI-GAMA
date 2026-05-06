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

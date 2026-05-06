class MobileEvent:
    """
    Základná trieda pre udalosti v mobilnom runtime GAMA.
    Každý event má typ a voliteľný payload.
    """

    def __init__(self, event_type: str, payload=None):
        self.type = event_type
        self.payload = payload

    def __repr__(self):
        return f"<MobileEvent type={self.type} payload={self.payload}>"

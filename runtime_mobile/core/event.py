# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Event
# Version: 3.0.0-pre
# ============================================================

class MobileEvent:
    """
    Lightweight event object used across the mobile runtime.
    Wraps event type and arbitrary payload fields.
    """

    def __init__(self, event_type, **payload):
        self.type = event_type
        self._payload = payload

    # ------------------------------------------------------------
    # Payload Access
    # ------------------------------------------------------------

    @property
    def payload(self):
        """Unified payload accessor (required in 3.x)."""
        return self._payload

    def get(self, key, default=None):
        return self._payload.get(key, default)

    # ------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------

    def to_dict(self):
        return {
            "type": self.type,
            "payload": dict(self._payload)
        }

    def __repr__(self):
        return f"<MobileEvent type={self.type} payload={self._payload}>"

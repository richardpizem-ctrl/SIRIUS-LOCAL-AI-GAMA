# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Event
# Version: 3.1.0
# ============================================================

class MobileEvent:
    """
    Unified event object for the GAMA 3.1 runtime.
    Includes:
    - normalized input
    - intent + confidence
    - metadata v3
    - tags (vision, OCR, hybrid)
    - source tracking
    """

    def __init__(self, event_type, *,
                 raw_input=None,
                 normalized_input=None,
                 intent=None,
                 confidence=None,
                 source="unknown",
                 tags=None,
                 metadata=None,
                 **payload):

        # Core event fields
        self.type = event_type
        self.raw_input = raw_input
        self.normalized_input = normalized_input
        self.intent = intent
        self.confidence = confidence
        self.source = source

        # Metadata v3
        self.metadata = metadata or {}

        # Tags (vision, OCR, hybrid, scene)
        self.tags = tags or []

        # Original payload
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
            "raw_input": self.raw_input,
            "normalized_input": self.normalized_input,
            "intent": self.intent,
            "confidence": self.confidence,
            "source": self.source,
            "tags": list(self.tags),
            "metadata": dict(self.metadata),
            "payload": dict(self._payload),
        }

    def __repr__(self):
        return (
            f"<MobileEvent type={self.type} "
            f"intent={self.intent} conf={self.confidence} "
            f"source={self.source} tags={self.tags} "
            f"payload={self._payload}>"
        )

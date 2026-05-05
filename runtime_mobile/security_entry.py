# SIRIUS LOCAL AI GAMA - Mobile Security Layer

class MobileSecurityEntry:
    """
    Mobile security evaluation layer.
    """

    def evaluate(self, event):
        text = event.get("text", "").lower()

        # Basic mobile-safe rules
        forbidden = ["hack", "bypass", "cheat", "exploit"]

        if any(word in text for word in forbidden):
            return "deny"

        return "allow"

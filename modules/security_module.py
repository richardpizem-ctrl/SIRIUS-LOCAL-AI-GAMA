# SIRIUS LOCAL AI GAMA - Security Module

from .base_module import BaseModule

class SecurityModule(BaseModule):
    """Security evaluation module for mobile runtime."""

    def __init__(self):
        super().__init__("security")

    def evaluate(self, event):
        forbidden = ["hack", "bypass", "exploit"]

        text = event.get("text", "").lower()

        if any(word in text for word in forbidden):
            return "deny"

        return "allow"

# SIRIUS LOCAL AI GAMA - Mobile NL Router

class MobileNLRouter:
    """
    Lightweight intent router for mobile runtime.
    Routes events to vision, knowledge packs, or other modules.
    """

    def route(self, event):
        text = event.get("text", "").lower()

        if any(k in text for k in ["scan", "photo", "ocr", "camera"]):
            return "vision"

        if any(k in text for k in ["how", "why", "what", "explain"]):
            return "knowledge"

        return "unknown"

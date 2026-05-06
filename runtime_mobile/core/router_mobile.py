class MobileNLRouter:
    """
    Natural Language router for the GAMA mobile runtime.
    Converts user text commands into internal event identifiers.
    """

    def route(self, text: str):
        """
        Input:
            text (str): User text command.

        Output:
            dict: Event object with type + optional parameters.
        """

        if not text:
            return {"type": "UNKNOWN"}

        t = text.lower()

        # --- APP CONTROL ---
        if "open" in t:
            return {"type": "OPEN_APP"}

        # --- DEVICE STATUS ---
        if "battery" in t:
            return {"type": "CHECK_BATTERY"}

        if "wifi" in t:
            return {"type": "CHECK_WIFI"}

        # --- SECURITY ---
        if "permission" in t or "allow" in t or "deny" in t:
            return {"type": "security", "permission": "generic"}

        if "restricted" in t:
            enabled = "on" in t or "enable" in t
            return {"type": "security", "enabled": enabled}

        # --- VISION ---
        if "read" in t or "ocr" in t or "text from image" in t:
            return {"type": "vision", "mode": "ocr"}

        if "analyze" in t or "what is in the picture" in t:
            return {"type": "vision", "mode": "analyze"}

        # --- KNOWLEDGE PACKS ---
        if "lookup" in t or "search" in t:
            return {"type": "packs", "key": "query"}

        # --- HELP ---
        if "help" in t:
            return {"type": "SHOW_HELP"}

        # Default fallback
        return {"type": "UNKNOWN"}

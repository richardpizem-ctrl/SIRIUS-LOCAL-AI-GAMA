from runtime_mobile.core.event_types import MobileEvent, MobileEventTypes


class MobileNLRouter:
    """
    Natural Language router for the GAMA mobile runtime.
    Converts user text commands into MobileEvent objects.
    """

    def route(self, text: str):
        """
        Input:
            text (str): User text command.

        Output:
            MobileEvent: Parsed event with type + payload.
        """

        if not text:
            return MobileEvent(MobileEventTypes.UNKNOWN)

        t = text.lower()

        # --- APP CONTROL ---
        if "open" in t:
            return MobileEvent(MobileEventTypes.OPEN_APP)

        # --- DEVICE STATUS ---
        if "battery" in t:
            return MobileEvent(MobileEventTypes.CHECK_BATTERY)

        if "wifi" in t:
            return MobileEvent(MobileEventTypes.CHECK_WIFI)

        # --- SECURITY ---
        if "permission" in t or "allow" in t or "deny" in t:
            return MobileEvent(
                MobileEventTypes.SECURITY,
                {"permission": "generic"}
            )

        if "restricted" in t:
            enabled = "on" in t or "enable" in t
            return MobileEvent(
                MobileEventTypes.RESTRICTED_MODE,
                {"enabled": enabled}
            )

        # --- VISION ---
        if "read" in t or "ocr" in t or "text from image" in t:
            return MobileEvent(
                MobileEventTypes.OCR,
                {"mode": "ocr"}
            )

        if "analyze" in t or "what is in the picture" in t:
            return MobileEvent(
                MobileEventTypes.ANALYZE,
                {"mode": "analyze"}
            )

        # --- KNOWLEDGE PACKS ---
        if "lookup" in t or "search" in t:
            return MobileEvent(
                MobileEventTypes.PACK_LOOKUP,
                {"key": "query"}
            )

        # --- HELP ---
        if "help" in t:
            return MobileEvent(MobileEventTypes.SHOW_HELP)

        # Default fallback
        return MobileEvent(MobileEventTypes.UNKNOWN)

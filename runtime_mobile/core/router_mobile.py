class MobileNLRouter:
    """
    Simple Natural Language router for the GAMA mobile runtime.
    Converts user text commands into internal event identifiers.
    """

    def route(self, text: str):
        """
        Input:
            text (str): User text command.

        Output:
            str: Event type name that the runtime will process.
        """

        if not text:
            return "UNKNOWN"

        t = text.lower()

        # Basic commands
        if "open" in t:
            return "OPEN_APP"

        if "battery" in t:
            return "CHECK_BATTERY"

        if "wifi" in t:
            return "CHECK_WIFI"

        if "help" in t:
            return "SHOW_HELP"

        # Default fallback
        return "UNKNOWN"

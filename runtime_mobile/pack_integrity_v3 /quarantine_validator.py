"""
quarantine_validator.py
-----------------------
Validation layer for Quarantine Pipeline v3.

Responsibilities:
- Validate event structure
- Detect malformed or suspicious payloads
- Enforce deterministic rules (no randomness)
- Provide clear reason codes for quarantine decisions

This module is part of SIRIUS Mobile Runtime 3.3.0.
Prepared for Self‑Repair Layer 4.4.
"""


class QuarantineValidator:
    """
    Deterministic event validator.
    No dynamic evaluation, no unsafe parsing.
    """

    REQUIRED_FIELDS = ["type", "payload"]
    MAX_PAYLOAD_SIZE = 50000  # hard safety limit

    def validate(self, event: dict) -> dict:
        """
        Validates event structure.
        Returns:
            {
                "valid": True/False,
                "reason": "..."
            }
        """

        # 1. Must be a dictionary
        if not isinstance(event, dict):
            return self._fail("event_not_dict")

        # 2. Required fields
        for field in self.REQUIRED_FIELDS:
            if field not in event:
                return self._fail(f"missing_field_{field}")

        # 3. Type must be a string
        if not isinstance(event["type"], str):
            return self._fail("type_not_string")

        # 4. Payload must be a dictionary
        if not isinstance(event["payload"], dict):
            return self._fail("payload_not_dict")

        # 5. Payload size limit
        if len(str(event["payload"])) > self.MAX_PAYLOAD_SIZE:
            return self._fail("payload_too_large")

        # 6. No executable content allowed
        if self._contains_executable(event["payload"]):
            return self._fail("executable_content_detected")

        # Passed all checks
        return {"valid": True, "reason": None}

    # ---------------------------------------------------------

    def _contains_executable(self, payload: dict) -> bool:
        """
        Detects dangerous content:
        - code fragments
        - script tags
        - eval-like patterns
        """

        text = str(payload).lower()

        forbidden = [
            "import ",
            "exec(",
            "eval(",
            "<script",
            "os.system",
            "subprocess",
            "rm -rf",
            "base64decode",
        ]

        return any(f in text for f in forbidden)

    # ---------------------------------------------------------

    def _fail(self, reason: str) -> dict:
        return {"valid": False, "reason": reason}

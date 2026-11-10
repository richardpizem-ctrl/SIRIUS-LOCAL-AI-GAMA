"""
quarantine_validator.py
-----------------------
Validation layer for Quarantine Pipeline v3.

Responsibilities:
- Validate incoming event structure
- Detect unsafe or malformed payloads
- Enforce deterministic safety rules
- Fully offline, no dynamic imports or reflection
- Support Self‑Repair Layer 4.4

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""


class QuarantineValidator:
    """
    Deterministic validator for quarantine events.
    """

    REQUIRED_FIELDS = ["type", "payload"]

    def validate(self, event: dict) -> dict:
        """
        Validates event structure and safety.

        Returns:
            {"valid": True}
            {"valid": False, "reason": "..."}
        """

        # Must be a dictionary
        if not isinstance(event, dict):
            return {
                "valid": False,
                "reason": "invalid_event_type"
            }

        # Check required fields
        for field in self.REQUIRED_FIELDS:
            if field not in event:
                return {
                    "valid": False,
                    "reason": f"missing_field_{field}"
                }

        # Validate event type
        if not isinstance(event["type"], str):
            return {
                "valid": False,
                "reason": "invalid_type_field"
            }

        # Validate payload
        if not isinstance(event["payload"], dict):
            return {
                "valid": False,
                "reason": "invalid_payload_type"
            }

        # Detect suspicious keys
        forbidden = ["script", "html", "exec", "cmd"]
        for key in forbidden:
            if key in event["payload"]:
                return {
                    "valid": False,
                    "reason": f"forbidden_key_{key}"
                }

        # Everything is clean
        return {"valid": True}

"""
quarantine_router.py
--------------------
Primary entry point for the Quarantine Pipeline v3.

Responsibilities:
- Intercept incoming events before Event Engine
- Validate payload structure
- Detect suspicious or malformed data
- Route event to quarantine storage if needed
- Provide deterministic decision-making (no randomness)

This module is part of SIRIUS Mobile Runtime 3.3.0.
Prepared for Self‑Repair Layer 4.4.
"""

from .quarantine_validator import QuarantineValidator
from .quarantine_storage import QuarantineStorage
from .quarantine_diagnostics import QuarantineDiagnostics


class QuarantineRouter:
    """
    Deterministic quarantine router.
    No dynamic imports, no reflection, no unsafe evaluation.
    """

    def __init__(self):
        self.validator = QuarantineValidator()
        self.storage = QuarantineStorage()
        self.diagnostics = QuarantineDiagnostics()

    def process_event(self, event: dict) -> dict:
        """
        Main entry point.
        Returns:
            - {"status": "clean", "event": event}  → safe to continue
            - {"status": "quarantined", "id": qid} → event isolated
        """

        # Step 1: Validate structure
        validation = self.validator.validate(event)

        if not validation["valid"]:
            # Step 2: Store in quarantine
            qid = self.storage.store(event, reason=validation["reason"])

            # Step 3: Log diagnostics
            self.diagnostics.log_quarantine(event, qid, validation["reason"])

            return {
                "status": "quarantined",
                "id": qid,
                "reason": validation["reason"]
            }

        # Event is clean
        return {
            "status": "clean",
            "event": event
        }

"""
quarantine_router.py
--------------------
Primary entry point for the Quarantine Pipeline v3.

Responsibilities:
- Intercept incoming events before Event Engine
- Validate payload structure and safety
- Route unsafe events into quarantine storage
- Provide deterministic diagnostics
- Fully offline, no dynamic imports or reflection

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""

from .quarantine_validator import QuarantineValidator
from .quarantine_storage import QuarantineStorage
from .quarantine_diagnostics import QuarantineDiagnostics


class QuarantineRouter:
    """
    Deterministic quarantine router.
    """

    def __init__(self):
        self.validator = QuarantineValidator()
        self.storage = QuarantineStorage()
        self.diagnostics = QuarantineDiagnostics()

    def process_event(self, event: dict) -> dict:
        """
        Main entry point for quarantine routing.

        Returns:
            - {"status": "clean", "event": event}
            - {"status": "quarantined", "id": qid, "reason": reason}
        """

        # Step 1: Validate event structure and safety
        validation = self.validator.validate(event)

        if not validation["valid"]:
            # Step 2: Store event in quarantine
            qid = self.storage.store(event, reason=validation["reason"])

            # Step 3: Log diagnostics
            self.diagnostics.log_quarantine(event, qid, validation["reason"])

            return {
                "status": "quarantined",
                "id": qid,
                "reason": validation["reason"]
            }

        # Event is clean → pass through
        return {
            "status": "clean",
            "event": event
        }

"""
quarantine_diagnostics.py
-------------------------
Diagnostics layer for Quarantine Pipeline v3.

Responsibilities:
- Log all quarantine actions
- Provide deterministic diagnostic output
- Support Self‑Repair Layer 4.4
- Never expose sensitive data
- Fully offline, no external dependencies

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""

import time
import os
import json


class QuarantineDiagnostics:
    """
    Deterministic diagnostics logger for quarantine events.
    """

    LOG_DIR = "runtime_quarantine_logs"

    def __init__(self):
        # Ensure log directory exists
        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

    def log_quarantine(self, event: dict, qid: str, reason: str):
        """
        Logs a quarantined event.
        Creates a simple JSON log entry.
        """

        log_entry = {
            "timestamp": int(time.time()),
            "id": qid,
            "reason": reason,
            "event_type": event.get("type", "unknown")
        }

        path = os.path.join(self.LOG_DIR, f"{qid}.log.json")

        with open(path, "w", encoding="utf-8") as f:
            json.dump(log_entry, f, indent=2, ensure_ascii=False)

    def list_logs(self) -> list:
        """
        Returns a list of all quarantine log filenames.
        """

        try:
            return sorted(os.listdir(self.LOG_DIR))
        except FileNotFoundError:
            return []

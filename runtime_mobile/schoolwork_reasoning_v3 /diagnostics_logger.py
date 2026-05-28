"""
diagnostics_logger.py
---------------------
Diagnostics logger for Schoolwork Reasoning Engine v3.

Responsibilities:
- Log reasoning pipeline events
- Provide deterministic, offline-safe diagnostics
- Never log sensitive student data
- Support Self‑Repair Layer 4.4
- Produce simple JSON-like log entries

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""

import time
import os
import json


class DiagnosticsLogger:
    """
    Deterministic diagnostics logger for schoolwork reasoning.
    """

    LOG_DIR = "runtime_schoolwork_logs"

    def __init__(self):
        # Ensure log directory exists
        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

    def log(self, subject: str, normalized: str, steps: list):
        """
        Logs a reasoning session.
        """

        entry = {
            "timestamp": int(time.time()),
            "subject": subject,
            "normalized_length": len(normalized),
            "steps_count": len(steps)
        }

        filename = f"log_{entry['timestamp']}.json"
        path = os.path.join(self.LOG_DIR, filename)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(entry, f, indent=2, ensure_ascii=False)

    def list_logs(self) -> list:
        """
        Returns a list of all diagnostic log filenames.
        """

        try:
            return sorted(os.listdir(self.LOG_DIR))
        except FileNotFoundError:
            return []

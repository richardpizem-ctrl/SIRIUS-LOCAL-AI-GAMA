"""
sandbox_violation_handler.py
----------------------------
Violation handler for Sandbox Enforcement v3.

Responsibilities:
- Handle sandbox violations deterministically
- Log all unauthorized actions
- Provide safe fallback behavior
- Support Self‑Repair Layer 4.4
- Fully offline, no external dependencies

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""

import time
import os
import json


class SandboxViolationHandler:
    """
    Deterministic handler for sandbox violations.
    Logs violations and provides safe fallback behavior.
    """

    LOG_DIR = "runtime_sandbox_violations"

    def __init__(self):
        # Ensure log directory exists
        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

    # -------------------------------------------------------------

    def handle_violation(self, module_name: str, action: str, reason: str):
        """
        Logs a sandbox violation.
        Does NOT raise exceptions — SandboxCore decides that.
        """

        entry = {
            "timestamp": int(time.time()),
            "module": module_name,
            "action": action,
            "reason": reason
        }

        filename = f"violation_{entry['timestamp']}.json"
        path = os.path.join(self.LOG_DIR, filename)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(entry, f, indent=2, ensure_ascii=False)

    # -------------------------------------------------------------

    def list_violations(self) -> list:
        """
        Returns a sorted list of all violation log files.
        """

        try:
            return sorted(os.listdir(self.LOG_DIR))
        except FileNotFoundError:
            return []

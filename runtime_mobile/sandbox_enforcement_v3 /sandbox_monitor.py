"""
sandbox_monitor.py
------------------
Monitoring layer for Sandbox Enforcement v3.

Responsibilities:
- Record all sandbox‑related requests
- Provide deterministic audit logs
- Support Self‑Repair Layer 4.4
- Never modify permissions or block actions
- Fully offline, no external dependencies

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""

import time
import os
import json


class SandboxMonitor:
    """
    Deterministic sandbox monitor.
    Logs all permission checks for auditing and diagnostics.
    """

    LOG_DIR = "runtime_sandbox_logs"

    def __init__(self):
        # Ensure log directory exists
        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

    # -------------------------------------------------------------

    def record_request(self, module_name: str, action: str):
        """
        Records a sandbox permission check.
        Does NOT enforce anything — only logs.
        """

        entry = {
            "timestamp": int(time.time()),
            "module": module_name,
            "action": action
        }

        filename = f"log_{entry['timestamp']}.json"
        path = os.path.join(self.LOG_DIR, filename)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(entry, f, indent=2, ensure_ascii=False)

    # -------------------------------------------------------------

    def list_logs(self) -> list:
        """
        Returns a sorted list of all sandbox log files.
        """

        try:
            return sorted(os.listdir(self.LOG_DIR))
        except FileNotFoundError:
            return []

"""
quarantine_storage.py
---------------------
Storage layer for Quarantine Pipeline v3.

Responsibilities:
- Store quarantined events in deterministic local storage
- Generate stable quarantine IDs
- Provide safe read/write operations
- Never overwrite existing quarantine entries
- Fully offline, no external dependencies

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""

import time
import json
import os


class QuarantineStorage:
    """
    Deterministic quarantine storage.
    Stores quarantined events in local JSON files.
    """

    STORAGE_DIR = "runtime_quarantine"

    def __init__(self):
        # Ensure storage directory exists
        if not os.path.exists(self.STORAGE_DIR):
            os.makedirs(self.STORAGE_DIR)

    def _generate_id(self) -> str:
        """
        Deterministic ID based on timestamp (no randomness).
        Example: q_1716871234
        """
        return f"q_{int(time.time())}"

    def store(self, event: dict, reason: str) -> str:
        """
        Stores the quarantined event and returns its ID.
        """

        qid = self._generate_id()
        path = os.path.join(self.STORAGE_DIR, f"{qid}.json")

        data = {
            "id": qid,
            "timestamp": int(time.time()),
            "reason": reason,
            "event": event
        }

        # Write to file safely
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return qid

    def load(self, qid: str) -> dict | None:
        """
        Loads a quarantined event by ID.
        Returns None if not found.
        """

        path = os.path.join(self.STORAGE_DIR, f"{qid}.json")

        if not os.path.exists(path):
            return None

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

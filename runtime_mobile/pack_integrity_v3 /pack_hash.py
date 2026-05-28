"""
pack_hash.py
------------
Deterministic hashing utility for Pack Integrity v3.

Responsibilities:
- Compute SHA256 hash of pack contents
- Ensure deterministic ordering
- Support Self‑Repair Layer 4.4
- Fully offline, no dynamic imports

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""

import hashlib
import json


class PackHash:
    """
    Deterministic SHA256 hashing for knowledge packs.
    """

    @staticmethod
    def hash_dict(data: dict) -> str:
        """
        Computes a deterministic SHA256 hash of a dictionary.
        Keys are sorted to ensure stable output.
        """

        normalized = json.dumps(data, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    @staticmethod
    def hash_bytes(data: bytes) -> str:
        """
        Computes SHA256 hash of raw bytes.
        """

        return hashlib.sha256(data).hexdigest()

    @staticmethod
    def hash_text(text: str) -> str:
        """
        Computes SHA256 hash of a UTF‑8 string.
        """

        return hashlib.sha256(text.encode("utf-8")).hexdigest()

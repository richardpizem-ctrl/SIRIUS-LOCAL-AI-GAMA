"""
pack_signature.py
-----------------
Signature verification module for Pack Integrity v3.

Responsibilities:
- Verify static signatures of knowledge packs
- Ensure deterministic, offline verification
- Support Self‑Repair Layer 4.4
- No dynamic imports, no external dependencies

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""

import hashlib
import json


class PackSignature:
    """
    Deterministic signature verification for knowledge packs.
    """

    @staticmethod
    def compute_signature(data: dict) -> str:
        """
        Computes a deterministic signature for a pack.
        Uses SHA256 over sorted JSON.
        """

        normalized = json.dumps(data, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    @staticmethod
    def verify_signature(data: dict, expected_signature: str) -> bool:
        """
        Verifies that the computed signature matches the expected one.
        """

        actual = PackSignature.compute_signature(data)
        return actual == expected_signature

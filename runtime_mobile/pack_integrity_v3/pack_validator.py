"""
pack_validator.py
-----------------
Validation module for Pack Integrity v3.

Responsibilities:
- Validate pack structure
- Validate required metadata
- Enforce deterministic rules
- Support Self‑Repair Layer 4.4
- Fully offline, no dynamic imports

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""


class PackValidator:
    """
    Validates the structure and metadata of knowledge packs.
    """

    REQUIRED_FIELDS = ["data", "meta"]
    REQUIRED_META = ["version", "type"]

    def validate_structure(self, pack: dict) -> dict:
        """
        Checks if pack contains required top-level fields.
        """

        if not isinstance(pack, dict):
            return {
                "valid": False,
                "error": "invalid_pack_type"
            }

        for field in self.REQUIRED_FIELDS:
            if field not in pack:
                return {
                    "valid": False,
                    "error": "missing_field",
                    "field": field
                }

        return {"valid": True}

    def validate_metadata(self, meta: dict) -> dict:
        """
        Checks if metadata contains required keys.
        """

        if not isinstance(meta, dict):
            return {
                "valid": False,
                "error": "invalid_meta_type"
            }

        for key in self.REQUIRED_META:
            if key not in meta:
                return {
                    "valid": False,
                    "error": "missing_meta_key",
                    "key": key
                }

        return {"valid": True}

    def validate(self, pack: dict) -> dict:
        """
        Performs full validation of a pack.
        """

        struct = self.validate_structure(pack)
        if not struct["valid"]:
            return struct

        meta = self.validate_metadata(pack["meta"])
        if not meta["valid"]:
            return meta

        return {"valid": True}

"""
fallback_normalizer.py

GAMA Runtime 3.4.0 – Fallback Normalization v3
Deterministic multi‑stage normalization pipeline with safe fallback logic.

This module:
- normalizes noisy SCHOOLWORK input (OCR/text)
- applies v3 normalization rules
- activates fallback paths when primary normalization fails
- guarantees deterministic output for reasoning engine

Rules:
- No raw OCR content stored internally.
- No dynamic imports.
- No randomness.
- 100% offline, safe for families and schools.
"""

from typing import Dict, Any

from .normalization_rules_v3 import apply_primary_rules_v3, apply_fallback_rules_v3
from .fallback_detector import needs_fallback_v3


class FallbackNormalizerV3:
    """
    Multi‑stage normalization pipeline:

        1) Primary normalization (rules v3)
        2) Fallback detection
        3) Fallback normalization (rules v3 fallback)
        4) Deterministic output

    Output is always:
        {
            "normalized_text": <string>,
            "normalization_meta": {
                "primary_applied": bool,
                "fallback_applied": bool,
                "fallback_reason": str | None
            }
        }
    """

    def normalize(self, raw_text: str) -> Dict[str, Any]:
        """
        Main entry point for normalization.

        raw_text:
            - OCR output
            - user‑typed text
            - mixed content
        """

        # 1) PRIMARY NORMALIZATION
        primary_output = apply_primary_rules_v3(raw_text)

        # 2) CHECK IF FALLBACK IS NEEDED
        if needs_fallback_v3(primary_output):
            fallback_output = apply_fallback_rules_v3(raw_text)

            return {
                "normalized_text": fallback_output,
                "normalization_meta": {
                    "primary_applied": True,
                    "fallback_applied": True,
                    "fallback_reason": "primary_normalization_insufficient",
                },
            }

        # 3) PRIMARY IS ENOUGH → NO FALLBACK
        return {
            "normalized_text": primary_output,
            "normalization_meta": {
                "primary_applied": True,
                "fallback_applied": False,
                "fallback_reason": None,
            },
        }


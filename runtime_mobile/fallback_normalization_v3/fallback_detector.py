"""
fallback_detector.py

GAMA Runtime 3.4.0 – Fallback Normalization v3
Deterministic detection logic for deciding when fallback normalization is required.

Rules:
- No randomness.
- No raw OCR/text stored.
- Only semantic/meta checks.
- Fully offline, safe for families and schools.
"""

from typing import Dict


def needs_fallback_v3(primary_output: str) -> bool:
    """
    Determines whether fallback normalization should be applied.

    Fallback is triggered when:
    - primary normalization leaves suspicious OCR artifacts
    - text still contains mixed-language math tokens
    - text contains non-ASCII characters
    - structure is still noisy after primary cleanup
    """

    if not primary_output:
        return False

    # 1) Non-ASCII characters → fallback required
    if any(ord(ch) > 127 for ch in primary_output):
        return True

    # 2) Suspicious OCR leftovers
    suspicious_tokens = ["□", "■", "●", "○", "✓", "✔", "✗", "✘"]
    if any(token in primary_output for token in suspicious_tokens):
        return True

    # 3) Mixed-language math tokens
    mixed_math = ["×", "÷", "·"]
    if any(token in primary_output for token in mixed_math):
        return True

    # 4) Excessive spacing or structural noise
    if "  " in primary_output:  # double spaces after primary normalization = anomaly
        return True

    return False

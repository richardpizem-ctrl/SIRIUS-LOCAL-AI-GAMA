"""
normalization_rules_v3.py

GAMA Runtime 3.4.0 – Fallback Normalization v3
Primary + fallback normalization rules for SCHOOLWORK reasoning.

Rules:
- No raw OCR/text stored internally.
- No dynamic imports.
- No randomness.
- Deterministic transformations only.
- 100% offline, safe for families and schools.
"""

from typing import List


# ---------------------------------------------------------
# PRIMARY NORMALIZATION RULES (v3)
# ---------------------------------------------------------

def apply_primary_rules_v3(text: str) -> str:
    """
    Applies deterministic primary normalization rules.

    These rules:
    - clean whitespace
    - normalize punctuation
    - fix common OCR artifacts
    - unify math symbols
    - remove invisible characters
    """

    if not text:
        return ""

    normalized = text

    # 1) Trim + collapse whitespace
    normalized = " ".join(normalized.split())

    # 2) Normalize punctuation
    replacements = {
        "–": "-",   # en dash
        "—": "-",   # em dash
        "−": "-",   # minus sign
        "•": "*",   # bullet to multiplication
        "×": "*",   # math multiply
        "÷": "/",   # division
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
    }
    for src, dst in replacements.items():
        normalized = normalized.replace(src, dst)

    # 3) Remove stray OCR artifacts
    ocr_noise: List[str] = ["□", "■", "●", "○", "✓", "✔", "✗", "✘"]
    for noise in ocr_noise:
        normalized = normalized.replace(noise, "")

    # 4) Normalize math spacing
    normalized = normalized.replace(" = ", "=").replace(" + ", "+").replace(" - ", "-")

    return normalized


# ---------------------------------------------------------
# FALLBACK NORMALIZATION RULES (v3)
# ---------------------------------------------------------

def apply_fallback_rules_v3(text: str) -> str:
    """
    Applies fallback normalization when primary rules are insufficient.

    Fallback rules:
    - aggressively collapse structure
    - remove leftover OCR noise
    - normalize mixed-language math tokens
    - enforce ASCII-safe output
    """

    if not text:
        return ""

    normalized = text

    # 1) Hard whitespace collapse
    normalized = " ".join(normalized.split())

    # 2) Remove any non-ASCII characters (safe fallback)
    normalized = "".join(ch for ch in normalized if ord(ch) < 128)

    # 3) Normalize math tokens again (fallback mode)
    fallback_math = {
        "x": "*",
        "X": "*",
        "·": "*",
        "÷": "/",
    }
    for src, dst in fallback_math.items():
        normalized = normalized.replace(src, dst)

    # 4) Remove leftover punctuation noise
    for noise in ["?", "!", "|", "~", "`"]:
        normalized = normalized.replace(noise, "")

    return normalized

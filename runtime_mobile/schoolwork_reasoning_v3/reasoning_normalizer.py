"""
reasoning_normalizer.py
-----------------------
Deterministic input normalizer for Schoolwork Reasoning Engine v3.

Responsibilities:
- Normalize raw schoolwork input (text, OCR, mixed)
- Remove noise, formatting artifacts, OCR glitches
- Standardize math expressions and language tasks
- Prepare clean input for ReasoningEngine
- Fully offline, deterministic, no dynamic imports

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""


class ReasoningNormalizer:
    """
    Normalizes raw schoolwork input into a clean, structured format.
    """

    def normalize(self, text: str) -> str:
        """
        Main normalization pipeline.
        """

        if not isinstance(text, str):
            return ""

        cleaned = text.strip()

        # Remove OCR artifacts
        cleaned = self._remove_ocr_noise(cleaned)

        # Normalize whitespace
        cleaned = self._normalize_whitespace(cleaned)

        # Normalize math symbols
        cleaned = self._normalize_math(cleaned)

        return cleaned

    def _remove_ocr_noise(self, text: str) -> str:
        """
        Removes common OCR artifacts.
        """

        replacements = {
            "§": "S",
            "©": "c",
            "0 ": "0",
            "  ": " ",
            "|": "l",
            "¬": "-",
        }

        for bad, good in replacements.items():
            text = text.replace(bad, good)

        return text

    def _normalize_whitespace(self, text: str) -> str:
        """
        Collapses excessive whitespace.
        """

        while "  " in text:
            text = text.replace("  ", " ")

        return text.strip()

    def _normalize_math(self, text: str) -> str:
        """
        Normalizes math expressions into a consistent form.
        """

        replacements = {
            "×": "*",
            "·": "*",
            "÷": "/",
            "−": "-",
            "—": "-",
            "–": "-",
            ",": ".",
        }

        for bad, good in replacements.items():
            text = text.replace(bad, good)

        return text

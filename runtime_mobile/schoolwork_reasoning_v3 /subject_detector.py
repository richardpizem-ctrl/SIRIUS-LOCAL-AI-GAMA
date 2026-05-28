"""
subject_detector.py
-------------------
Subject detection module for Schoolwork Reasoning Engine v3.

Responsibilities:
- Detect the subject of a schoolwork task (math, language, science, general)
- Use deterministic keyword-based classification
- Fully offline, no ML models, no dynamic imports
- Compatible with Schoolwork Mode 3.0 and Self‑Repair Layer 4.4

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""


class SubjectDetector:
    """
    Deterministic subject classifier for schoolwork tasks.
    """

    MATH_KEYWORDS = [
        "+", "-", "*", "/", "=", "x", "y", "z",
        "rovnica", "vypočítaj", "výsledok", "percentá",
        "uhol", "trojuholník", "obsah", "objem"
    ]

    LANGUAGE_KEYWORDS = [
        "vetu", "slovný druh", "podmet", "prísudok",
        "gramatika", "pravopis", "vyčasuj", "vysvetli význam"
    ]

    SCIENCE_KEYWORDS = [
        "fyzika", "chémia", "biológia", "reakcia",
        "energia", "sila", "teplota", "tlak",
        "rastlina", "živočích", "prvok", "molekula"
    ]

    def detect(self, text: str) -> str:
        """
        Detects the subject of the task based on keywords.
        Returns one of:
        - "math"
        - "language"
        - "science"
        - "general"
        """

        if not isinstance(text, str):
            return "general"

        lower = text.lower()

        # Math detection
        for kw in self.MATH_KEYWORDS:
            if kw in lower:
                return "math"

        # Language detection
        for kw in self.LANGUAGE_KEYWORDS:
            if kw in lower:
                return "language"

        # Science detection
        for kw in self.SCIENCE_KEYWORDS:
            if kw in lower:
                return "science"

        # Default fallback
        return "general"

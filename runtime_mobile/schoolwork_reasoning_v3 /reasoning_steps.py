"""
reasoning_steps.py
------------------
Deterministic step-by-step reasoning builder for Schoolwork Reasoning Engine v3.

Responsibilities:
- Build structured reasoning steps
- Ensure deterministic ordering
- Provide safe, offline educational explanations
- Used by ReasoningEngine and ExplanationGenerator
- Fully compatible with Schoolwork Mode 3.0 and Self‑Repair Layer 4.4

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""


class ReasoningSteps:
    """
    Utility class for constructing step-by-step reasoning sequences.
    """

    def __init__(self):
        self.steps = []

    def add(self, text: str):
        """
        Adds a reasoning step.
        """
        if isinstance(text, str) and text.strip():
            self.steps.append(text.strip())

    def extend(self, items: list):
        """
        Adds multiple reasoning steps at once.
        """
        for item in items:
            self.add(item)

    def build(self) -> list:
        """
        Returns the final list of reasoning steps.
        """
        return list(self.steps)

    def clear(self):
        """
        Clears all stored steps.
        """
        self.steps = []

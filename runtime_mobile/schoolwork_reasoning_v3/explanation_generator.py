"""
explanation_generator.py
------------------------
Generates final student-friendly explanations for Schoolwork Reasoning Engine v3.

Responsibilities:
- Convert reasoning steps into natural-language explanation
- Ensure safe, offline, deterministic output
- Avoid hallucinations and unsupported claims
- Provide simple, educational explanations
- Compatible with Schoolwork Mode 3.0 and Self‑Repair Layer 4.4

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""


class ExplanationGenerator:
    """
    Builds final explanation text from reasoning steps.
    """

    def generate(self, subject: str, steps: list) -> str:
        """
        Creates a readable explanation for the student.
        """

        if not isinstance(steps, list) or len(steps) == 0:
            return "No explanation available."

        intro = self._intro(subject)
        body = self._steps_to_text(steps)
        outro = self._outro(subject)

        return f"{intro}\n\n{body}\n\n{outro}"

    def _intro(self, subject: str) -> str:
        """
        Subject-specific introduction.
        """

        if subject == "math":
            return "Let's solve this math problem step by step."
        if subject == "language":
            return "Let's analyze this language task clearly."
        if subject == "science":
            return "Let's understand this science question logically."

        return "Let's go through this task step by step."

    def _steps_to_text(self, steps: list) -> str:
        """
        Converts reasoning steps into readable text.
        """

        lines = []
        for i, step in enumerate(steps, start=1):
            lines.append(f"{i}. {step}")

        return "\n".join(lines)

    def _outro(self, subject: str) -> str:
        """
        Subject-specific closing message.
        """

        if subject == "math":
            return "This is how we reach the final result."
        if subject == "language":
            return "This is how we understand the structure of the sentence."
        if subject == "science":
            return "This is how the scientific principle applies here."

        return "This is the complete reasoning for the task."

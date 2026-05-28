"""
knowledge_pack_integrator.py
----------------------------
Knowledge Pack integration module for Schoolwork Reasoning Engine v3.

Responsibilities:
- Load subject-specific knowledge packs
- Provide deterministic fallback packs
- Ensure offline, safe, predictable behavior
- No dynamic imports, no external dependencies

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""


class KnowledgePackIntegrator:
    """
    Loads and provides knowledge pack data for reasoning.
    """

    DEFAULT_PACK = {
        "rules": [
            "Apply logical reasoning.",
            "Break the problem into smaller steps.",
            "Check the final answer for consistency."
        ]
    }

    MATH_PACK = {
        "rules": [
            "Identify known and unknown values.",
            "Select the correct mathematical operation.",
            "Substitute values into the formula.",
            "Compute step-by-step without skipping.",
            "Verify the result by reversing the operation."
        ]
    }

    LANGUAGE_PACK = {
        "rules": [
            "Identify the type of sentence.",
            "Locate subject and predicate.",
            "Check grammar and spelling.",
            "Apply language rules from curriculum."
        ]
    }

    SCIENCE_PACK = {
        "rules": [
            "Identify the scientific principle involved.",
            "Recall relevant definitions or laws.",
            "Apply the principle to the given scenario.",
            "Explain the reasoning in simple terms."
        ]
    }

    def load(self, subject: str) -> dict:
        """
        Returns the knowledge pack for the given subject.
        """

        if subject == "math":
            return self.MATH_PACK

        if subject == "language":
            return self.LANGUAGE_PACK

        if subject == "science":
            return self.SCIENCE_PACK

        # Fallback for general tasks
        return self.DEFAULT_PACK

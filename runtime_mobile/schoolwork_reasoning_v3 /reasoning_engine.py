"""
reasoning_engine.py
-------------------
Core deterministic reasoning engine for Schoolwork Reasoning v3.

Responsibilities:
- Receive normalized schoolwork input
- Detect subject type
- Apply deterministic reasoning rules
- Build step-by-step reasoning
- Integrate knowledge packs
- Produce structured reasoning output

This module is part of SIRIUS Mobile Runtime 3.3.0.
"""

from .reasoning_normalizer import ReasoningNormalizer
from .reasoning_steps import ReasoningSteps
from .subject_detector import SubjectDetector
from .knowledge_pack_integrator import KnowledgePackIntegrator
from .explanation_generator import ExplanationGenerator


class ReasoningEngine:
    """
    Main reasoning engine for schoolwork tasks.
    """

    def __init__(self):
        self.normalizer = ReasoningNormalizer()
        self.detector = SubjectDetector()
        self.integrator = KnowledgePackIntegrator()
        self.explainer = ExplanationGenerator()

    def process(self, raw_text: str) -> dict:
        """
        Full reasoning pipeline.
        """

        # Step 1: Normalize input
        normalized = self.normalizer.normalize(raw_text)

        # Step 2: Detect subject
        subject = self.detector.detect(normalized)

        # Step 3: Integrate knowledge packs
        pack_data = self.integrator.load(subject)

        # Step 4: Build reasoning steps
        steps = ReasoningSteps()

        # Subject-specific reasoning
        self._apply_reasoning(subject, normalized, steps, pack_data)

        # Step 5: Generate explanation
        explanation = self.explainer.generate(subject, steps.build())

        return {
            "subject": subject,
            "normalized": normalized,
            "steps": steps.build(),
            "explanation": explanation
        }

    def _apply_reasoning(self, subject: str, text: str, steps: ReasoningSteps, pack_data: dict):
        """
        Applies deterministic reasoning rules based on subject.
        """

        if subject == "math":
            steps.add("Identifying mathematical structure in the problem.")
            steps.add("Applying math reasoning rules from knowledge pack.")
            steps.extend(pack_data.get("rules", []))

        elif subject == "language":
            steps.add("Analyzing sentence structure.")
            steps.add("Applying grammar rules from knowledge pack.")

        elif subject == "science":
            steps.add("Identifying scientific concepts.")
            steps.add("Applying domain-specific rules from knowledge pack.")

        else:
            steps.add("General reasoning applied.")
            steps.add("Using fallback educational rules.")

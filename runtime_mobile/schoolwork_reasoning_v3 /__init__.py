"""
schoolwork_reasoning_v3
-----------------------
Schoolwork Reasoning Engine for SIRIUS Mobile Runtime 3.3.0.

Responsibilities:
- Normalize schoolwork inputs (text + OCR)
- Detect subject type (math, language, science, general)
- Apply deterministic reasoning rules
- Integrate Knowledge Packs
- Produce step-by-step explanations
- Provide safe, offline educational output

Modules included:
- SubjectDetector
- ProblemNormalizer
- ReasoningEngine
- KnowledgePackIntegrator
- ExplanationGenerator
- OutputFormatter
- DiagnosticsLogger
"""

from .subject_detector import SubjectDetector
from .problem_normalizer import ProblemNormalizer
from .reasoning_engine import ReasoningEngine
from .knowledge_pack_integrator import KnowledgePackIntegrator
from .explanation_generator import ExplanationGenerator
from .output_formatter import OutputFormatter
from .diagnostics_logger import DiagnosticsLogger

__all__ = [
    "SubjectDetector",
    "ProblemNormalizer",
    "ReasoningEngine",
    "KnowledgePackIntegrator",
    "ExplanationGenerator",
    "OutputFormatter",
    "DiagnosticsLogger",
]

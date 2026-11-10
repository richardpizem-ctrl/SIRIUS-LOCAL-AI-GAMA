"""
vision_deterministic_flow_v3
----------------------------
Deterministic Vision Flow module for SIRIUS Mobile Runtime 3.3.0.

Responsibilities:
- Provide a fully deterministic processing pipeline for vision tasks
- Enforce strict, predictable execution order
- Integrate with Vision Engine and Runtime Core
- Avoid nondeterministic operations (no randomness, no async drift)
- Support Self‑Repair Layer 4.4

This package is fully deterministic:
- No dynamic imports
- No reflection
- No eval/exec
"""

from .vision_router import VisionRouter
from .vision_sanitizer import VisionSanitizer
from .vision_flow import VisionFlow

__all__ = [
    "VisionRouter",
    "VisionSanitizer",
    "VisionFlow",
]

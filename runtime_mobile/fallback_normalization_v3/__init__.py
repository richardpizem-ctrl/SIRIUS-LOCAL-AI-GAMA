"""
fallback_normalization_v3

GAMA Runtime 3.4.0 – Fallback Normalization v3
Deterministic multi-stage normalization with safe fallback logic.

Exports:
- FallbackNormalizerV3
- apply_primary_rules_v3
- apply_fallback_rules_v3
- needs_fallback_v3
"""

from .fallback_normalizer import FallbackNormalizerV3
from .normalization_rules_v3 import apply_primary_rules_v3, apply_fallback_rules_v3
from .fallback_detector import needs_fallback_v3

__all__ = [
    "FallbackNormalizerV3",
    "apply_primary_rules_v3",
    "apply_fallback_rules_v3",
    "needs_fallback_v3",
]

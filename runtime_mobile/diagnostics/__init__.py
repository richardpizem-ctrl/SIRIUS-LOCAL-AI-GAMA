# ============================================================
# SIRIUS LOCAL AI GAMA - Diagnostics Package
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for GAMA Runtime 3.1:
# - Unified diagnostics API
# - Diagnostics v3 hooks
# - Consistent package export
# ============================================================

from .diagnostics import MobileDiagnostics

__all__ = [
    "MobileDiagnostics",
]

# ============================================================
# SIRIUS LOCAL AI GAMA - Pack Manager Package
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for GAMA Runtime 3.1:
# - Unified pack manager export
# - Compatible with PackManager v3.1
# - Consistent metadata header
# ============================================================

from .pack_manager import MobilePackManager

__all__ = [
    "MobilePackManager",
]

# ============================================================
# SIRIUS LOCAL AI GAMA - Knowledge Packs Package
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Public API for mobile knowledge packs subsystem.
# Updated for GAMA Runtime 3.1:
# - unified export surface
# - metadata v3 compatibility
# - PackManager 3.1 + MobileKnowledgePacks 3.1
# ============================================================

from .packs_mobile import MobileKnowledgePacks

__all__ = [
    "MobileKnowledgePacks",
]

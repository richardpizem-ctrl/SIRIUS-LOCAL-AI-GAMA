# ============================================================
# SIRIUS LOCAL AI GAMA - Knowledge Packs Package
# Version: 3.0.0-pre
# ============================================================

"""
Knowledge Packs package initializer.

Exposes:
- PackManager: core loader and validator for knowledge packs
- MobileKnowledgePacks: high-level interface used by runtime modules
"""

from .pack_manager.pack_manager import PackManager
from .packs_mobile import MobileKnowledgePacks

__all__ = [
    "PackManager",
    "MobileKnowledgePacks",
]


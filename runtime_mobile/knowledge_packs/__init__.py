# ============================================================
# SIRIUS LOCAL AI GAMA - Knowledge Packs Package
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Exposes:
# - PackManager: core loader, validator and metadata processor
# - MobileKnowledgePacks: high-level runtime interface
#
# Updated for GAMA Runtime 3.1:
# - metadata v3 support
# - pack_id / checksum / entries_count compatibility
# - unified import surface
# ============================================================

from .pack_manager.pack_manager import PackManager
from .packs_mobile import MobileKnowledgePacks

__all__ = [
    "PackManager",
    "MobileKnowledgePacks",
]

# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Modules Package
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Public API surface for all mobile modules.
# ============================================================

# Core base module
from runtime_mobile.modules.base_module import BaseModule

# Knowledge system
from runtime_mobile.modules.knowledge_module import KnowledgeModule
from runtime_mobile.knowledge_packs.packs_mobile import MobileKnowledgePacks
from runtime_mobile.pack_manager import MobilePackManager

# Security system
from runtime_mobile.modules.security_module import SecurityModule

# Vision system
from runtime_mobile.modules.vision_module import VisionModule

# Diagnostics
from runtime_mobile.diagnostics.diagnostics_entry import MobileDiagnostics

__all__ = [
    "BaseModule",
    "KnowledgeModule",
    "MobileKnowledgePacks",
    "MobilePackManager",
    "SecurityModule",
    "VisionModule",
    "MobileDiagnostics",
]

MODULES_VERSION = "3.0.0-pre"

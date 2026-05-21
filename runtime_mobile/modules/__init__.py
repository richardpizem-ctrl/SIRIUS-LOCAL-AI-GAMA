# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Modules Package
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Public API surface for all mobile runtime modules.
# Updated for GAMA Runtime 3.1:
# - unified module exports
# - diagnostics v3 compatibility
# - consistent metadata header
# ============================================================

# Core base module
from runtime_mobile.modules.base_module import BaseModule

# Knowledge system
from runtime_mobile.modules.knowledge_module import KnowledgeModule

# Security system
from runtime_mobile.modules.security_module import SecurityModule

# Vision system
from runtime_mobile.modules.vision_module import VisionModule

# Diagnostics v3
from runtime_mobile.diagnostics.diagnostics_entry import MobileDiagnostics

__all__ = [
    "BaseModule",
    "KnowledgeModule",
    "SecurityModule",
    "VisionModule",
    "MobileDiagnostics",
]

MODULES_VERSION = "3.1.0"

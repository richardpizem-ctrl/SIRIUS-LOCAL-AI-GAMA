# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Modules Package
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Public API surface for all mobile modules.
# Every mobile module should be imported via this package.
#
# Example:
#   from runtime_mobile.modules import (
#       BaseModule,
#       KnowledgeModule,
#       SecurityModule,
#       VisionModule,
#   )
# ============================================================

from runtime_mobile.modules.base_module import BaseModule
from runtime_mobile.modules.knowledge_module import KnowledgeModule
from runtime_mobile.modules.security_module import SecurityModule
from runtime_mobile.modules.vision_module import VisionModule

__all__ = [
    "BaseModule",
    "KnowledgeModule",
    "SecurityModule",
    "VisionModule",
]

MODULES_VERSION = "3.0.0-pre"


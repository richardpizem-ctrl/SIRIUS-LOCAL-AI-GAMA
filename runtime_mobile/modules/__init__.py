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
from runtime_mobile.knowledge.knowledge_module import KnowledgeModule
from runtime_mobile.knowledge_packs.packs_mobile import MobileKnowledgePacks
from runtime_mobile.knowledge_packs.pack_manager.pack_manager import PackManager

# Security system
from runtime_mobile.security.security_module import SecurityModule

# Vision system
from runtime_mobile.vision.vision_module import VisionModule

# Diagnostics
from runtime_mobile.diagnostics.diagnostics import MobileDiagnostics

# Optional modules (future)
# from runtime_mobile.workflow.workflow_module import WorkflowModule
# from runtime_mobile.lan.lan_bridge import LanBridgeModule
# from runtime_mobile.governor.energy_governor import EnergyGovernorModule

__all__ = [
    "BaseModule",
    "KnowledgeModule",
    "MobileKnowledgePacks",
    "PackManager",
    "SecurityModule",
    "VisionModule",
    "MobileDiagnostics",
]

MODULES_VERSION = "3.0.0-pre"

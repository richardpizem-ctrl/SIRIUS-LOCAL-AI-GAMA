# ============================================================
# SIRIUS LOCAL AI GAMA - Vision Module
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# GAMA Mobile Vision subsystem.
#
# Provides:
# - Vision entry point for mobile runtime
# - Integration hooks for the Vision Engine
# - Framework-agnostic interface for camera/image-based features
# - Metadata v3 for diagnostics and runtime introspection
# ============================================================

VISION_VERSION = "3.1.0"

from .vision_entry import VisionEntry

__all__ = [
    "VISION_VERSION",
    "VisionEntry",
]

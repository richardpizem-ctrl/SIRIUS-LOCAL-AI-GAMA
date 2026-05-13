# ============================================================
# SIRIUS LOCAL AI GAMA - Vision Module
# Version: 3.0.0-pre
# ============================================================

"""
GAMA Mobile Vision subsystem.

Provides:
- Vision entry point for mobile runtime
- Integration hooks for the Vision Engine
- Framework-agnostic interface for camera/image-based features
"""

VISION_VERSION = "3.0.0-pre"

from .vision_entry import VisionEntry

__all__ = [
    "VISION_VERSION",
    "VisionEntry",
]


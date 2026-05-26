"""
SIRIUS LOCAL AI GAMA – Vision Engine Package
Version: 3.2.0

Exports:
- VisionEngineV3 (main engine)
- vision_analyze_v2 (SCENE/DETECT/HOMEWORK/OCR)
- schoolwork_ocr_v2 (homework OCR v2)
"""

from .vision_engine_v3 import VisionEngineV3
from .vision_analyze_v2 import analyze as analyze_v2
from .schoolwork_ocr_v2 import run as schoolwork_ocr_v2

__all__ = [
    "VisionEngineV3",
    "analyze_v2",
    "schoolwork_ocr_v2",
]

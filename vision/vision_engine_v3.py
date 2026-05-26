"""
SIRIUS LOCAL AI GAMA – Vision Engine v3
Mobile Runtime 3.2.0

This module unifies:
- Vision Analyze v2
- Schoolwork OCR v2

It provides a clean engine interface for VisionEntry.
"""

from .vision_analyze_v2 import analyze as analyze_v2
from .schoolwork_ocr_v2 import run as schoolwork_ocr_v2


VISION_ENGINE_VERSION = "3.2.0"


class VisionEngineV3:
    """
    Unified Vision Engine for Mobile Runtime 3.2.0.
    """

    def __init__(self):
        self.version = VISION_ENGINE_VERSION

    # ---------------------------------------------------------
    # SCENE / DETECT / HOMEWORK / OCR
    # ---------------------------------------------------------

    def analyze(self, image):
        """
        SCENE v2 analysis.
        """
        return analyze_v2(image, mode="SCENE")

    def detect(self, image):
        """
        DETECT v2 object extraction.
        """
        return analyze_v2(image, mode="DETECT")

    def homework(self, image):
        """
        HOMEWORK v2 classification.
        """
        return analyze_v2(image, mode="HOMEWORK")

    def ocr(self, image):
        """
        OCR v2 text extraction.
        """
        return schoolwork_ocr_v2(image, mode="OCR")

    # ---------------------------------------------------------
    # Metadata
    # ---------------------------------------------------------

    def get_info(self):
        return {
            "engine": "VisionEngineV3",
            "version": self.version,
            "supports": ["SCENE", "DETECT", "HOMEWORK", "OCR"],
        }

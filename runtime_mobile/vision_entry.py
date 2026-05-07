# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Vision Entry
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Entry point for mobile OCR and vision processing.
# Supports:
#   - OCR
#   - Object detection
#   - Scene analysis
#   - Homework mode (math/text extraction)
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes


class MobileVisionEntry:
    """
    Entry point for mobile OCR and vision processing.
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def handle_event(self, event):
        image = event.get("image")

        if image is None:
            return {
                "status": "error",
                "reason": "no_image"
            }

        etype = event.type

        # --------------------------------------------------------
        # OCR
        # --------------------------------------------------------
        if etype == MobileEventTypes.OCR:
            try:
                text = self.context.vision_engine.ocr(image)
            except Exception as e:
                return {"status": "error", "reason": "ocr_failed", "error": str(e)}

            return {
                "status": "ok",
                "type": "ocr_result",
                "text": text
            }

        # --------------------------------------------------------
        # Object Detection
        # --------------------------------------------------------
        if etype == MobileEventTypes.DETECT:
            try:
                objects = self.context.vision_engine.detect(image)
            except Exception as e:
                return {"status": "error", "reason": "detect_failed", "error": str(e)}

            return {
                "status": "ok",
                "type": "detection_result",
                "objects": objects
            }

        # --------------------------------------------------------
        # Scene Analysis
        # --------------------------------------------------------
        if etype == MobileEventTypes.SCENE:
            try:
                analysis = self.context.vision_engine.analyze(image)
            except Exception as e:
                return {"status": "error", "reason": "scene_failed", "error": str(e)}

            return {
                "status": "ok",
                "type": "scene_result",
                "analysis": analysis
            }

        # --------------------------------------------------------
        # Homework Mode
        # --------------------------------------------------------
        if etype == MobileEventTypes.HOMEWORK:
            try:
                solution = self.context.vision_engine.homework(image)
            except Exception as e:
                return {"status": "error", "reason": "homework_failed", "error": str(e)}

            return {
                "status": "ok",
                "type": "homework_result",
                "solution": solution
            }

        # --------------------------------------------------------
        # Unknown
        # --------------------------------------------------------
        return {
            "status": "ignored",
            "reason": "unknown_vision_event",
            "event_type": etype
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "module": "vision",
            "version": self.MODULE_VERSION,
            "engine_attached": hasattr(self.context, "vision_engine")
        }

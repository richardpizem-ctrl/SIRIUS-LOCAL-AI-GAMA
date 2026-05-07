# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Vision Entry
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Entry point for the mobile vision module.
# Responsibilities:
#   - OCR
#   - object detection
#   - scene analysis
#   - homework mode (math/text extraction)
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes


class MobileVisionEntry:
    """
    Entry point for the mobile vision module.
    Handles OCR, image preprocessing and visual event interpretation.
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def handle_event(self, event):
        """
        Main processing method for vision events.
        """

        et = event.type

        if et == MobileEventTypes.OCR:
            return self._run_ocr(event)

        if et == MobileEventTypes.DETECT:
            return self._detect_objects(event)

        if et == MobileEventTypes.SCENE:
            return self._analyze_scene(event)

        if et == MobileEventTypes.HOMEWORK:
            return self._homework_mode(event)

        return {
            "status": "ignored",
            "reason": "unknown_event",
            "event_type": et
        }

    # ------------------------------------------------------------
    # OCR
    # ------------------------------------------------------------

    def _run_ocr(self, event):
        image = event.get("image")

        if not image:
            return {"status": "error", "reason": "no_image"}

        try:
            text = self.context.vision_engine.ocr(image)
        except Exception as e:
            return {"status": "error", "reason": "ocr_failed", "error": str(e)}

        return {
            "status": "ok",
            "type": "ocr_result",
            "text": text
        }

    # ------------------------------------------------------------
    # Object Detection
    # ------------------------------------------------------------

    def _detect_objects(self, event):
        image = event.get("image")

        if not image:
            return {"status": "error", "reason": "no_image"}

        try:
            result = self.context.vision_engine.detect(image)
        except Exception as e:
            return {"status": "error", "reason": "detect_failed", "error": str(e)}

        return {
            "status": "ok",
            "type": "detection_result",
            "objects": result
        }

    # ------------------------------------------------------------
    # Scene Analysis
    # ------------------------------------------------------------

    def _analyze_scene(self, event):
        image = event.get("image")

        if not image:
            return {"status": "error", "reason": "no_image"}

        try:
            result = self.context.vision_engine.analyze(image)
        except Exception as e:
            return {"status": "error", "reason": "scene_failed", "error": str(e)}

        return {
            "status": "ok",
            "type": "scene_result",
            "analysis": result
        }

    # ------------------------------------------------------------
    # Homework Mode (GAMA Schoolwork Mode)
    # ------------------------------------------------------------

    def _homework_mode(self, event):
        image = event.get("image")

        if not image:
            return {"status": "error", "reason": "no_image"}

        try:
            result = self.context.vision_engine.homework(image)
        except Exception as e:
            return {"status": "error", "reason": "homework_failed", "error": str(e)}

        return {
            "status": "ok",
            "type": "homework_result",
            "solution": result
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

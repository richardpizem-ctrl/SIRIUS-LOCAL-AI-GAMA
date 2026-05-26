# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Vision Entry
# Version: 3.2.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes
from vision.vision_engine_v3 import VisionEngineV3


class VisionEntry:
    """
    Entry point for the mobile vision module.
    Handles OCR, object detection, scene analysis and homework mode.
    """

    MODULE_VERSION = "3.2.0"

    def __init__(self, context):
        self.context = context
        self.engine = VisionEngineV3()   # ← NEW ENGINE

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _get_image(self, event):
        image = event.image if hasattr(event, "image") else event.get("image")
        if image is None:
            return None, {"status": "error", "reason": "no_image"}
        return image, None

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def on_event(self, event):
        etype = event.type if hasattr(event, "type") else event.get("type")

        if etype == MobileEventTypes.OCR:
            return self._run_ocr(event)

        if etype == MobileEventTypes.DETECT:
            return self._detect_objects(event)

        if etype == MobileEventTypes.SCENE:
            return self._analyze_scene(event)

        if etype == MobileEventTypes.HOMEWORK:
            return self._homework_mode(event)

        return {
            "status": "ignored",
            "reason": "unknown_event",
            "event_type": etype
        }

    # ------------------------------------------------------------
    # OCR
    # ------------------------------------------------------------

    def _run_ocr(self, event):
        image, err = self._get_image(event)
        if err:
            return err

        try:
            result = self.engine.ocr(image)
        except Exception as e:
            return {"status": "error", "reason": "ocr_failed", "error": str(e)}

        return {
            "status": "ok",
            "type": "ocr_result",
            "text": result.get("text", "")
        }

    # ------------------------------------------------------------
    # Object Detection
    # ------------------------------------------------------------

    def _detect_objects(self, event):
        image, err = self._get_image(event)
        if err:
            return err

        try:
            result = self.engine.detect(image)
        except Exception as e:
            return {"status": "error", "reason": "detect_failed", "error": str(e)}

        return {
            "status": "ok",
            "type": "detection_result",
            "objects": result.get("objects", [])
        }

    # ------------------------------------------------------------
    # Scene Analysis
    # ------------------------------------------------------------

    def _analyze_scene(self, event):
        image, err = self._get_image(event)
        if err:
            return err

        try:
            result = self.engine.analyze(image)
        except Exception as e:
            return {"status": "error", "reason": "scene_failed", "error": str(e)}

        return {
            "status": "ok",
            "type": "scene_result",
            "analysis": result
        }

    # ------------------------------------------------------------
    # Homework Mode
    # ------------------------------------------------------------

    def _homework_mode(self, event):
        image, err = self._get_image(event)
        if err:
            return err

        try:
            result = self.engine.homework(image)
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
            "engine": self.engine.get_info(),
            "supported_events": [
                MobileEventTypes.OCR,
                MobileEventTypes.DETECT,
                MobileEventTypes.SCENE,
                MobileEventTypes.HOMEWORK,
            ],
        }

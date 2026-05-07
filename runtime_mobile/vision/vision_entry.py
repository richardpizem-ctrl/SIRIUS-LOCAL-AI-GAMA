# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Vision Entry
# Version: 3.0.0-pre
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes


class MobileVisionEntry:
    """
    Entry point for the mobile vision module.
    Handles OCR, object detection, scene analysis and homework mode.
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main Event Handler (required by runtime)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Unified event handler for the runtime dispatcher.
        Supports both MobileEvent and dict events.
        """

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
        image = event.image if hasattr(event, "image") else event.get("image")

        if image is None:
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
        image = event.image if hasattr(event, "image") else event.get("image")

        if image is None:
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
        image = event.image if hasattr(event, "image") else event.get("image")

        if image is None:
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
    # Homework Mode
    # ------------------------------------------------------------

    def _homework_mode(self, event):
        image = event.image if hasattr(event, "image") else event.get("image")

        if image is None:
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

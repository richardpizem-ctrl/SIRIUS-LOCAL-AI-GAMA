# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Vision Entry
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes


class MobileVisionEntry:
    """
    Entry point for mobile OCR and vision processing.
    Handles:
    - OCR
    - Object detection
    - Scene analysis
    - ANALYZE alias
    - Homework mode
    """

    MODULE_VERSION = "3.1.0"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _get_image(self, event):
        """Extract image from MobileEvent or dict event."""
        image = getattr(event, "image", None)
        if image is None and isinstance(event, dict):
            image = event.get("image")

        if image is None:
            return None, {"status": "error", "reason": "no_image"}

        return image, None

    def _get_engine(self):
        """Ensure vision engine is attached."""
        engine = getattr(self.context, "vision_engine", None)
        if engine is None:
            return None, {"status": "error", "reason": "vision_engine_missing"}
        return engine, None

    # ------------------------------------------------------------
    # Main Event Handler
    # ------------------------------------------------------------

    def on_event(self, event):
        etype = getattr(event, "type", None)
        if etype is None and isinstance(event, dict):
            etype = event.get("type")

        if etype is None:
            return {"status": "error", "reason": "invalid_event"}

        image, err = self._get_image(event)
        if err:
            return err

        engine, err = self._get_engine()
        if err:
            return err

        # --------------------------------------------------------
        # OCR
        # --------------------------------------------------------
        if etype == MobileEventTypes.OCR:
            try:
                text = engine.ocr(image)
                return {"status": "ok", "type": "ocr_result", "text": text}
            except Exception as e:
                return {"status": "error", "reason": "ocr_failed", "error": str(e)}

        # --------------------------------------------------------
        # Object Detection
        # --------------------------------------------------------
        if etype == MobileEventTypes.DETECT:
            try:
                objects = engine.detect(image)
                return {"status": "ok", "type": "detection_result", "objects": objects}
            except Exception as e:
                return {"status": "error", "reason": "detect_failed", "error": str(e)}

        # --------------------------------------------------------
        # Scene Analysis
        # --------------------------------------------------------
        if etype == MobileEventTypes.SCENE:
            try:
                analysis = engine.analyze(image)
                return {"status": "ok", "type": "scene_result", "analysis": analysis}
            except Exception as e:
                return {"status": "error", "reason": "scene_failed", "error": str(e)}

        # --------------------------------------------------------
        # ANALYZE (alias for SCENE)
        # --------------------------------------------------------
        if etype == MobileEventTypes.ANALYZE:
            try:
                analysis = engine.analyze(image)
                return {"status": "ok", "type": "analysis_result", "analysis": analysis}
            except Exception as e:
                return {"status": "error", "reason": "analyze_failed", "error": str(e)}

        # --------------------------------------------------------
        # Homework Mode
        # --------------------------------------------------------
        if etype == MobileEventTypes.HOMEWORK:
            try:
                solution = engine.homework(image)
                return {"status": "ok", "type": "homework_result", "solution": solution}
            except Exception as e:
                return {"status": "error", "reason": "homework_failed", "error": str(e)}

        # --------------------------------------------------------
        # Unknown Vision Event
        # --------------------------------------------------------
        return {
            "status": "ignored",
            "reason": "unknown_vision_event",
            "event_type": etype,
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "module": "vision",
            "version": self.MODULE_VERSION,
            "engine_attached": hasattr(self.context, "vision_engine"),
            "supported_events": [
                MobileEventTypes.OCR,
                MobileEventTypes.DETECT,
                MobileEventTypes.SCENE,
                MobileEventTypes.ANALYZE,
                MobileEventTypes.HOMEWORK,
            ],
        }

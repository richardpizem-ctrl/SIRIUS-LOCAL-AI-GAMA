# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Vision Entry
# Version: 3.0.0-pre
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
    # Main Event Handler (required by runtime)
    # ------------------------------------------------------------

    def on_event(self, event):
        # Support both MobileEvent and dict events
        etype = event.type if hasattr(event, "type") else event.get("type")
        image = event.image if hasattr(event, "image") else event.get("image")

        if image is None:
            return {"status": "error", "reason": "no_image"}

        # --------------------------------------------------------
        # OCR
        # --------------------------------------------------------
        if etype == MobileEventTypes.OCR:
            try:
                text = self.context.vision_engine.ocr(image)
            except Exception as e:
                return {"status": "error", "reason": "ocr_failed", "error": str(e)}

            return {"status": "ok", "type": "ocr_result", "text": text}

        # --------------------------------------------------------
        # Object Detection
        # --------------------------------------------------------
        if etype == MobileEventTypes.DETECT:
            try:
                objects = self.context.vision_engine.detect(image)
            except Exception as e:
                return {"status": "error", "reason": "detect_failed", "error": str(e)}

            return {"status": "ok", "type": "detection_result", "objects": objects}

        # --------------------------------------------------------
        # Scene Analysis
        # --------------------------------------------------------
        if etype == MobileEventTypes.SCENE:
            try:
                analysis = self.context.vision_engine.analyze(image)
            except Exception as e:
                return {"status": "error", "reason": "scene_failed", "error": str(e)}

            return {"status": "ok", "type": "scene_result", "analysis": analysis}

        # --------------------------------------------------------
        # ANALYZE (alias for SCENE)
        # --------------------------------------------------------
        if etype == MobileEventTypes.ANALYZE:
            try:
                analysis = self.context.vision_engine.analyze(image)
            except Exception as e:
                return {"status": "error", "reason": "analyze_failed", "error": str(e)}

            return {"status": "ok", "type": "analysis_result", "analysis": analysis}

        # --------------------------------------------------------
        # Homework Mode
        # --------------------------------------------------------
        if etype == MobileEventTypes.HOMEWORK:
            try:
                solution = self.context.vision_engine.homework(image)
            except Exception as e:
                return {"status": "error", "reason": "homework_failed", "error": str(e)}

            return {"status": "ok", "type": "homework_result", "solution": solution}

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

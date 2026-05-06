# SIRIUS LOCAL AI GAMA - Mobile Vision Entry

from runtime_mobile.core.event_types import MobileEventTypes

class MobileVisionEntry:
    """
    Entry point for mobile OCR and vision processing.
    """

    def __init__(self, context):
        self.context = context

    def process(self, event):
        image = event.get("image")

        if image is None:
            return {
                "status": "error",
                "reason": "no_image"
            }

        etype = event.type

        # --- OCR ---
        if etype == MobileEventTypes.OCR:
            text = self.context.vision_engine.ocr(image)
            return {
                "status": "ok",
                "type": "ocr_result",
                "text": text
            }

        # --- Image Analysis ---
        if etype == MobileEventTypes.ANALYZE:
            result = self.context.vision_engine.analyze(image)
            return {
                "status": "ok",
                "type": "analysis_result",
                "analysis": result
            }

        # --- Unknown ---
        return {
            "status": "ignored",
            "reason": "unknown_vision_event",
            "event_type": etype
        }

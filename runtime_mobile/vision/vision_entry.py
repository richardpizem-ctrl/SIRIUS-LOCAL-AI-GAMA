class MobileVisionEntry:
    """
    Entry point for the mobile vision module.
    Handles OCR, image preprocessing and visual event interpretation.
    """

    def __init__(self, context):
        self.context = context

    def process(self, event):
        """
        Main processing method for vision events.
        """
        event_type = event.get("type")

        if event_type == "ocr":
            return self._run_ocr(event)

        if event_type == "analyze":
            return self._analyze_image(event)

        return {"status": "ignored", "reason": "unknown_event"}

    def _run_ocr(self, event):
        image = event.get("image")
        text = self.context.vision_engine.ocr(image)

        return {
            "status": "ok",
            "text": text
        }

    def _analyze_image(self, event):
        image = event.get("image")
        result = self.context.vision_engine.analyze(image)

        return {
            "status": "ok",
            "analysis": result
        }

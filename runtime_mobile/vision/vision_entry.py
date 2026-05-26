"""
SIRIUS LOCAL AI GAMA – Vision Entry
Mobile Runtime 3.2.0

Connects:
- Event Engine
- VisionEngineV3
"""

from runtime_mobile.core.event_types import MobileEventTypes


class VisionEntry:
    VERSION = "3.2.0"

    def __init__(self, context):
        self.context = context
        self.engine = context.vision_engine

    # ---------------------------------------------------------
    # Event Handler
    # ---------------------------------------------------------

    def on_event(self, event):
        etype = event.type if hasattr(event, "type") else event.get("type")
        payload = event.payload if hasattr(event, "payload") else event.get("payload", {})

        if not self.engine:
            return {"status": "error", "reason": "vision_engine_missing"}

        # SCENE
        if etype == MobileEventTypes.SCENE:
            return self.engine.process_scene(payload)

        # DETECT
        if etype == MobileEventTypes.DETECT:
            return self.engine.process_detect(payload)

        # OCR
        if etype == MobileEventTypes.OCR:
            return self.engine.process_ocr(payload)

        # HOMEWORK
        if etype == MobileEventTypes.HOMEWORK:
            return self.engine.process_homework(payload)

        return {"status": "ignored", "reason": "unknown_vision_event"}

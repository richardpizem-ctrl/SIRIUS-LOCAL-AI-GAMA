# ============================================================
# SIRIUS LOCAL AI GAMA - Vision Module
# Version: 3.0.0-pre
# ============================================================

from typing import Any, Dict
from .base_module import BaseModule


class VisionModule(BaseModule):

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self):
        super().__init__("vision")
        self.engine = None

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_load(self):
        if self.runtime and hasattr(self.runtime, "get_vision_engine"):
            self.engine = self.runtime.get_vision_engine()

    def on_unload(self):
        self.engine = None

    # ------------------------------------------------------------
    # Event Hook (3.x)
    # ------------------------------------------------------------

    def on_event(self, event):
        """Passive hook (optional)."""
        pass

    # ------------------------------------------------------------
    # Main Vision Entry
    # ------------------------------------------------------------

    def process(self, event: Any) -> Dict[str, Any]:
        """
        Unified vision processing entry point.
        Supports both dict and MobileEvent.
        """

        # MobileEvent support
        if hasattr(event, "payload"):
            payload = event.payload
        else:
            payload = event

        vtype = payload.get("type")
        image = payload.get("image")

        if not self.engine:
            return {"status": "error", "reason": "engine_not_available"}

        if not image:
            return {"status": "error", "reason": "no_image"}

        try:
            if vtype == "ocr":
                result = self.engine.ocr(image)
                return {"status": "ok", "type": "ocr", "text": result}

            if vtype == "detect":
                result = self.engine.detect(image)
                return {"status": "ok", "type": "detect", "objects": result}

            if vtype == "scene":
                result = self.engine.analyze(image)
                return {"status": "ok", "type": "scene", "analysis": result}

            if vtype == "homework":
                result = self.engine.homework(image)
                return {"status": "ok", "type": "homework", "solution": result}

        except Exception as e:
            return {"status": "error", "reason": "vision_failed", "error": str(e)}

        return {"status": "error", "reason": "unknown_vision_type", "type": vtype}

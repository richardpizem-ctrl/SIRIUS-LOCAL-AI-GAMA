# ============================================================
# SIRIUS LOCAL AI GAMA - Vision Module
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Unified Vision Module for mobile runtime.
# Provides:
#   - OCR interface
#   - object detection interface
#   - scene understanding interface
#   - homework recognition hooks
#   - safe processing pipeline
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

from typing import Any, Dict
from .base_module import BaseModule


class VisionModule(BaseModule):
    """
    Vision processing module for GAMA mobile runtime.

    Responsibilities:
    - provide unified process() interface
    - route tasks to OCR / detection / scene understanding
    - integrate with Vision Engine (runtime-injected)
    - handle errors safely
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self):
        super().__init__("vision")
        self.engine = None  # Vision Engine instance (injected by runtime)

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_load(self):
        """Attach Vision Engine from runtime if available."""
        if self.runtime and hasattr(self.runtime, "get_vision_engine"):
            self.engine = self.runtime.get_vision_engine()

    def on_unload(self):
        """Detach engine."""
        self.engine = None

    # ------------------------------------------------------------
    # Main Vision Entry
    # ------------------------------------------------------------

    def process(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Unified vision processing entry point.

        Expected event format:
        {
            "type": "ocr" | "detect" | "scene" | "homework",
            "image": <image_data>
        }
        """

        if not isinstance(event, dict):
            return self._error("Invalid event format")

        event_type = event.get("type")
        image = event.get("image")

        if image is None:
            return self._error("No image provided")

        # Route to specific vision task
        if event_type == "ocr":
            return self._run_ocr(image)

        if event_type == "detect":
            return self._run_detection(image)

        if event_type == "scene":
            return self._run_scene_understanding(image)

        if event_type == "homework":
            return self._run_homework(image)

        return self._error(f"Unknown vision event type: {event_type}")

    # ------------------------------------------------------------
    # Vision Task Handlers
    # ------------------------------------------------------------

    def _run_ocr(self, image):
        """OCR processing."""
        if not self.engine or not hasattr(self.engine, "ocr"):
            return self._placeholder("ocr")

        try:
            text = self.engine.ocr(image)
            return {
                "status": "ok",
                "type": "ocr_result",
                "text": text,
            }
        except Exception as e:
            return self._error(f"OCR failed: {e}")

    def _run_detection(self, image):
        """Object detection."""
        if not self.engine or not hasattr(self.engine, "detect"):
            return self._placeholder("detect")

        try:
            objects = self.engine.detect(image)
            return {
                "status": "ok",
                "type": "detection_result",
                "objects": objects,
            }
        except Exception as e:
            return self._error(f"Detection failed: {e}")

    def _run_scene_understanding(self, image):
        """Scene understanding."""
        if not self.engine or not hasattr(self.engine, "scene"):
            return self._placeholder("scene")

        try:
            scene = self.engine.scene(image)
            return {
                "status": "ok",
                "type": "scene_result",
                "scene": scene,
            }
        except Exception as e:
            return self._error(f"Scene understanding failed: {e}")

    def _run_homework(self, image):
        """Homework recognition (math, text, diagrams)."""
        if not self.engine or not hasattr(self.engine, "homework"):
            return self._placeholder("homework")

        try:
            result = self.engine.homework(image)
            return {
                "status": "ok",
                "type": "homework_result",
                "result": result,
            }
        except Exception as e:
            return self._error(f"Homework recognition failed: {e}")

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _placeholder(self, task: str) -> Dict[str, Any]:
        """Fallback when Vision Engine is not available."""
        return {
            "status": "placeholder",
            "type": f"{task}_result",
            "message": f"[Vision module placeholder output for {task}]",
        }

    def _error(self, message: str) -> Dict[str, Any]:
        """Error response."""
        return {
            "status": "error",
            "type": "vision_error",
            "error": message,
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
        """Extend base metadata with vision info."""
        base = super().get_info()
        base.update({
            "engine_attached": self.engine is not None,
        })
        return base

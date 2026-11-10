"""
vision_flow_detect.py
---------------------
Deterministic detection flow for Vision Flow v3.

Responsibilities:
- Perform deterministic object detection steps
- Integrate with VisionFlowScene
- Avoid nondeterministic behavior (no randomness, no async drift)
- Provide stable, predictable detection output
- Support Self‑Repair Layer 4.4

This module is fully deterministic:
- No dynamic imports
- No reflection
- No eval/exec
"""


class VisionFlowDetect:
    """
    Deterministic detection pipeline.
    Each step receives and returns a context dictionary.
    """

    def __init__(self, sanitizer, detector):
        """
        sanitizer: VisionSanitizer instance
        detector: deterministic object detector (no randomness)
        """
        self.sanitizer = sanitizer
        self.detector = detector

    # -------------------------------------------------------------

    def step_sanitize(self, context: dict) -> dict:
        """
        Sanitizes the input image data.
        """

        cleaned = self.sanitizer.clean(context.get("image"))
        if cleaned is None:
            return {
                "status": "error",
                "reason": "sanitize_failed"
            }

        context["image"] = cleaned
        return context

    # -------------------------------------------------------------

    def step_extract_features(self, context: dict) -> dict:
        """
        Extracts deterministic features from the image.
        """

        image = context.get("image")
        if image is None:
            return {
                "status": "error",
                "reason": "missing_image"
            }

        features = self.detector.extract_features(image)
        if features is None:
            return {
                "status": "error",
                "reason": "feature_extraction_failed"
            }

        context["features"] = features
        return context

    # -------------------------------------------------------------

    def step_detect_objects(self, context: dict) -> dict:
        """
        Performs deterministic object detection.
        """

        features = context.get("features")
        if features is None:
            return {
                "status": "error",
                "reason": "missing_features"
            }

        detections = self.detector.detect(features)
        if detections is None:
            return {
                "status": "error",
                "reason": "detection_failed"
            }

        context["detections"] = detections
        return context

    # -------------------------------------------------------------

    def step_format_output(self, context: dict) -> dict:
        """
        Formats detection results into a stable structure.
        """

        detections = context.get("detections", [])

        context["result"] = {
            "objects": detections,
            "count": len(detections)
        }

        return context

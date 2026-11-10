"""
vision_flow_homework.py
-----------------------
Deterministic homework extraction flow for Vision Flow v3.

Responsibilities:
- Extract homework text from images
- Normalize and classify extracted content
- Provide deterministic, predictable output
- Integrate with VisionFlowScene and Schoolwork Reasoning v3
- Support Self‑Repair Layer 4.4

This module is fully deterministic:
- No dynamic imports
- No reflection
- No eval/exec
"""


class VisionFlowHomework:
    """
    Deterministic homework extraction pipeline.
    """

    def __init__(self, sanitizer, ocr_engine, classifier):
        """
        sanitizer: VisionSanitizer instance
        ocr_engine: deterministic OCR engine
        classifier: deterministic homework classifier
        """
        self.sanitizer = sanitizer
        self.ocr_engine = ocr_engine
        self.classifier = classifier

    # -------------------------------------------------------------

    def step_sanitize(self, context: dict) -> dict:
        """
        Sanitizes the input image.
        """

        cleaned = self.sanitizer.clean(context.get("image"))
        if cleaned is None:
            return {"status": "error", "reason": "sanitize_failed"}

        context["image"] = cleaned
        return context

    # -------------------------------------------------------------

    def step_preprocess(self, context: dict) -> dict:
        """
        Prepares image for OCR.
        """

        image = context.get("image")
        if image is None:
            return {"status": "error", "reason": "missing_image"}

        processed = self.ocr_engine.preprocess(image)
        if processed is None:
            return {"status": "error", "reason": "preprocess_failed"}

        context["processed"] = processed
        return context

    # -------------------------------------------------------------

    def step_run_ocr(self, context: dict) -> dict:
        """
        Extracts text deterministically.
        """

        processed = context.get("processed")
        if processed is None:
            return {"status": "error", "reason": "missing_processed_image"}

        text = self.ocr_engine.extract_text(processed)
        if text is None:
            return {"status": "error", "reason": "ocr_failed"}

        context["raw_text"] = text
        return context

    # -------------------------------------------------------------

    def step_normalize(self, context: dict) -> dict:
        """
        Normalizes OCR text for classification.
        """

        raw = context.get("raw_text", "")
        normalized = self.ocr_engine.normalize(raw)

        context["text"] = normalized
        return context

    # -------------------------------------------------------------

    def step_classify(self, context: dict) -> dict:
        """
        Classifies the homework type (math, language, physics, etc.).
        """

        text = context.get("text", "")
        classification = self.classifier.classify(text)

        context["classification"] = classification
        return context

    # -------------------------------------------------------------

    def step_format_output(self, context: dict) -> dict:
        """
        Formats final output for Schoolwork Reasoning Engine.
        """

        context["result"] = {
            "text": context.get("text", ""),
            "classification": context.get("classification", "unknown")
        }

        return context

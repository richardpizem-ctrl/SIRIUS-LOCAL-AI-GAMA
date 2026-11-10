"""
vision_flow_ocr.py
------------------
Deterministic OCR flow for Vision Flow v3.

Responsibilities:
- Perform deterministic OCR extraction
- Integrate with VisionFlowScene
- Avoid nondeterministic behavior (no randomness, no async drift)
- Provide stable, predictable OCR output
- Support Self‑Repair Layer 4.4

This module is fully deterministic:
- No dynamic imports
- No reflection
- No eval/exec
"""


class VisionFlowOCR:
    """
    Deterministic OCR pipeline.
    Each step receives and returns a context dictionary.
    """

    def __init__(self, sanitizer, ocr_engine):
        """
        sanitizer: VisionSanitizer instance
        ocr_engine: deterministic OCR engine (no randomness)
        """
        self.sanitizer = sanitizer
        self.ocr_engine = ocr_engine

    # -------------------------------------------------------------

    def step_sanitize(self, context: dict) -> dict:
        """
        Sanitizes the input image before OCR.
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

    def step_preprocess(self, context: dict) -> dict:
        """
        Applies deterministic preprocessing:
        - grayscale
        - thresholding
        - deskew
        - noise removal
        """

        image = context.get("image")
        if image is None:
            return {
                "status": "error",
                "reason": "missing_image"
            }

        processed = self.ocr_engine.preprocess(image)
        if processed is None:
            return {
                "status": "error",
                "reason": "preprocess_failed"
            }

        context["processed"] = processed
        return context

    # -------------------------------------------------------------

    def step_run_ocr(self, context: dict) -> dict:
        """
        Runs deterministic OCR extraction.
        """

        processed = context.get("processed")
        if processed is None:
            return {
                "status": "error",
                "reason": "missing_processed_image"
            }

        text = self.ocr_engine.extract_text(processed)
        if text is None:
            return {
                "status": "error",
                "reason": "ocr_failed"
            }

        context["raw_text"] = text
        return context

    # -------------------------------------------------------------

    def step_normalize(self, context: dict) -> dict:
        """
        Normalizes OCR output:
        - trims whitespace
        - removes invalid characters
        - ensures deterministic formatting
        """

        raw = context.get("raw_text", "")
        normalized = self.ocr_engine.normalize(raw)

        context["text"] = normalized
        return context

    # -------------------------------------------------------------

    def step_format_output(self, context: dict) -> dict:
        """
        Formats OCR results into a stable structure.
        """

        text = context.get("text", "")

        context["result"] = {
            "text": text,
            "length": len(text)
        }

        return context

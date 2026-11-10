"""
vision_flow_fallback.py
-----------------------
Deterministic fallback handler for Vision Flow v3.

Responsibilities:
- Provide safe fallback behavior when primary vision flows fail
- Ensure deterministic, predictable output
- Prevent crashes in VisionFlowScene and VisionRouter
- Support Self‑Repair Layer 4.4

This module is fully deterministic:
- No dynamic imports
- No reflection
- No eval/exec
"""


class VisionFlowFallback:
    """
    Deterministic fallback pipeline for all vision flows.
    """

    def __init__(self):
        # No external dependencies, fully self-contained
        pass

    # -------------------------------------------------------------

    def step_validate(self, context: dict) -> dict:
        """
        Validates the incoming context.
        """

        if not isinstance(context, dict):
            return {
                "status": "error",
                "reason": "invalid_context_type",
                "result": self._default_result()
            }

        return context

    # -------------------------------------------------------------

    def step_recover_image(self, context: dict) -> dict:
        """
        Ensures that an image key exists.
        If missing, inserts a deterministic placeholder.
        """

        if "image" not in context or context["image"] is None:
            context["image"] = "fallback_image_placeholder"

        return context

    # -------------------------------------------------------------

    def step_generate_stub(self, context: dict) -> dict:
        """
        Generates a deterministic stub result when real processing fails.
        """

        context["result"] = {
            "text": "",
            "objects": [],
            "classification": "unknown",
            "fallback_used": True
        }

        return context

    # -------------------------------------------------------------

    def step_finalize(self, context: dict) -> dict:
        """
        Finalizes fallback output.
        """

        return {
            "status": "ok",
            "fallback": True,
            "context": context,
            "result": context.get("result", self._default_result())
        }

    # -------------------------------------------------------------

    def _default_result(self) -> dict:
        """
        Deterministic default result structure.
        """

        return {
            "text": "",
            "objects": [],
            "classification": "unknown",
            "fallback_used": True
        }

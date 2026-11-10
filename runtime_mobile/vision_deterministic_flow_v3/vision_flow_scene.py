"""
vision_flow_scene.py
--------------------
Scene-level deterministic flow controller for Vision Flow v3.

Responsibilities:
- Define deterministic scene steps for vision processing
- Provide predictable execution order
- Integrate with VisionFlow and VisionRouter
- Avoid nondeterministic behavior (no randomness, no async drift)
- Support Self‑Repair Layer 4.4

This module is fully deterministic:
- No dynamic imports
- No reflection
- No eval/exec
"""


class VisionFlowScene:
    """
    Represents a deterministic scene in the vision processing pipeline.
    Each scene defines:
    - name
    - required inputs
    - ordered processing steps
    """

    def __init__(self, name: str, steps: list):
        self.name = name
        self.steps = steps  # list of callables

    # -------------------------------------------------------------

    def run(self, context: dict) -> dict:
        """
        Executes the scene deterministically.
        Each step receives and returns the context.
        """

        if not isinstance(context, dict):
            return {"status": "error", "reason": "invalid_context"}

        current = context

        for step in self.steps:
            try:
                current = step(current)

                if not isinstance(current, dict):
                    return {
                        "status": "error",
                        "reason": "step_return_invalid",
                        "step": step.__name__
                    }

            except Exception:
                return {
                    "status": "error",
                    "reason": "step_exception",
                    "step": step.__name__
                }

        return {
            "status": "ok",
            "scene": self.name,
            "context": current
        }

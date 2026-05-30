"""
context_builder.py

GAMA Runtime 3.4.0 – Runtime Context v3
Builds a deterministic debug/runtime context for SCHOOLWORK + VISION + PACK pipelines.

Rules:
- No raw OCR/text content.
- No image data.
- Only semantic/meta fields.
- Deterministic structure.
- Fully offline, safe for families and schools.
"""

from typing import Dict, Any

from .context_schema_v3 import build_context_record_v3
from .debug_metadata import build_debug_meta_v3


class RuntimeContextBuilderV3:
    """
    Builds a unified runtime context record for the reasoning engine.

    Input:
        - unified_event (from unified_events_v3)
        - trace_meta (from trace_logs_v3)
        - normalization_meta (from fallback_normalization_v3)
        - system_meta (runtime info, safe only)

    Output:
        Deterministic context record (dict)
    """

    def build(
        self,
        *,
        unified_event: Dict[str, Any],
        trace_meta: Dict[str, Any],
        normalization_meta: Dict[str, Any],
        system_meta: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Main entry point for building the runtime context.
        """

        debug_meta = build_debug_meta_v3(
            unified_event=unified_event,
            trace_meta=trace_meta,
            normalization_meta=normalization_meta,
            system_meta=system_meta,
        )

        return build_context_record_v3(
            unified_event=unified_event,
            trace_meta=trace_meta,
            normalization_meta=normalization_meta,
            debug_meta=debug_meta,
        )

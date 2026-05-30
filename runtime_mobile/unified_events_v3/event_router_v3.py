"""
event_router_v3.py

GAMA Runtime 3.4.0 – Unified Event Router v3
Routes SCHOOLWORK + VISION + PACK inputs into a single unified event model.

Rules:
- No raw OCR/text content stored.
- No images or binary data.
- Only semantic/meta fields.
- Deterministic routing.
- Fully offline, safe for families and schools.
"""

from typing import Dict, Any, Optional

from .event_schema_v3 import build_event_v3
from .vision_bridge import extract_vision_meta_v3
from .pack_event_adapter import extract_pack_meta_v3


class UnifiedEventRouterV3:
    """
    Routes inputs from SCHOOLWORK, VISION, and PACK pipelines
    into a unified event structure.

    Input types:
        - SCHOOLWORK_TEXT
        - SCHOOLWORK_VISION
        - SCHOOLWORK_PACK

    Output:
        Deterministic unified event record (dict)
    """

    def route_schoolwork_text(
        self,
        *,
        trace_id: str,
        subject: Optional[str],
        difficulty: Optional[str],
        schoolwork_meta: Dict[str, Any],
        context_meta: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Routes SCHOOLWORK text-based tasks.
        """

        return build_event_v3(
            event_type="SCHOOLWORK_TEXT",
            source="user_input",
            trace_id=trace_id,
            subject=subject,
            difficulty=difficulty,
            schoolwork_meta=schoolwork_meta,
            context_meta=context_meta,
        )

    def route_schoolwork_vision(
        self,
        *,
        trace_id: str,
        vision_raw: Dict[str, Any],
        subject: Optional[str],
        difficulty: Optional[str],
        context_meta: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Routes SCHOOLWORK tasks that originate from VISION pipeline.
        """

        vision_meta = extract_vision_meta_v3(vision_raw)

        return build_event_v3(
            event_type="SCHOOLWORK_VISION",
            source="vision_detector",
            trace_id=trace_id,
            subject=subject,
            difficulty=difficulty,
            vision_meta=vision_meta,
            context_meta=context_meta,
        )

    def route_schoolwork_pack(
        self,
        *,
        trace_id: str,
        pack_raw: Dict[str, Any],
        subject: Optional[str],
        difficulty: Optional[str],
        context_meta: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Routes SCHOOLWORK tasks that originate from Knowledge Packs.
        """

        pack_meta = extract_pack_meta_v3(pack_raw)

        return build_event_v3(
            event_type="SCHOOLWORK_PACK",
            source="pack_loader",
            trace_id=trace_id,
            subject=subject,
            difficulty=difficulty,
            pack_ids=pack_meta.get("pack_ids", []),
            schoolwork_meta=pack_meta.get("schoolwork_meta", {}),
            context_meta=context_meta,
        )

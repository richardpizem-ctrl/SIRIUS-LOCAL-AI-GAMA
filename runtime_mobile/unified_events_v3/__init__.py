"""
unified_events_v3

GAMA Runtime 3.4.0 – Unified Event Model v3
Unified event schema + routing for SCHOOLWORK + VISION + PACK.

Exports:
- build_event_v3
- UnifiedEventRouterV3
- extract_vision_meta_v3
- extract_pack_meta_v3
"""

from .event_schema_v3 import build_event_v3
from .event_router_v3 import UnifiedEventRouterV3
from .vision_bridge import extract_vision_meta_v3
from .pack_event_adapter import extract_pack_meta_v3

__all__ = [
    "build_event_v3",
    "UnifiedEventRouterV3",
    "extract_vision_meta_v3",
    "extract_pack_meta_v3",
]

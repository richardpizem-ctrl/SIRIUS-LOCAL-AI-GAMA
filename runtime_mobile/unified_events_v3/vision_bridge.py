"""
vision_bridge.py

GAMA Runtime 3.4.0 – Unified Event Model v3
Bridge module that converts Vision Flow v3 output into safe semantic meta-data.

Rules:
- No raw OCR/text content.
- No image data.
- Only semantic/meta fields.
- Deterministic structure.
- Fully offline, safe for families and schools.
"""

from typing import Dict, Any


def extract_vision_meta_v3(vision_raw: Dict[str, Any]) -> Dict[str, Any]:
    """
    Converts raw Vision Flow v3 output into a safe meta-data block.

    Expected vision_raw structure (example):
        {
            "status": "ok",
            "type": "homework",
            "detected_subject": "math",
            "confidence": 0.92,
            "detected_shapes": [...],
            "detected_regions": [...],
            "ocr_meta": {...},   # NO raw text here
        }

    Output (safe):
        {
            "vision_status": "ok",
            "vision_type": "homework",
            "subject_hint": "math",
            "confidence": 0.92,
            "regions_count": 3,
            "shapes_count": 1
        }
    """

    if not vision_raw:
        return {
            "vision_status": "empty",
            "vision_type": None,
            "subject_hint": None,
            "confidence": None,
            "regions_count": 0,
            "shapes_count": 0,
        }

    # Extract safe fields only
    status = vision_raw.get("status")
    vtype = vision_raw.get("type")
    subject_hint = vision_raw.get("detected_subject")
    confidence = vision_raw.get("confidence")

    regions = vision_raw.get("detected_regions", [])
    shapes = vision_raw.get("detected_shapes", [])

    return {
        "vision_status": status,
        "vision_type": vtype,
        "subject_hint": subject_hint,
        "confidence": confidence,
        "regions_count": len(regions),
        "shapes_count": len(shapes),
    }

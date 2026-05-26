"""
SIRIUS LOCAL AI GAMA – Schoolwork OCR v2
Mobile Runtime 3.2.0

This module provides:
- OCR v2 text extraction
- homework-specific OCR heuristics
- math/physics/geometry detection
- preparation for Vision Engine 4.0
"""

SCHOOLWORK_OCR_VERSION = "3.2.0"


# ---------------------------------------------------------
# Basic OCR extraction
# ---------------------------------------------------------

def extract_text(image_payload: dict) -> dict:
    """
    Extract raw text from the image using OCR v2.
    """
    return {
        "type": "ocr",
        "text": image_payload.get("text", ""),
        "lines": image_payload.get("lines", []),
        "language": image_payload.get("language", "unknown"),
    }


# ---------------------------------------------------------
# Homework subject detection
# ---------------------------------------------------------

def detect_subject(text: str) -> str:
    """
    Detect homework subject based on OCR text.
    """
    t = text.lower()

    if any(x in t for x in ["solve", "equation", "x =", "y =", "root"]):
        return "math"

    if any(x in t for x in ["force", "velocity", "joule", "energy"]):
        return "physics"

    if any(x in t for x in ["triangle", "angle", "geometry"]):
        return "geometry"

    if any(x in t for x in ["translate", "grammar", "sentence"]):
        return "language"

    return "unknown"


# ---------------------------------------------------------
# Homework OCR v2
# ---------------------------------------------------------

def process_homework(image_payload: dict) -> dict:
    """
    Full homework OCR v2 pipeline:
    - extract text
    - detect subject
    - return structured result
    """
    text = image_payload.get("text", "")
    lines = image_payload.get("lines", [])

    subject = detect_subject(text)

    return {
        "type": "homework_ocr",
        "text": text,
        "lines": lines,
        "subject": subject,
    }


# ---------------------------------------------------------
# Main dispatcher
# ---------------------------------------------------------

def run(image_payload: dict, mode: str = "HOMEWORK") -> dict:
    """
    Unified entry point for Schoolwork OCR v2.
    """
    mode = mode.upper()

    if mode == "HOMEWORK":
        return process_homework(image_payload)

    if mode == "OCR":
        return extract_text(image_payload)

    return {"error": "UNSUPPORTED_MODE"}


# ---------------------------------------------------------
# Metadata
# ---------------------------------------------------------

def get_schoolwork_ocr_info() -> dict:
    """
    Return metadata for Schoolwork OCR v2.
    """
    return {
        "version": SCHOOLWORK_OCR_VERSION,
        "modes": ["HOMEWORK", "OCR"],
    }

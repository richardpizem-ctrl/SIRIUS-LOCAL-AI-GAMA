# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Smoke Test
# Version: 3.1.0
# ============================================================

from runtime_mobile.core.runtime_core import MobileRuntimeCore
from runtime_mobile.core.runtime_context import MobileRuntimeContext
from runtime_mobile.core.runtime_dispatcher import MobileRuntimeDispatcher
from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.core.mobile_event import MobileEvent

# ------------------------------------------------------------
# Dummy Vision Engine (for testing)
# ------------------------------------------------------------

class DummyVisionEngine:
    def ocr(self, image):
        return "dummy ocr text"

    def detect(self, image):
        return [{"label": "object", "confidence": 0.99}]

    def analyze(self, image):
        return {"scene": "dummy scene"}

    def homework(self, image):
        return {"solution": "42"}


# ------------------------------------------------------------
# Runtime Builder
# ------------------------------------------------------------

def build_runtime():
    context = MobileRuntimeContext()
    context.vision_engine = DummyVisionEngine()

    dispatcher = MobileRuntimeDispatcher(context)

    core = MobileRuntimeCore(context, dispatcher)

    init = core.initialize()
    assert init["status"] == "initialized", init

    return core


# ------------------------------------------------------------
# Smoke Test
# ------------------------------------------------------------

def test_mobile_ocr():
    runtime = build_runtime()

    # Simulate OCR event
    event = MobileEvent(MobileEventTypes.OCR, image="dummy")
    result = runtime.handle_event(event)

    print("OCR RESULT:", result)

    assert result["status"] == "ok", result
    assert result["type"] == "ocr"
    assert result["text"] == "dummy ocr text"

    print("Smoke test passed.")


if __name__ == "__main__":
    test_mobile_ocr()

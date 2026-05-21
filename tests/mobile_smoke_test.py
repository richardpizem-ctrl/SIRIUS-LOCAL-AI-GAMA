# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Smoke Test
# Version: 3.1.0
# ============================================================

from runtime_mobile.core.runtime_core import MobileRuntimeCore
from runtime_mobile.core.runtime_context import MobileRuntimeContext
from runtime_mobile.core.runtime_dispatcher import MobileRuntimeDispatcher
from runtime_mobile.core.router_mobile import MobileNLRouter
from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.core.mobile_event import MobileEvent

from runtime_mobile.core.permissions import MobilePermissions
from runtime_mobile.pack_manager import MobilePackManager
from runtime_mobile.knowledge_packs.packs_mobile import MobileKnowledgePacks
from runtime_mobile.vision_entry import MobileVisionEntry
from runtime_mobile.security.security_entry import MobileSecurityEntry


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
    context.permissions = MobilePermissions()
    context.pack_manager = MobilePackManager()
    context.vision_engine = DummyVisionEngine()

    vision = MobileVisionEntry(context)
    security = MobileSecurityEntry(context)
    packs = MobileKnowledgePacks(context)

    router = MobileNLRouter()
    dispatcher = MobileRuntimeDispatcher(context)

    core = MobileRuntimeCore(context, dispatcher, router)
    core.load_modules(
        vision=vision,
        security=security,
        packs=packs,
    )

    init = core.initialize()
    assert init["status"] == "initialized"

    return core


# ------------------------------------------------------------
# Smoke Test
# ------------------------------------------------------------

if __name__ == "__main__":
    runtime = build_runtime()

    # Simulate OCR event
    event = MobileEvent(MobileEventTypes.OCR, image="dummy")
    result = runtime.dispatcher.dispatch(event)

    print("OCR RESULT:", result)

    assert result["status"] == "ok"
    assert result["type"] == "ocr_result"
    assert result["text"] == "dummy ocr text"

    print("Smoke test passed.")

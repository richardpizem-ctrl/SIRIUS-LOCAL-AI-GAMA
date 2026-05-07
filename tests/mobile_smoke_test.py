# SIRIUS LOCAL AI GAMA - Mobile Runtime Smoke Test

from runtime_mobile.core import (
    MobileRuntimeCore,
    MobileRuntimeContext,
    MobileRuntimeDispatcher,
    MobileNLRouter,
    MobileEventTypes,
)
from runtime_mobile.core.permissions import MobilePermissions
from runtime_mobile.pack_manager import MobilePackManager
from runtime_mobile.knowledge_packs.packs_mobile import MobileKnowledgePacks
from runtime_mobile.vision_entry import MobileVisionEntry
from runtime_mobile.security.security_entry import MobileSecurityEntry
from runtime_mobile.core.event import MobileEvent


class DummyVisionEngine:
    def ocr(self, image):
        return "dummy ocr text"


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
    core.initialize()
    return core


if __name__ == "__main__":
    runtime = build_runtime()

    event = MobileEvent(MobileEventTypes.OCR, image="dummy")
    result = runtime.dispatcher.dispatch(event)
    print("OCR RESULT:", result)

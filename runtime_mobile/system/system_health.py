"""
SIRIUS LOCAL AI GAMA – System Health Monitor
Mobile Runtime 3.2.0

Provides:
- runtime health checks
- engine availability checks
- event engine diagnostics
- vision engine diagnostics
"""

class SystemHealth:
    VERSION = "3.2.0"

    def __init__(self, context):
        self.context = context

    # ---------------------------------------------------------
    # Vision Engine Health
    # ---------------------------------------------------------

    def check_vision(self) -> dict:
        engine = getattr(self.context, "vision_engine", None)

        if engine is None:
            return {"vision": "missing"}

        try:
            info = engine.get_info()
            return {"vision": "ok", "info": info}
        except Exception as e:
            return {"vision": "error", "error": str(e)}

    # ---------------------------------------------------------
    # Event Engine Health
    # ---------------------------------------------------------

    def check_event_engine(self) -> dict:
        router = getattr(self.context, "event_router", None)

        if router is None:
            return {"event_engine": "missing"}

        try:
            return {"event_engine": "ok"}
        except Exception as e:
            return {"event_engine": "error", "error": str(e)}

    # ---------------------------------------------------------
    # Full System Health
    # ---------------------------------------------------------

    def full_report(self) -> dict:
        return {
            "system_health": {
                "version": self.VERSION,
                "vision": self.check_vision(),
                "event_engine": self.check_event_engine(),
            }
        }

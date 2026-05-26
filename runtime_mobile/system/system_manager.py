"""
SIRIUS LOCAL AI GAMA – System Manager
Mobile Runtime 3.2.0

Coordinates:
- SystemLoader
- SystemHealth
- Event Engine
- Vision Entry

Provides:
- runtime start
- runtime restart
- health reporting
"""

from .system_loader import SystemLoader
from .system_health import SystemHealth


class SystemManager:
    VERSION = "3.2.0"

    def __init__(self):
        self.loader = SystemLoader()
        self.context = None
        self.health = None

    # ---------------------------------------------------------
    # Runtime Start
    # ---------------------------------------------------------

    def start(self):
        """
        Start the entire runtime system.
        """
        print("[SystemManager] Starting runtime...")
        self.context = self.loader.load_all()
        self.health = SystemHealth(self.context)
        print("[SystemManager] Runtime started.")
        return self.context

    # ---------------------------------------------------------
    # Runtime Restart
    # ---------------------------------------------------------

    def restart(self):
        """
        Restart the runtime system.
        """
        print("[SystemManager] Restarting runtime...")
        self.context = self.loader.load_all()
        self.health = SystemHealth(self.context)
        print("[SystemManager] Runtime restarted.")
        return self.context

    # ---------------------------------------------------------
    # Health Report
    # ---------------------------------------------------------

    def get_health_report(self) -> dict:
        """
        Return full system health report.
        """
        if not self.health:
            return {"error": "runtime_not_started"}

        return self.health.full_report()

    # ---------------------------------------------------------
    # Metadata
    # ---------------------------------------------------------

    def get_info(self) -> dict:
        return {
            "system_manager": "SIRIUS Mobile Runtime",
            "version": self.VERSION,
            "components": {
                "loader": True,
                "health": True,
                "event_engine": hasattr(self.context, "event_router"),
                "vision_engine": hasattr(self.context, "vision_engine"),
                "vision_entry": hasattr(self.context, "vision_entry"),
            }
        }

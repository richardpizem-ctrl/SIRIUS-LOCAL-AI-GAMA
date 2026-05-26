"""
SIRIUS LOCAL AI GAMA – System API
Mobile Runtime 3.2.0

Provides a clean API for:
- sending events to runtime
- retrieving system health
- restarting runtime
- accessing system info
"""

from .system_manager import SystemManager


class SystemAPI:
    VERSION = "3.2.0"

    def __init__(self):
        self.manager = SystemManager()
        self.context = self.manager.start()

    # ---------------------------------------------------------
    # Event Execution
    # ---------------------------------------------------------

    def run_event(self, event):
        """
        Send an event to the runtime event engine.
        """
        if not self.context or not self.context.event_router:
            return {"error": "runtime_not_ready"}

        try:
            return self.context.event_router.route(event)
        except Exception as e:
            return {"error": "event_failed", "details": str(e)}

    # ---------------------------------------------------------
    # Health Report
    # ---------------------------------------------------------

    def get_health(self):
        """
        Return full system health report.
        """
        return self.manager.get_health_report()

    # ---------------------------------------------------------
    # Restart Runtime
    # ---------------------------------------------------------

    def restart(self):
        """
        Restart the entire runtime system.
        """
        self.context = self.manager.restart()
        return {"status": "restarted"}

    # ---------------------------------------------------------
    # System Info
    # ---------------------------------------------------------

    def get_system_info(self):
        """
        Return metadata about the runtime system.
        """
        return self.manager.get_info()

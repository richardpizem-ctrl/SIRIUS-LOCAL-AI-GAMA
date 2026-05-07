# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Diagnostics Module
# Version: 3.0.0-pre
# ============================================================

from typing import Dict, Any, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes

from runtime_mobile.system.battery import MobileBatteryModule
from runtime_mobile.system.thermal import MobileThermalModule
from runtime_mobile.system.storage import MobileStorageModule


class MobileDiagnostics:

    MODULE_VERSION = "3.0.0-pre"

    def __init__(
        self,
        battery: Optional[MobileBatteryModule] = None,
        thermal: Optional[MobileThermalModule] = None,
        storage: Optional[MobileStorageModule] = None,
    ):
        self.battery = battery or MobileBatteryModule()
        self.thermal = thermal or MobileThermalModule()
        self.storage = storage or MobileStorageModule()

        self.last_report: Dict[str, Any] = {}

    # ------------------------------------------------------------
    # Runtime hook
    # ------------------------------------------------------------

    def on_event(self, event: MobileEvent):
        """Passive monitoring hook."""
        self.last_report["last_event"] = event.type

    # ------------------------------------------------------------
    # Unified diagnostics report
    # ------------------------------------------------------------

    def generate_report(self) -> Dict[str, Any]:
        report = {
            "module": "diagnostics",
            "version": self.MODULE_VERSION,
            "battery": self.battery.get_status(),
            "thermal": self.thermal.get_status(),
            "storage": self.storage.get_status(),
            "last_event": self.last_report.get("last_event"),
        }

        self.last_report = report
        return report

    # ------------------------------------------------------------
    # Event handling
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:

        et = event.type

        # Full diagnostics report
        if et == MobileEventTypes.DIAGNOSTICS_REPORT:
            return {
                "status": "ok",
                "type": "diagnostics_report",
                "report": self.generate_report(),
            }

        # Battery
        if et == MobileEventTypes.CHECK_BATTERY:
            return self.battery.handle_event(event)

        # Thermal
        if et == MobileEventTypes.CHECK_THERMAL:
            return self.thermal.handle_event(event)

        # Storage
        if et == MobileEventTypes.CHECK_STORAGE:
            return self.storage.handle_event(event)

        # Memory (missing in original)
        if et == MobileEventTypes.CHECK_MEMORY:
            return {
                "status": "ok",
                "type": "memory_status",
                "memory": self.storage.get_memory_status(),
            }

        return {
            "status": "ignored",
            "reason": "unsupported_event",
            "event_type": et,
            "module": "diagnostics",
        }

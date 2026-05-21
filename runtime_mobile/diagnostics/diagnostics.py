# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Diagnostics Module
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Upgraded for GAMA Runtime 3.1:
# - Diagnostics v3 unified pipeline
# - MobileEvent 3.1 (metadata, tags, source)
# - Extended system metrics (battery / thermal / storage / memory)
# - Passive monitoring hook v3
# - Stable structured report format
# ============================================================

from typing import Dict, Any, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes

from runtime_mobile.system.battery import MobileBatteryModule
from runtime_mobile.system.thermal import MobileThermalModule
from runtime_mobile.system.storage import MobileStorageModule


class MobileDiagnostics:

    MODULE_VERSION = "3.1.0"

    def __init__(
        self,
        battery: Optional[MobileBatteryModule] = None,
        thermal: Optional[MobileThermalModule] = None,
        storage: Optional[MobileStorageModule] = None,
    ):
        self.battery = battery or MobileBatteryModule()
        self.thermal = thermal or MobileThermalModule()
        self.storage = storage or MobileStorageModule()

        # Last known diagnostics snapshot
        self.last_report: Dict[str, Any] = {}

    # ------------------------------------------------------------
    # Runtime Hook (Diagnostics v3)
    # ------------------------------------------------------------

    def on_event(self, event: MobileEvent):
        """
        Passive monitoring hook.
        Records last event type and timestamp.
        """
        self.last_report["last_event"] = event.type
        self.last_report["last_event_id"] = event.event_id
        self.last_report["last_event_timestamp"] = event.timestamp

    # ------------------------------------------------------------
    # Unified Diagnostics Report (3.1)
    # ------------------------------------------------------------

    def generate_report(self) -> Dict[str, Any]:
        report = {
            "module": "diagnostics",
            "version": self.MODULE_VERSION,

            # System metrics
            "battery": self.battery.get_status(),
            "thermal": self.thermal.get_status(),
            "storage": self.storage.get_status(),
            "memory": self.storage.get_memory_status(),

            # Metadata
            "last_event": self.last_report.get("last_event"),
            "last_event_id": self.last_report.get("last_event_id"),
            "last_event_timestamp": self.last_report.get("last_event_timestamp"),
        }

        self.last_report = report
        return report

    # ------------------------------------------------------------
    # Event Handling (3.1)
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

        # Memory
        if et == MobileEventTypes.CHECK_MEMORY:
            return {
                "status": "ok",
                "type": "memory_status",
                "memory": self.storage.get_memory_status(),
            }

        # Unknown / unsupported
        return {
            "status": "ignored",
            "reason": "unsupported_event",
            "event_type": et,
            "module": "diagnostics",
        }

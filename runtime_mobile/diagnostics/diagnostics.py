# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Diagnostics Module
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Central diagnostics orchestrator for the mobile runtime.
# Integrates:
#   - battery module
#   - thermal module
#   - storage module
#
# Provides:
#   - unified diagnostics API
#   - event handler for dispatcher
#   - on_event() hook for runtime_core
#
# Framework-agnostic, safe for offline/simulated environments.
# ============================================================

from typing import Dict, Any, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes

from runtime_mobile.system.battery import MobileBatteryModule
from runtime_mobile.system.thermal import MobileThermalModule
from runtime_mobile.system.storage import MobileStorageModule


class MobileDiagnostics:
    """
    Central diagnostics orchestrator.

    Responsibilities:
    - unify battery / thermal / storage diagnostics
    - provide event-based diagnostics API
    - provide runtime hook on_event()
    """

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

        # last diagnostics snapshot (for UI debug screen)
        self.last_report: Dict[str, Any] = {}

    # ------------------------------------------------------------
    # Runtime hook
    # ------------------------------------------------------------

    def on_event(self, event: MobileEvent):
        """
        Hook called by runtime_core before dispatch.
        Used for passive monitoring (optional).
        """
        # We do not modify the event or block anything.
        # Only record metadata if needed.
        self.last_report["last_event"] = event.type

    # ------------------------------------------------------------
    # Unified diagnostics report
    # ------------------------------------------------------------

    def generate_report(self) -> Dict[str, Any]:
        """Return full diagnostics snapshot."""
        report = {
            "module": "diagnostics",
            "version": self.MODULE_VERSION,
            "battery": self.battery.get_status(),
            "thermal": self.thermal.get_status(),
            "storage": self.storage.get_status(),
        }

        self.last_report = report
        return report

    # ------------------------------------------------------------
    # Event handling
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:
        """
        Handle diagnostics-related events from dispatcher.
        """

        # Full diagnostics report
        if event.type == MobileEventTypes.DIAGNOSTICS_REPORT:
            return {
                "status": "ok",
                "type": "diagnostics_report",
                "report": self.generate_report(),
            }

        # Battery
        if event.type == MobileEventTypes.CHECK_BATTERY:
            return self.battery.handle_event(event)

        # Thermal
        if event.type == MobileEventTypes.CHECK_THERMAL:
            return self.thermal.handle_event(event)

        # Storage
        if event.type == MobileEventTypes.CHECK_STORAGE:
            return self.storage.handle_event(event)

        # Unknown event
        return {
            "status": "ignored",
            "reason": "unsupported_event",
            "event_type": event.type,
            "module": "diagnostics",
        }

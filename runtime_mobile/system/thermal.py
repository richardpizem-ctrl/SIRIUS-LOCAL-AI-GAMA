# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Thermal System Module
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Framework-agnostic thermal status provider for the mobile runtime.
# - no direct OS / platform calls
# - expects an injected backend/adapter for real sensor data
# - safe for offline / simulated environments
# ============================================================

from typing import Any, Dict, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileThermalModule:
    """
    Thermal sensor abstraction for the mobile runtime.

    Design:
    - backend is optional (callable or object with get_thermal_status())
    - if backend missing, returns safe simulated values
    - used by diagnostics and dispatcher
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, backend: Optional[Any] = None):
        """
        backend may be:
            - callable: backend() -> dict
            - object:   backend.get_thermal_status() -> dict
        """
        self.backend = backend

    # ------------------------------------------------------------
    # Backend read
    # ------------------------------------------------------------

    def _read_backend(self) -> Dict[str, Any]:
        """Safely read raw thermal data from backend."""
        if self.backend is None:
            return {}

        try:
            if callable(self.backend):
                return self.backend() or {}
            if hasattr(self.backend, "get_thermal_status"):
                return self.backend.get_thermal_status() or {}
        except Exception as e:
            print(f"[WARN] Thermal backend failed: {e}")

        return {}

    # ------------------------------------------------------------
    # Normalized thermal status
    # ------------------------------------------------------------

    def get_status(self) -> Dict[str, Any]:
        """
        Return normalized thermal status.
        Keys are stable across all platforms.
        """
        raw = self._read_backend()

        cpu = raw.get("cpu_temp") or raw.get("cpu") or None
        gpu = raw.get("gpu_temp") or raw.get("gpu") or None
        battery = raw.get("battery_temp") or raw.get("battery") or None
        thermal_state = raw.get("state", "unknown")

        return {
            "module": "thermal",
            "version": self.MODULE_VERSION,
            "cpu_temp": cpu,
            "gpu_temp": gpu,
            "battery_temp": battery,
            "state": thermal_state,
        }

    # ------------------------------------------------------------
    # Event handling
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:
        """Handle CHECK_THERMAL event."""
        if event.type != MobileEventTypes.CHECK_THERMAL:
            return {
                "status": "ignored",
                "reason": "unsupported_event",
                "event_type": event.type,
                "module": "thermal",
            }

        status = self.get_status()

        return {
            "status": "ok",
            "module": "thermal",
            "thermal": status,
        }

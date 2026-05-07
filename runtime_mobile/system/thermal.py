# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Thermal System Module
# Version: 3.0.0-pre
# ============================================================

from typing import Any, Dict, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileThermalModule:

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, backend: Optional[Any] = None):
        self.backend = backend

    # ------------------------------------------------------------
    # Backend read
    # ------------------------------------------------------------

    def _read_backend(self) -> Dict[str, Any]:
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
        raw = self._read_backend()

        # CPU
        cpu = raw.get("cpu_temp")
        if cpu is None:
            cpu = raw.get("cpu")

        # GPU
        gpu = raw.get("gpu_temp")
        if gpu is None:
            gpu = raw.get("gpu")

        # Battery
        battery = raw.get("battery_temp")
        if battery is None:
            battery = raw.get("battery")

        # Validate ranges
        def _validate_temp(v):
            if v is None:
                return None
            if not isinstance(v, (int, float)):
                return None
            if v < -50 or v > 150:
                return None
            return v

        cpu = _validate_temp(cpu)
        gpu = _validate_temp(gpu)
        battery = _validate_temp(battery)

        # Thermal state
        thermal_state = raw.get("state", "unknown")

        return {
            "module": "thermal",
            "version": self.MODULE_VERSION,
            "cpu_temp": cpu,
            "gpu_temp": gpu,
            "battery_temp": battery,
            "thermal_state": thermal_state,
        }

    # ------------------------------------------------------------
    # Event handling
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:

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
            "event_type": MobileEventTypes.CHECK_THERMAL,
            "module": "thermal",
            "thermal": status,
        }

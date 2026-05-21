# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Thermal System Module
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for GAMA Runtime 3.1:
# - normalized thermal schema v3
# - safe validation of CPU/GPU/Battery temps
# - thermal_state v3 (cool/normal/warm/hot/critical)
# - backend fail-safe
# - diagnostics v3 compatibility
# - added thermal_load + source metadata
# ============================================================

from typing import Any, Dict, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileThermalModule:

    MODULE_VERSION = "3.1.0"

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
        """Safe backend read with full isolation."""
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
    # Temperature validator
    # ------------------------------------------------------------

    def _validate_temp(self, value):
        """Safe temperature validation for CPU/GPU/Battery."""
        if value is None:
            return None
        if not isinstance(value, (int, float)):
            return None
        # Safe operational range for mobile devices
        if value < -20:
            return -20
        if value > 120:
            return 120
        return value

    # ------------------------------------------------------------
    # Thermal state classifier (v3)
    # ------------------------------------------------------------

    def _classify_state(self, cpu, gpu, battery):
        temps = [t for t in (cpu, gpu, battery) if isinstance(t, (int, float))]
        if not temps:
            return "unknown"

        max_t = max(temps)

        if max_t < 40:
            return "cool"
        if max_t < 60:
            return "normal"
        if max_t < 75:
            return "warm"
        if max_t < 90:
            return "hot"
        return "critical"

    # ------------------------------------------------------------
    # Normalized thermal status (v3)
    # ------------------------------------------------------------

    def get_status(self) -> Dict[str, Any]:
        raw = self._read_backend()

        # CPU
        cpu = raw.get("cpu_temp") or raw.get("cpu")
        cpu = self._validate_temp(cpu)

        # GPU
        gpu = raw.get("gpu_temp") or raw.get("gpu")
        gpu = self._validate_temp(gpu)

        # Battery
        battery = raw.get("battery_temp") or raw.get("battery")
        battery = self._validate_temp(battery)

        # Optional fields
        thermal_load = raw.get("thermal_load")  # 0–100 %
        source = raw.get("source", "unknown")

        # State classification
        thermal_state = self._classify_state(cpu, gpu, battery)

        return {
            "module": "thermal",
            "version": self.MODULE_VERSION,
            "cpu_temp": cpu,
            "gpu_temp": gpu,
            "battery_temp": battery,
            "thermal_state": thermal_state,
            "thermal_load": thermal_load,
            "source": source,
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

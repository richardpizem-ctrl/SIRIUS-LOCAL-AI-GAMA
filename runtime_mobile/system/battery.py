# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Battery System Module
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for GAMA Runtime 3.1:
# - normalized battery schema v3
# - safe temperature validation
# - safe level validation
# - backend fail-safe
# - diagnostics v3 compatibility
# ============================================================

from typing import Any, Dict, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileBatteryModule:

    MODULE_VERSION = "3.1.0"

    def __init__(self, backend: Optional[Any] = None):
        """
        backend: optional adapter with either:
            - callable: backend() -> dict
            - method:   backend.get_battery_status() -> dict
        """
        self.backend = backend

    # ------------------------------------------------------------
    # Low-level read
    # ------------------------------------------------------------

    def _read_backend(self) -> Dict[str, Any]:
        """Safe backend read with full isolation."""
        if self.backend is None:
            return {}

        try:
            if callable(self.backend):
                return self.backend() or {}
            if hasattr(self.backend, "get_battery_status"):
                return self.backend.get_battery_status() or {}
        except Exception as e:
            print(f"[WARN] Battery backend failed: {e}")

        return {}

    # ------------------------------------------------------------
    # Normalized status (v3)
    # ------------------------------------------------------------

    def get_status(self) -> Dict[str, Any]:
        raw = self._read_backend()

        # Level (0–100)
        level = raw.get("level")
        if isinstance(level, (int, float)):
            if level < 0:
                level = 0
            if level > 100:
                level = 100
        else:
            level = None

        # Charging
        charging = raw.get("charging")
        if charging not in (True, False):
            charging = None

        # Temperature (°C)
        temperature = raw.get("temp")
        if temperature is None:
            temperature = raw.get("temperature")

        if isinstance(temperature, (int, float)):
            # Safety clamp
            if temperature < -20:
                temperature = -20
            if temperature > 90:
                temperature = 90
        else:
            temperature = None

        # Optional fields
        health = raw.get("health")
        voltage = raw.get("voltage")

        # Source metadata
        source = raw.get("source", "unknown")

        return {
            "module": "battery",
            "version": self.MODULE_VERSION,
            "level": level,
            "charging": charging,
            "temperature": temperature,
            "health": health,
            "voltage": voltage,
            "source": source,
        }

    # ------------------------------------------------------------
    # Event handling
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:

        if event.type != MobileEventTypes.CHECK_BATTERY:
            return {
                "status": "ignored",
                "reason": "unsupported_event",
                "event_type": event.type,
                "module": "battery",
            }

        status = self.get_status()

        return {
            "status": "ok",
            "event_type": MobileEventTypes.CHECK_BATTERY,
            "module": "battery",
            "battery": status,
        }

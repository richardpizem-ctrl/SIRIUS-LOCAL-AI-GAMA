# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Battery System Module
# Version: 3.0.0-pre
# ============================================================

from typing import Any, Dict, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileBatteryModule:

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, backend: Optional[Any] = None):
        self.backend = backend

    # ------------------------------------------------------------
    # Low-level read
    # ------------------------------------------------------------

    def _read_backend(self) -> Dict[str, Any]:
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
    # Normalized status
    # ------------------------------------------------------------

    def get_status(self) -> Dict[str, Any]:
        raw = self._read_backend()

        level = raw.get("level")
        charging = raw.get("charging")

        # temperature: safe fallback
        temperature = raw.get("temp")
        if temperature is None:
            temperature = raw.get("temperature")

        # optional fields
        health = raw.get("health")
        voltage = raw.get("voltage")

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

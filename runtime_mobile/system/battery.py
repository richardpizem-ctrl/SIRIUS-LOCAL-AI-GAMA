# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Battery System Module
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Framework-agnostic battery status provider for the mobile runtime.
# - no direct OS / platform calls
# - expects an injected backend/adapter for real data
# - safe to use in offline / simulated environments
# ============================================================

from typing import Any, Dict, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileBatteryModule:
    """
    Battery status abstraction for the mobile runtime.

    Design:
    - `backend` is an optional callable or object that provides real battery data
    - if no backend is present, returns simulated / unknown-safe values
    - can be used directly or via diagnostics / dispatcher
    """

    MODULE_VERSION = "3.0.0-pre"

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
        """
        Read raw battery data from backend, if available.
        Must be side-effect free and safe to call often.
        """
        if self.backend is None:
            return {}

        try:
            if callable(self.backend):
                return self.backend() or {}
            if hasattr(self.backend, "get_battery_status"):
                return self.backend.get_battery_status() or {}
        except Exception as e:
            # Never propagate backend errors into runtime
            print(f"[WARN] Battery backend failed: {e}")

        return {}

    # ------------------------------------------------------------
    # Normalized status
    # ------------------------------------------------------------

    def get_status(self) -> Dict[str, Any]:
        """
        Return normalized battery status for diagnostics / UI.
        Keys are stable across platforms.
        """
        raw = self._read_backend()

        level = raw.get("level")          # 0–100 or None
        charging = raw.get("charging")    # bool or None
        temperature = raw.get("temp") or raw.get("temperature")  # °C or None
        source = raw.get("source", "unknown")

        return {
            "module": "battery",
            "version": self.MODULE_VERSION,
            "level": level,
            "charging": charging,
            "temperature": temperature,
            "source": source,
        }

    # ------------------------------------------------------------
    # Event handling
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:
        """
        Handle battery-related events.
        Intended to be called from diagnostics or dispatcher.
        """
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
            "module": "battery",
            "battery": status,
        }

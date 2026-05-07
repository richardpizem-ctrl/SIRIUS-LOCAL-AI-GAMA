# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Storage System Module
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Framework-agnostic storage status provider for the mobile runtime.
# - no direct OS / platform calls
# - expects an injected backend/adapter for real filesystem data
# - safe for offline / simulated environments
# ============================================================

from typing import Any, Dict, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileStorageModule:
    """
    Storage abstraction for the mobile runtime.

    Design:
    - backend optional (callable or object with get_storage_status())
    - if backend missing, returns safe simulated values
    - used by diagnostics and dispatcher
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, backend: Optional[Any] = None):
        """
        backend may be:
            - callable: backend() -> dict
            - object:   backend.get_storage_status() -> dict
        """
        self.backend = backend

    # ------------------------------------------------------------
    # Backend read
    # ------------------------------------------------------------

    def _read_backend(self) -> Dict[str, Any]:
        """Safely read raw storage data from backend."""
        if self.backend is None:
            return {}

        try:
            if callable(self.backend):
                return self.backend() or {}
            if hasattr(self.backend, "get_storage_status"):
                return self.backend.get_storage_status() or {}
        except Exception as e:
            print(f"[WARN] Storage backend failed: {e}")

        return {}

    # ------------------------------------------------------------
    # Normalized storage status
    # ------------------------------------------------------------

    def get_status(self) -> Dict[str, Any]:
        """
        Return normalized storage status.
        Keys are stable across all platforms.
        """
        raw = self._read_backend()

        total = raw.get("total") or raw.get("total_bytes")
        free = raw.get("free") or raw.get("free_bytes")
        used = raw.get("used") or (total - free if total and free else None)
        percent = None

        if total and used:
            try:
                percent = round((used / total) * 100, 2)
            except Exception:
                percent = None

        return {
            "module": "storage",
            "version": self.MODULE_VERSION,
            "total_bytes": total,
            "used_bytes": used,
            "free_bytes": free,
            "used_percent": percent,
        }

    # ------------------------------------------------------------
    # Event handling
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:
        """Handle CHECK_STORAGE event."""
        if event.type != MobileEventTypes.CHECK_STORAGE:
            return {
                "status": "ignored",
                "reason": "unsupported_event",
                "event_type": event.type,
                "module": "storage",
            }

        status = self.get_status()

        return {
            "status": "ok",
            "module": "storage",
            "storage": status,
        }

# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Storage System Module
# Version: 3.0.0-pre
# ============================================================

from typing import Any, Dict, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileStorageModule:

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
            if hasattr(self.backend, "get_storage_status"):
                return self.backend.get_storage_status() or {}
        except Exception as e:
            print(f"[WARN] Storage backend failed: {e}")

        return {}

    # ------------------------------------------------------------
    # Normalized storage status
    # ------------------------------------------------------------

    def get_status(self) -> Dict[str, Any]:
        raw = self._read_backend()

        # Safe extraction
        total = raw.get("total")
        if total is None:
            total = raw.get("total_bytes")

        free = raw.get("free")
        if free is None:
            free = raw.get("free_bytes")

        used = raw.get("used")
        if used is None and total is not None and free is not None:
            used = total - free

        # Validate values
        if total is not None and total < 0:
            total = None
        if free is not None and free < 0:
            free = None
        if used is not None and used < 0:
            used = None

        percent = None
        if total not in (None, 0) and used is not None:
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
            "event_type": MobileEventTypes.CHECK_STORAGE,
            "module": "storage",
            "storage": status,
        }

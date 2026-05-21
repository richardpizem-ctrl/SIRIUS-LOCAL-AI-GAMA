# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Storage System Module
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for GAMA Runtime 3.1:
# - normalized storage schema v3
# - safe validation of total/free/used
# - percent calculation with protection
# - backend fail-safe
# - diagnostics v3 compatibility
# - added storage health + io_load (optional)
# ============================================================

from typing import Any, Dict, Optional

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileStorageModule:

    MODULE_VERSION = "3.1.0"

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
        """Safe backend read with full isolation."""
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
    # Normalized storage status (v3)
    # ------------------------------------------------------------

    def get_status(self) -> Dict[str, Any]:
        raw = self._read_backend()

        # Extract values
        total = raw.get("total") or raw.get("total_bytes")
        free = raw.get("free") or raw.get("free_bytes")
        used = raw.get("used")

        # Compute used if missing
        if used is None and total is not None and free is not None:
            used = total - free

        # Validate numeric values
        if total is not None and total < 0:
            total = None
        if free is not None and free < 0:
            free = None
        if used is not None and used < 0:
            used = None

        # Percent
        percent = None
        if total not in (None, 0) and used is not None:
            try:
                percent = round((used / total) * 100, 2)
            except Exception:
                percent = None

        # Optional fields
        health = raw.get("health")          # e.g. "good", "warning", "critical"
        io_load = raw.get("io_load")        # e.g. 0–100 %
        source = raw.get("source", "unknown")

        return {
            "module": "storage",
            "version": self.MODULE_VERSION,
            "total_bytes": total,
            "used_bytes": used,
            "free_bytes": free,
            "used_percent": percent,
            "health": health,
            "io_load": io_load,
            "source": source,
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

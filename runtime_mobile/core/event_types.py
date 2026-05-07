# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Event Types
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Defines:
#   - MobileEvent (runtime event container)
#   - MobileEventTypes (centralized event constants)
#
# GAMA 3-ready features:
#   - unified event metadata
#   - safe payload access
#   - serialization
#   - extended event categories (diagnostics, governor, scene)
#   - stable API for router + dispatcher + modules
# ============================================================

from typing import Any, Dict, Optional


# ------------------------------------------------------------
# MobileEvent
# ------------------------------------------------------------

class MobileEvent:
    """
    Base event class for the GAMA mobile runtime.

    Each event contains:
    - type (string)
    - payload (dict)
    - metadata (optional future extension)
    """

    EVENT_VERSION = "3.0.0-pre"

    def __init__(self, event_type: str, payload: Optional[Dict[str, Any]] = None):
        self.type = event_type
        self.payload = payload if payload is not None else {}

    # Safe getter
    def get(self, key: str, default=None):
        return self.payload.get(key, default)

    # Serialization
    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "payload": self.payload,
            "version": self.EVENT_VERSION,
        }

    def __repr__(self):
        return f"<MobileEvent type={self.type} payload={self.payload}>"


# ------------------------------------------------------------
# MobileEventTypes
# ------------------------------------------------------------

class MobileEventTypes:
    """
    Centralized list of event type constants for the mobile runtime.
    Used by:
    - NL Router
    - Dispatcher
    - RuntimeCore
    - Vision / Security / Knowledge
    - Diagnostics / Energy Governor
    """

    VERSION = "3.0.0-pre"

    # --------------------------------------------------------
    # System / Runtime
    # --------------------------------------------------------
    UNKNOWN = "UNKNOWN"
    OPEN_APP = "OPEN_APP"
    SHOW_HELP = "SHOW_HELP"
    HEARTBEAT = "HEARTBEAT"
    RUNTIME_INFO = "RUNTIME_INFO"

    # --------------------------------------------------------
    # Device Diagnostics (GAMA 2.0 → 3.0)
    # --------------------------------------------------------
    CHECK_BATTERY = "CHECK_BATTERY"
    CHECK_THERMAL = "CHECK_THERMAL"
    CHECK_MEMORY = "CHECK_MEMORY"
    CHECK_STORAGE = "CHECK_STORAGE"
    DIAGNOSTICS_REPORT = "DIAGNOSTICS_REPORT"

    # --------------------------------------------------------
    # Energy Governor (GAMA 2.0 → 3.0)
    # --------------------------------------------------------
    GOVERNOR_POLICY_UPDATE = "GOVERNOR_POLICY_UPDATE"
    GOVERNOR_BLOCK = "GOVERNOR_BLOCK"

    # --------------------------------------------------------
    # Security Module
    # --------------------------------------------------------
    SECURITY = "SECURITY"
    PERMISSION_CHECK = "PERMISSION_CHECK"
    RESTRICTED_MODE = "RESTRICTED_MODE"

    # --------------------------------------------------------
    # Vision Module
    # --------------------------------------------------------
    VISION = "VISION"
    OCR = "OCR"
    DETECT = "DETECT"
    SCENE = "SCENE"
    HOMEWORK = "HOMEWORK"

    # --------------------------------------------------------
    # Knowledge Packs
    # --------------------------------------------------------
    PACK_LOOKUP = "PACK_LOOKUP"
    PACK_INFO = "PACK_INFO"

    # --------------------------------------------------------
    # Workflow Engine 2.0 / 3.0
    # --------------------------------------------------------
    WORKFLOW_START = "WORKFLOW_START"
    WORKFLOW_STEP = "WORKFLOW_STEP"
    WORKFLOW_COMPLETE = "WORKFLOW_COMPLETE"
    WORKFLOW_ABORT = "WORKFLOW_ABORT"

    # --------------------------------------------------------
    # LAN Offline Bridge
    # --------------------------------------------------------
    LAN_MESSAGE = "LAN_MESSAGE"
    LAN_SYNC = "LAN_SYNC"
    LAN_STATUS = "LAN_STATUS"

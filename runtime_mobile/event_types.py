# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Event Types
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Centralized list of event types for the mobile runtime.
# Used by:
# - UI Engine
# - Vision Engine
# - Workflow Engine
# - Knowledge Packs
# - Diagnostics
# - Security Engine
# - LAN Bridge
# - Assistant Engine
# ============================================================

class MobileEventTypes:
    """Centralized list of event types for the mobile runtime."""

    VERSION = "3.1.0"

    # --------------------------------------------------------
    # System / Runtime
    # --------------------------------------------------------
    UNKNOWN = "UNKNOWN"
    OPEN_APP = "OPEN_APP"
    SHOW_HELP = "SHOW_HELP"
    HEARTBEAT = "HEARTBEAT"
    RUNTIME_INFO = "RUNTIME_INFO"
    APP_STATE = "APP_STATE"              # NEW (3.1)
    APP_RESUME = "APP_RESUME"            # NEW (3.1)
    APP_PAUSE = "APP_PAUSE"              # NEW (3.1)

    # --------------------------------------------------------
    # Text / Queries / Assistant
    # --------------------------------------------------------
    TEXT_QUERY = "TEXT_QUERY"
    ASSISTANT = "ASSISTANT"
    ASSISTANT_CONTEXT = "ASSISTANT_CONTEXT"  # NEW (3.1)

    # --------------------------------------------------------
    # Device Diagnostics
    # --------------------------------------------------------
    CHECK_BATTERY = "CHECK_BATTERY"
    CHECK_THERMAL = "CHECK_THERMAL"
    CHECK_MEMORY = "CHECK_MEMORY"
    CHECK_STORAGE = "CHECK_STORAGE"
    DIAGNOSTICS_REPORT = "DIAGNOSTICS_REPORT"
    DEVICE_INFO = "DEVICE_INFO"              # NEW (3.1)

    # --------------------------------------------------------
    # Energy Governor
    # --------------------------------------------------------
    GOVERNOR_POLICY_UPDATE = "GOVERNOR_POLICY_UPDATE"
    GOVERNOR_BLOCK = "GOVERNOR_BLOCK"
    GOVERNOR_STATE = "GOVERNOR_STATE"        # NEW (3.1)

    # --------------------------------------------------------
    # Security
    # --------------------------------------------------------
    SECURITY = "SECURITY"
    PERMISSION_CHECK = "PERMISSION_CHECK"
    RESTRICTED_MODE = "RESTRICTED_MODE"
    SECURITY_ALERT = "SECURITY_ALERT"        # NEW (3.1)

    # --------------------------------------------------------
    # Vision
    # --------------------------------------------------------
    VISION = "VISION"
    OCR = "OCR"
    DETECT = "DETECT"
    SCENE = "SCENE"
    ANALYZE = "ANALYZE"
    HOMEWORK = "HOMEWORK"
    VISION_CAPABILITIES = "VISION_CAPABILITIES"  # NEW (3.1)

    # --------------------------------------------------------
    # Knowledge Packs
    # --------------------------------------------------------
    PACK_LOOKUP = "PACK_LOOKUP"
    PACK_INFO = "PACK_INFO"
    PACK_QUERY = "PACK_QUERY"
    PACK_SUGGEST = "PACK_SUGGEST"            # NEW (3.1)

    # --------------------------------------------------------
    # Workflow Engine
    # --------------------------------------------------------
    WORKFLOW_START = "WORKFLOW_START"
    WORKFLOW_STEP = "WORKFLOW_STEP"
    WORKFLOW_COMPLETE = "WORKFLOW_COMPLETE"
    WORKFLOW_ABORT = "WORKFLOW_ABORT"
    WORKFLOW_ERROR = "WORKFLOW_ERROR"        # NEW (3.1)

    # --------------------------------------------------------
    # LAN Offline Bridge
    # --------------------------------------------------------
    LAN_MESSAGE = "LAN_MESSAGE"
    LAN_SYNC = "LAN_SYNC"
    LAN_STATUS = "LAN_STATUS"
    LAN_DISCOVERY = "LAN_DISCOVERY"          # NEW (3.1)

    # --------------------------------------------------------
    # Metadata
    # --------------------------------------------------------
    @classmethod
    def get_all(cls):
        """Return all event types as a list."""
        return [
            v for k, v in cls.__dict__.items()
            if k.isupper() and isinstance(v, str)
        ]

    @classmethod
    def get_info(cls):
        return {
            "module": "runtime_mobile.event_types",
            "version": cls.VERSION,
            "count": len(cls.get_all()),
            "events": cls.get_all(),
        }

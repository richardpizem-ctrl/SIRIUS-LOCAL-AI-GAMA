# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Event Types
# Version: 3.0.0-pre
# ============================================================

class MobileEventTypes:
    """
    Centralized list of event type constants for the mobile runtime.
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
    # Assistant
    # --------------------------------------------------------
    ASSISTANT = "ASSISTANT"
    TEXT_QUERY = "TEXT_QUERY"

    # --------------------------------------------------------
    # Device Diagnostics
    # --------------------------------------------------------
    CHECK_BATTERY = "CHECK_BATTERY"
    CHECK_THERMAL = "CHECK_THERMAL"
    CHECK_MEMORY = "CHECK_MEMORY"
    CHECK_STORAGE = "CHECK_STORAGE"
    DIAGNOSTICS_REPORT = "DIAGNOSTICS_REPORT"

    # --------------------------------------------------------
    # Energy Governor
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
    PACK_QUERY = "PACK_QUERY"

    # --------------------------------------------------------
    # Workflow Engine
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

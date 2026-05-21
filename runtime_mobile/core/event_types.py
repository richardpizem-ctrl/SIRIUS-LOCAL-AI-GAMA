# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Event Types
# Version: 3.1.0
# ============================================================

class MobileEventTypes:
    """
    Centralized list of event type constants for the GAMA 3.1 runtime.
    Includes new event types for:
    - SCENE v1
    - Hybrid Schoolwork v1
    - Multi-intent routing
    - Diagnostics v3
    """

    VERSION = "3.1.0"

    # --------------------------------------------------------
    # System / Runtime
    # --------------------------------------------------------
    UNKNOWN = "UNKNOWN"
    OPEN_APP = "OPEN_APP"
    SHOW_HELP = "SHOW_HELP"
    HEARTBEAT = "HEARTBEAT"
    RUNTIME_INFO = "RUNTIME_INFO"
    SYSTEM_TRACE = "SYSTEM_TRACE"          # NEW (Diagnostics v3)

    # --------------------------------------------------------
    # Assistant / Text
    # --------------------------------------------------------
    ASSISTANT = "ASSISTANT"
    TEXT_QUERY = "TEXT_QUERY"
    MULTI_INTENT = "MULTI_INTENT"          # NEW (multi-intent routing)

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
    SCENE = "SCENE"                         # UPDATED (SCENE v1)
    ANALYZE = "ANALYZE"                     # NEW (Vision pipeline v3)

    # --------------------------------------------------------
    # Schoolwork / Hybrid Input
    # --------------------------------------------------------
    HOMEWORK = "HOMEWORK"
    SCHOOLWORK_HYBRID = "SCHOOLWORK_HYBRID"  # NEW (Hybrid input v1)

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

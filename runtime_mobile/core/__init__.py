# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Core Package
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Public API surface for the mobile runtime core.
# Provides unified imports for all runtime modules.
#
# Updated for GAMA Runtime 3.1:
# - MobileEvent v3.1
# - MobileEventTypes v3.1
# - Dispatcher v3.1 (multi-intent routing)
# - Router v3.1 (NLRouter v3)
# - Context v3.1 (metadata v3, restricted mode v3)
# ============================================================

from .runtime_core import MobileRuntimeCore
from .runtime_context import MobileRuntimeContext
from .runtime_dispatcher import MobileRuntimeDispatcher
from .mobile_event import MobileEvent
from .event_types import MobileEventTypes
from .router_mobile import MobileNLRouter

__all__ = [
    "MobileRuntimeCore",
    "MobileRuntimeContext",
    "MobileRuntimeDispatcher",
    "MobileEvent",
    "MobileEventTypes",
    "MobileNLRouter",
]

# Package version (for diagnostics, debugging, metadata)
RUNTIME_CORE_VERSION = "3.1.0"

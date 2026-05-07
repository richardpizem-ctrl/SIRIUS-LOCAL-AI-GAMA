# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Core Package
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# This file exposes the public API of the mobile runtime core.
# All modules, engines, and runtime components import from here.
#
# GAMA 3-ready features:
#   - unified import surface
#   - stable public API for all runtime modules
#   - versioned architecture
#   - compatibility with new modules (diagnostics, governor, scene)
#   - clean namespace for external integrations
# ============================================================

from .runtime_core import MobileRuntimeCore
from .runtime_context import MobileRuntimeContext
from .runtime_dispatcher import MobileRuntimeDispatcher
from .event import MobileEvent
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
RUNTIME_CORE_VERSION = "3.0.0-pre"

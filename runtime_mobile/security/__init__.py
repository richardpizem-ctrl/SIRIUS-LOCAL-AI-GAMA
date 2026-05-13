# ============================================================
# SIRIUS LOCAL AI GAMA - Security Package
# Version: 3.0.0-pre
# ============================================================

"""
Security subsystem initializer.

Exposes:
- SecurityModule: main security engine
- MobilePermissions: lightweight permission model
- SecurityEntry: high-level event handler for runtime dispatcher
"""

from .security_module import SecurityModule
from .security_entry import SecurityEntry
from runtime_mobile.core.permissions import MobilePermissions

__all__ = [
    "SecurityModule",
    "SecurityEntry",
    "MobilePermissions",
]


# ============================================================
# SIRIUS LOCAL AI GAMA - Security Package
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Security subsystem initializer.
#
# Exposes:
# - SecurityModule: core security engine
# - SecurityEntry: high-level event handler for dispatcher
# - MobilePermissions: lightweight permission model (OWNER/FAMILY/STRANGER)
#
# Updated for GAMA Runtime 3.1:
# - unified export surface
# - restricted_mode sync with permissions
# - consistent metadata header
# ============================================================

from .security_module import SecurityModule
from .security_entry import SecurityEntry
from runtime_mobile.core.permissions import MobilePermissions

__all__ = [
    "SecurityModule",
    "SecurityEntry",
    "MobilePermissions",
]

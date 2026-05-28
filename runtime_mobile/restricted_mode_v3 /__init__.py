"""
restricted_mode_v3
------------------
Restricted Mode module for SIRIUS Mobile Runtime 3.3.0.

Responsibilities:
- Enforce strict behavioral policies
- Filter unsafe or disallowed actions
- Provide deterministic rule evaluation
- Integrate with Sandbox Enforcement v3
- Support SchoolMode v2 and Family Security 3.x

This package is fully deterministic:
- No dynamic imports
- No reflection
- No eval/exec
Prepared for Self‑Repair Layer 4.4.
"""

from .restricted_router import RestrictedRouter
from .restricted_policy import RestrictedPolicy
from .restricted_filters import RestrictedFilters

__all__ = [
    "RestrictedRouter",
    "RestrictedPolicy",
    "RestrictedFilters",
]


# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Core
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Package initializer for the mobile runtime.
# Exposes core entrypoints and metadata.
# ============================================================

__all__ = [
    "get_runtime_info",
]

RUNTIME_VERSION = "3.0.0-pre"
RUNTIME_NAME = "SIRIUS LOCAL AI GAMA - Mobile Runtime"


def get_runtime_info():
    return {
        "name": RUNTIME_NAME,
        "version": RUNTIME_VERSION,
        "module": "runtime_mobile",
    }

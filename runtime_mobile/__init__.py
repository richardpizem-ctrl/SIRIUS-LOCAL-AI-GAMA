# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Core
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Package initializer for the mobile runtime.
# Exposes core entrypoints and metadata.
# ============================================================

__all__ = [
    "get_runtime_info",
    "RUNTIME_VERSION",
    "RUNTIME_NAME",
]

RUNTIME_VERSION = "3.1.0"
RUNTIME_NAME = "SIRIUS LOCAL AI GAMA - Mobile Runtime"


def get_runtime_info():
    return {
        "name": RUNTIME_NAME,
        "version": RUNTIME_VERSION,
        "module": "runtime_mobile",
        "engine": {
            "ui": "3.1.0",
            "vision": "3.1.0",
            "screen": "3.1.0",
            "layouts": "3.1.0",
        },
        "status": "ok",
    }

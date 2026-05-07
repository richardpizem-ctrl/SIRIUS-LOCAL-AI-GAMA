# ============================================================
# SIRIUS LOCAL AI GAMA - Base Module Class
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# This is the unified base class for ALL mobile modules in GAMA.
# Every module in versions 2.x and 3.x MUST inherit from this.
#
# Provides:
#   - lifecycle management (load/unload/reload)
#   - module state tracking
#   - versioning
#   - dependency hooks
#   - runtime integration hooks
#   - error-safe loading
# ============================================================

from typing import Optional


class BaseModule:
    """
    Base class for all GAMA mobile modules.
    Every module must inherit from this class.

    Version 3-ready features:
    - unified lifecycle API
    - safe load/unload with error handling
    - dependency injection hooks
    - runtime registration hooks
    - metadata + versioning
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, name: str):
        self.name = name
        self.loaded = False
        self.runtime = None  # runtime_mobile reference (injected)
        self.dependencies = []  # list of module names this module depends on

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def load(self) -> bool:
        """
        Load module resources.
        Returns True if loaded successfully.
        """
        try:
            self.on_load()
            self.loaded = True
            return True
        except Exception as e:
            self.loaded = False
            print(f"[ERROR] Module '{self.name}' failed to load: {e}")
            return False

    def unload(self) -> bool:
        """
        Unload module resources.
        Returns True if unloaded successfully.
        """
        try:
            self.on_unload()
            self.loaded = False
            return True
        except Exception as e:
            print(f"[ERROR] Module '{self.name}' failed to unload: {e}")
            return False

    def reload(self) -> bool:
        """
        Reload module resources safely.
        """
        self.unload()
        return self.load()

    # ------------------------------------------------------------
    # Hooks (to be overridden by child modules)
    # ------------------------------------------------------------

    def on_load(self):
        """Executed when module is loaded. Override in child modules."""
        pass

    def on_unload(self):
        """Executed when module is unloaded. Override in child modules."""
        pass

    # ------------------------------------------------------------
    # Runtime Integration
    # ------------------------------------------------------------

    def attach_runtime(self, runtime):
        """
        Inject runtime_mobile reference.
        Called automatically by MobileRuntimeCore.
        """
        self.runtime = runtime

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
        """
        Returns module metadata for diagnostics, debugging, UI, etc.
        """
        return {
            "name": self.name,
            "version": self.MODULE_VERSION,
            "loaded": self.loaded,
            "dependencies": self.dependencies,
            "runtime_attached": self.runtime is not None,
        }

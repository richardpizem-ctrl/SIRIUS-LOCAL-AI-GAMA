# ============================================================
# SIRIUS LOCAL AI GAMA - Base Module Class
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Unified base class for ALL mobile modules in GAMA.
# Compatible with versions 2.x and 3.x.
#
# Provides:
#   - lifecycle management
#   - module state tracking
#   - versioning
#   - dependency hooks
#   - runtime integration hooks
#   - event hook (3.x)
#   - error-safe loading
# ============================================================


class BaseModule:
    """
    Base class for all GAMA mobile modules.

    Version 3-ready features:
    - unified lifecycle API
    - safe load/unload with error handling
    - dependency injection hooks
    - runtime registration hooks
    - event hook
    - metadata + versioning
    """

    MODULE_VERSION = "3.0.0-pre"

    def __init__(self, name: str):
        self.name = name
        self.loaded = False
        self.runtime = None
        self.dependencies = []

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def load(self) -> bool:
        try:
            self.on_load()
            self.loaded = True
            return True
        except Exception as e:
            self.loaded = False
            print(f"[ERROR] Module '{self.name}' failed to load: {e}")
            return False

    def unload(self) -> bool:
        try:
            self.on_unload()
            self.loaded = False
            return True
        except Exception as e:
            print(f"[ERROR] Module '{self.name}' failed to unload: {e}")
            return False

    def reload(self) -> bool:
        self.unload()
        return self.load()

    # ------------------------------------------------------------
    # Hooks (override in child modules)
    # ------------------------------------------------------------

    def on_load(self):
        pass

    def on_unload(self):
        pass

    def on_event(self, event):
        """
        Passive event hook.
        Child modules may override this.
        """
        pass

    # ------------------------------------------------------------
    # Runtime Integration
    # ------------------------------------------------------------

    def attach_runtime(self, runtime):
        self.runtime = runtime

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> dict:
        return {
            "name": self.name,
            "version": self.MODULE_VERSION,
            "loaded": self.loaded,
            "dependencies": self.dependencies,
            "runtime_attached": self.runtime is not None,
        }

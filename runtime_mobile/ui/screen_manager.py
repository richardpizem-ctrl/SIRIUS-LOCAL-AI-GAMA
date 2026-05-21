# ============================================================
# SIRIUS LOCAL AI GAMA - Screen Manager
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - safe lifecycle pipeline
# - event bubbling
# - stack navigation v3
# - screen initialization safety
# - unified metadata schema v3
# ============================================================

class ScreenManager:

    COMPONENT_VERSION = "3.1.0"

    def __init__(self):
        self.screens = {}
        self.stack = []
        self.active_screen = None

    # ------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------

    def register_screen(self, name: str, screen_obj):
        if not hasattr(screen_obj, "render"):
            return {"status": "error", "message": "Invalid screen object"}

        # Inject screen_manager reference
        screen_obj.screen_manager = self

        self.screens[name] = screen_obj
        return {"status": "registered", "screen": name}

    # ------------------------------------------------------------
    # Direct switching
    # ------------------------------------------------------------

    def set_screen(self, name: str):
        if name not in self.screens:
            return {"status": "error", "message": f"Screen '{name}' not found"}

        # Hide previous
        if self.active_screen and hasattr(self.active_screen, "on_hide"):
            try:
                self.active_screen.on_hide()
            except Exception:
                pass

        self.active_screen = self.screens[name]
        self.stack = [name]

        # Initialize + show
        try:
            if hasattr(self.active_screen, "initialize"):
                self.active_screen.initialize()
        except Exception:
            pass

        try:
            if hasattr(self.active_screen, "on_show"):
                self.active_screen.on_show()
        except Exception:
            pass

        return {"status": "screen_set", "screen": name}

    # ------------------------------------------------------------
    # Stack navigation (v3)
    # ------------------------------------------------------------

    def push(self, name: str):
        if name not in self.screens:
            return {"status": "error", "message": f"Screen '{name}' not found"}

        # Hide current
        if self.active_screen and hasattr(self.active_screen, "on_hide"):
            try:
                self.active_screen.on_hide()
            except Exception:
                pass

        self.stack.append(name)
        self.active_screen = self.screens[name]

        try:
            if hasattr(self.active_screen, "initialize"):
                self.active_screen.initialize()
        except Exception:
            pass

        try:
            if hasattr(self.active_screen, "on_show"):
                self.active_screen.on_show()
        except Exception:
            pass

        return {"status": "pushed", "screen": name}

    def pop(self):
        if len(self.stack) <= 1:
            return {"status": "error", "message": "Cannot pop root screen"}

        # Hide current
        if self.active_screen and hasattr(self.active_screen, "on_hide"):
            try:
                self.active_screen.on_hide()
            except Exception:
                pass

        self.stack.pop()
        previous = self.stack[-1]
        self.active_screen = self.screens[previous]

        try:
            if hasattr(self.active_screen, "on_show"):
                self.active_screen.on_show()
        except Exception:
            pass

        return {"status": "popped", "screen": previous}

    # ------------------------------------------------------------
    # Update + Render
    # ------------------------------------------------------------

    def update(self):
        if self.active_screen and hasattr(self.active_screen, "update"):
            try:
                return {
                    "status": "updated",
                    "screen": self.stack[-1],
                    "data": self.active_screen.update()
                }
            except Exception as e:
                return {"status": "error", "error": str(e)}

        return {"status": "no_active_screen"}

    def render(self):
        if self.active_screen and hasattr(self.active_screen, "render"):
            try:
                return {
                    "status": "rendered",
                    "screen": self.stack[-1],
                    "data": self.active_screen.render()
                }
            except Exception as e:
                return {"status": "error", "error": str(e)}

        return {"status": "no_active_screen"}

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        if self.active_screen and hasattr(self.active_screen, "on_event"):
            try:
                return self.active_screen.on_event(event)
            except Exception as e:
                return {"status": "error", "error": str(e)}

        return {"status": "ignored", "event": event, "bubble": True}

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "type": "screen_manager",
            "version": self.COMPONENT_VERSION,
            "registered_screens": list(self.screens.keys()),
            "stack": list(self.stack),
            "active_screen": self.stack[-1] if self.stack else None
        }

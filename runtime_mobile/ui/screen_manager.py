# ============================================================
# SIRIUS LOCAL AI GAMA - Screen Manager
# Version: 3.0.0-pre
# ============================================================

class ScreenManager:

    COMPONENT_VERSION = "3.0.0-pre"

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

        # Hide previous screen
        if self.active_screen and hasattr(self.active_screen, "on_hide"):
            self.active_screen.on_hide()

        self.active_screen = self.screens[name]
        self.stack = [name]

        # Initialize + show
        if hasattr(self.active_screen, "initialize"):
            self.active_screen.initialize()

        if hasattr(self.active_screen, "on_show"):
            self.active_screen.on_show()

        return {"status": "screen_set", "screen": name}

    # ------------------------------------------------------------
    # Stack navigation
    # ------------------------------------------------------------

    def push(self, name: str):
        if name not in self.screens:
            return {"status": "error", "message": f"Screen '{name}' not found"}

        # Hide current
        if self.active_screen and hasattr(self.active_screen, "on_hide"):
            self.active_screen.on_hide()

        self.stack.append(name)
        self.active_screen = self.screens[name]

        if hasattr(self.active_screen, "initialize"):
            self.active_screen.initialize()

        if hasattr(self.active_screen, "on_show"):
            self.active_screen.on_show()

        return {"status": "pushed", "screen": name}

    def pop(self):
        if len(self.stack) <= 1:
            return {"status": "error", "message": "Cannot pop root screen"}

        # Hide current
        if self.active_screen and hasattr(self.active_screen, "on_hide"):
            self.active_screen.on_hide()

        self.stack.pop()
        previous = self.stack[-1]
        self.active_screen = self.screens[previous]

        if hasattr(self.active_screen, "on_show"):
            self.active_screen.on_show()

        return {"status": "popped", "screen": previous}

    # ------------------------------------------------------------
    # Update + Render
    # ------------------------------------------------------------

    def update(self):
        if self.active_screen and hasattr(self.active_screen, "update"):
            return {
                "status": "updated",
                "screen": self.stack[-1],
                "data": self.active_screen.update()
            }

        return {"status": "no_active_screen"}

    def render(self):
        if self.active_screen and hasattr(self.active_screen, "render"):
            return {
                "status": "rendered",
                "screen": self.stack[-1],
                "data": self.active_screen.render()
            }

        return {"status": "no_active_screen"}

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        if self.active_screen and hasattr(self.active_screen, "on_event"):
            return self.active_screen.on_event(event)

        return {"status": "ignored", "event": event}

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "type": "screen_manager",
            "registered_screens": list(self.screens.keys()),
            "stack": list(self.stack),
            "active_screen": self.stack[-1] if self.stack else None
        }

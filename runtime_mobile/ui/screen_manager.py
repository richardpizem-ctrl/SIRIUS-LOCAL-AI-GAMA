# ============================================================
# SIRIUS LOCAL AI GAMA - Screen Manager
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Central navigation controller for mobile UI.
# Handles screen registration, switching, and stack navigation.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

class ScreenManager:
    """
    Central navigation controller for mobile UI.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self):
        # Registered screens: { "home": ScreenObject, ... }
        self.screens = {}

        # Navigation stack for push/pop navigation
        self.stack = []

        # Currently active screen object
        self.active_screen = None

    # ------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------

    def register_screen(self, name: str, screen_obj):
        """
        Register a screen object under a name.
        """
        self.screens[name] = screen_obj
        return {"status": "registered", "screen": name}

    # ------------------------------------------------------------
    # Direct switching
    # ------------------------------------------------------------

    def set_screen(self, name: str):
        """
        Switch to a screen directly (clears stack).
        """
        if name not in self.screens:
            return {"status": "error", "message": f"Screen '{name}' not found"}

        self.active_screen = self.screens[name]
        self.stack = [name]

        if hasattr(self.active_screen, "on_show"):
            self.active_screen.on_show()

        return {"status": "screen_set", "screen": name}

    # ------------------------------------------------------------
    # Stack navigation
    # ------------------------------------------------------------

    def push(self, name: str):
        """
        Push a new screen on top of the stack.
        """
        if name not in self.screens:
            return {"status": "error", "message": f"Screen '{name}' not found"}

        self.stack.append(name)
        self.active_screen = self.screens[name]

        if hasattr(self.active_screen, "on_show"):
            self.active_screen.on_show()

        return {"status": "pushed", "screen": name}

    def pop(self):
        """
        Pop the current screen and return to the previous one.
        """
        if len(self.stack) <= 1:
            return {"status": "error", "message": "Cannot pop root screen"}

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
        """
        Update the active screen.
        """
        if self.active_screen and hasattr(self.active_screen, "update"):
            return self.active_screen.update()

        return {"status": "no_active_screen"}

    def render(self):
        """
        Render the active screen.
        """
        if self.active_screen and hasattr(self.active_screen, "render"):
            return self.active_screen.render()

        return {"status": "no_active_screen"}

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

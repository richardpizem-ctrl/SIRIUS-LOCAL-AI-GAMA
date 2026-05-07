# ============================================================
# SIRIUS LOCAL AI GAMA - UI Manager
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Central UI orchestrator for the Mobile Runtime.
# Manages layouts, components, lifecycle and update/render flow.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .main_window import MobileMainWindow
from .theme import MobileUITheme


class UIManager:
    """
    Central UI orchestrator.
    Controls:
    - main window
    - active layout
    - lifecycle pipeline
    - update/render loop
    """

    MANAGER_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context
        self.window = MobileMainWindow(context)
        self.active_layout = None
        self.initialized = False

    # ------------------------------------------------------------
    # Layout management
    # ------------------------------------------------------------

    def set_layout(self, layout):
        """Assign a layout as the active UI layout."""
        if not hasattr(layout, "render"):
            return {"status": "error", "reason": "invalid_layout"}

        self.active_layout = layout

        # Assign layout geometry to match window
        layout.x = 0
        layout.y = 0
        layout.width = self.window.width
        layout.height = self.window.height

        return {
            "status": "layout_set",
            "layout": layout.layout_id
        }

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        """Initialize window + layout + components."""
        win = self.window.initialize()

        layout_info = None
        if self.active_layout:
            layout_info = self.active_layout.initialize()

        self.initialized = True

        return {
            "status": "initialized",
            "manager_version": self.MANAGER_VERSION,
            "window": win,
            "layout": layout_info
        }

    def update(self):
        """Update window + layout."""
        if not self.initialized:
            return {"status": "error", "reason": "ui_not_initialized"}

        win = self.window.update()

        layout_info = None
        if self.active_layout:
            layout_info = self.active_layout.update()

        return {
            "status": "updated",
            "window": win,
            "layout": layout_info
        }

    def render(self):
        """Render window + layout (placeholder)."""
        if not self.initialized:
            return {"status": "error", "reason": "ui_not_initialized"}

        win_render = self.window.render()

        layout_render = None
        if self.active_layout:
            layout_render = self.active_layout.render()

        return {
            "status": "rendered",
            "window": win_render,
            "layout": layout_render
        }

    def shutdown(self):
        """Shutdown UI cleanly."""
        layout_info = None
        if self.active_layout:
            layout_info = self.active_layout.shutdown()

        win = self.window.shutdown()

        return {
            "status": "shutdown",
            "window": win,
            "layout": layout_info
        }

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Route events to window and active layout.
        """
        results = []

        if hasattr(self.window, "on_event"):
            results.append(self.window.on_event(event))

        if self.active_layout and hasattr(self.active_layout, "on_event"):
            results.append(self.active_layout.on_event(event))

        return {
            "status": "events_forwarded",
            "results": results
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "module": "ui.ui_manager",
            "version": self.MANAGER_VERSION,
            "window": self.window.get_info(),
            "layout": self.active_layout.get_info() if self.active_layout else None
        }

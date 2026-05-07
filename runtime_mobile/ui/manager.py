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
    # Layout Management
    # ------------------------------------------------------------

    def set_layout(self, layout):
        """Assign a layout as the active UI layout."""
        self.active_layout = layout
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

        layout_render = None
        if self.active_layout:
            layout_render = self.active_layout.render()

        return {
            "status": "rendered",
            "window_title": self.window.title,
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
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "module": "ui.ui_manager",
            "version": self.MANAGER_VERSION,
            "window": self.window.get_info(),
            "layout": self.active_layout.get_info() if self.active_layout else None
        }

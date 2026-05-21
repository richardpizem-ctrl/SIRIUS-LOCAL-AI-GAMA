# ============================================================
# SIRIUS LOCAL AI GAMA - UI Manager
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Central UI orchestrator for the Mobile Runtime.
# Manages:
# - main window
# - active layout
# - lifecycle pipeline
# - update/render loop
# - event bubbling
# - layout geometry sync
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
    - event routing (with bubbling)
    """

    MANAGER_VERSION = "3.1.0"

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

        # Sync geometry with window
        layout.x = 0
        layout.y = 0
        layout.width = self.window.width
        layout.height = self.window.height

        layout.needs_layout = True
        layout.dirty = True

        return {
            "status": "layout_set",
            "layout": layout.layout_id
        }

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        """Initialize window + layout + components."""
        try:
            win = self.window.initialize()
        except Exception as e:
            win = {"status": "error", "error": str(e)}

        layout_info = None
        if self.active_layout:
            try:
                layout_info = self.active_layout.initialize()
            except Exception as e:
                layout_info = {"status": "error", "error": str(e)}

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

        try:
            win = self.window.update()
        except Exception as e:
            win = {"status": "error", "error": str(e)}

        layout_info = None
        if self.active_layout:
            try:
                layout_info = self.active_layout.update()
            except Exception as e:
                layout_info = {"status": "error", "error": str(e)}

        return {
            "status": "updated",
            "window": win,
            "layout": layout_info
        }

    def render(self):
        """Render window + layout."""
        if not self.initialized:
            return {"status": "error", "reason": "ui_not_initialized"}

        try:
            win_render = self.window.render()
        except Exception as e:
            win_render = {"status": "error", "error": str(e)}

        layout_render = None
        if self.active_layout:
            try:
                layout_render = self.active_layout.render()
            except Exception as e:
                layout_render = {"status": "error", "error": str(e)}

        return {
            "status": "rendered",
            "window": win_render,
            "layout": layout_render
        }

    def shutdown(self):
        """Shutdown UI cleanly."""
        layout_info = None
        if self.active_layout:
            try:
                layout_info = self.active_layout.shutdown()
            except Exception as e:
                layout_info = {"status": "error", "error": str(e)}

        try:
            win = self.window.shutdown()
        except Exception as e:
            win = {"status": "error", "error": str(e)}

        return {
            "status": "shutdown",
            "window": win,
            "layout": layout_info
        }

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Route events to window and active layout.
        Both may bubble events upward.
        """
        results = []

        # Window first
        if hasattr(self.window, "on_event"):
            try:
                results.append(self.window.on_event(event))
            except Exception as e:
                results.append({"status": "error", "error": str(e), "source": "window"})

        # Layout second
        if self.active_layout and hasattr(self.active_layout, "on_event"):
            try:
                results.append(self.active_layout.on_event(event))
            except Exception as e:
                results.append({"status": "error", "error": str(e), "source": "layout"})

        return {
            "status": "events_forwarded",
            "results": results,
            "bubble": True
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

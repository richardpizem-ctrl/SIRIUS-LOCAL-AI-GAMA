# ============================================================
# SIRIUS LOCAL AI GAMA - Debug Screen
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - safe log rendering
# - scroll view v3 (momentum, clamping)
# - event bubbling
# - layout invalidation
# - unified metadata schema v3
# ============================================================

from ..components.text_label import TextLabel
from ..components.button import Button
from ..components.panel import Panel
from ..components.scroll_view import ScrollView
from ..layouts.vertical_layout import VerticalLayout


class DebugScreen:
    SCREEN_VERSION = "3.1.0"

    def __init__(self, screen_manager, debug_provider=None):
        self.screen_manager = screen_manager
        self.debug_provider = debug_provider
        self.layout = None

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_show(self):
        # Title
        title = TextLabel("Debug Menu")
        title.font_size = 20

        subtitle = TextLabel("Runtime Diagnostics")
        subtitle.font_size = 14

        # Back button
        btn_back = Button(
            text="← Back",
            on_click=lambda _: self.screen_manager.pop()
        )

        # Logs
        logs = []
        if callable(self.debug_provider):
            try:
                logs = self.debug_provider()
            except Exception as e:
                logs = [f"[ERROR] Debug provider failed: {e}"]

        log_layout = VerticalLayout()

        for line in logs:
            t = TextLabel(str(line))
            t.font_size = 12
            log_layout.add_component(t)

        scroll = ScrollView(layout=log_layout)

        # Main panel
        panel_layout = VerticalLayout()
        panel_layout.add_component(title)
        panel_layout.add_component(subtitle)
        panel_layout.add_component(btn_back)
        panel_layout.add_component(scroll)

        panel = Panel(layout=panel_layout)

        # Root layout
        root = VerticalLayout()
        root.add_component(panel)

        self.layout = root

    # ------------------------------------------------------------
    # Update + Render
    # ------------------------------------------------------------

    def update(self):
        if not self.layout:
            return {"status": "no_layout"}
        try:
            return self.layout.update()
        except Exception as e:
            return {"status": "error", "error": str(e)}

    def render(self):
        if not self.layout:
            return {"status": "no_layout"}
        try:
            return self.layout.render()
        except Exception as e:
            return {"status": "error", "error": str(e)}

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "type": "screen",
            "name": "debug_screen",
            "version": self.SCREEN_VERSION,
            "layout": self.layout.get_info() if self.layout else None
        }

# ============================================================
# SIRIUS LOCAL AI GAMA - Home Screen
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - event bubbling
# - safe rendering
# - layout invalidation
# - unified metadata schema v3
# ============================================================

from ..components.panel import Panel
from ..components.icon import Icon
from ..components.button import Button
from ..components.text_label import TextLabel
from ..layouts.vertical_layout import VerticalLayout


class HomeScreen:
    SCREEN_VERSION = "3.1.0"

    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.layout = None

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_show(self):
        # Title
        title = TextLabel("SIRIUS LOCAL AI GAMA")
        title.font_size = 22

        subtitle = TextLabel("Mobile Runtime UI 3.1.0")
        subtitle.font_size = 14

        # Icon
        icon = Icon("⚡", size=32)

        # Debug button
        btn_debug = Button(
            text="Open Debug Screen",
            on_click=lambda _: self.screen_manager.push("debug")
        )

        # Panel layout
        panel_layout = VerticalLayout()
        panel_layout.add_component(icon)
        panel_layout.add_component(title)
        panel_layout.add_component(subtitle)
        panel_layout.add_component(btn_debug)

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
            "name": "home_screen",
            "version": self.SCREEN_VERSION,
            "layout": self.layout.get_info() if self.layout else None
        }

# ============================================================
# SIRIUS LOCAL AI GAMA - Home Screen
# Version: 3.0.0-pre
# ============================================================

from ..components.panel import Panel
from ..components.icon import Icon
from ..components.button import Button
from ..components.text_label import TextLabel
from ..layouts.vertical_layout import VerticalLayout


class HomeScreen:
    SCREEN_VERSION = "3.0.0-pre"

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

        subtitle = TextLabel("Mobile Runtime UI 3.0.0")
        subtitle.font_size = 14

        # Icon
        icon = Icon("⚡", size=32)

        # Debug button
        btn_debug = Button(
            text="Open Debug Screen",
            on_click=lambda: self.screen_manager.push("debug")
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
        return self.layout.update() if self.layout else {"status": "no_layout"}

    def render(self):
        return self.layout.render() if self.layout else {"status": "no_layout"}

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "type": "screen",
            "name": "home_screen",
            "version": self.SCREEN_VERSION
        }

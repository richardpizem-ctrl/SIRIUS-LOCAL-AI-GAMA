# ============================================================
# SIRIUS LOCAL AI GAMA - Home Screen
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Main entry screen for the mobile UI.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from ..components.panel import Panel
from ..components.icon import Icon
from ..components.button import Button
from ..components.text import Text
from ..layouts.vertical_layout import VerticalLayout


class HomeScreen:
    """
    Main entry screen for the mobile UI.
    """

    SCREEN_VERSION = "3.0.0-pre"

    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.layout = None

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_show(self):
        """
        Called when the screen becomes active.
        Build UI layout here.
        """

        title = Text("SIRIUS LOCAL AI GAMA", size=22, weight="bold")
        subtitle = Text("Mobile Runtime UI 3.0.0", size=14)

        icon = Icon("⚡", size=32)

        btn_debug = Button(
            label="Open Debug Screen",
            on_click=lambda: self.screen_manager.push("debug")
        )

        panel = Panel(
            content=VerticalLayout([
                icon,
                title,
                subtitle,
                btn_debug
            ])
        )

        self.layout = VerticalLayout([panel])

    # ------------------------------------------------------------
    # Update + Render
    # ------------------------------------------------------------

    def update(self):
        if self.layout:
            return self.layout.update()
        return {"status": "no_layout"}

    def render(self):
        if self.layout:
            return self.layout.render()
        return {"status": "no_layout"}

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "type": "screen",
            "name": "home_screen",
            "version": self.SCREEN_VERSION
        }

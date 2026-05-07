# ============================================================
# SIRIUS LOCAL AI GAMA - Debug Screen
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Diagnostic and development screen for mobile UI.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from ..components.text import Text
from ..components.button import Button
from ..components.panel import Panel
from ..components.scroll_view import ScrollView
from ..layouts.vertical_layout import VerticalLayout


class DebugScreen:
    """
    Diagnostic and development screen for mobile UI.
    """

    SCREEN_VERSION = "3.0.0-pre"

    def __init__(self, screen_manager, debug_provider=None):
        self.screen_manager = screen_manager
        self.debug_provider = debug_provider  # function returning list of log strings
        self.layout = None

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def on_show(self):
        """
        Called when the screen becomes active.
        Build UI layout here.
        """

        title = Text("Debug Menu", size=20, weight="bold")
        subtitle = Text("Runtime Diagnostics", size=14)

        btn_back = Button(
            label="← Back",
            on_click=lambda: self.screen_manager.pop()
        )

        # Load logs from provider
        logs = []
        if self.debug_provider:
            logs = self.debug_provider()

        log_texts = [Text(line, size=12) for line in logs]

        scroll = ScrollView(
            layout=VerticalLayout(log_texts)
        )

        panel = Panel(
            content=VerticalLayout([
                title,
                subtitle,
                btn_back,
                scroll
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
            "name": "debug_screen",
            "version": self.SCREEN_VERSION
        }

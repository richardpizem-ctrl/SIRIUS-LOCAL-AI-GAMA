# ============================================================
# SIRIUS LOCAL AI GAMA - Debug Screen
# Version: 3.0.0-pre
# ============================================================

from ..components.text_label import TextLabel
from ..components.button import Button
from ..components.panel import Panel
from ..components.scroll_view import ScrollView
from ..layouts.vertical_layout import VerticalLayout


class DebugScreen:
    SCREEN_VERSION = "3.0.0-pre"

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
            on_click=lambda: self.screen_manager.pop()
        )

        # Logs
        logs = self.debug_provider() if self.debug_provider else []
        log_layout = VerticalLayout()

        for line in logs:
            t = TextLabel(line)
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
        return self.layout.update() if self.layout else {"status": "no_layout"}

    def render(self):
        return self.layout.render() if self.layout else {"status": "no_layout"}

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "type": "screen",
            "name": "debug_screen",
            "version": self.SCREEN_VERSION
        }

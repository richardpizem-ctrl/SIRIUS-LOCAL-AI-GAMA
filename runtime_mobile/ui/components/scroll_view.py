# ============================================================
# SIRIUS LOCAL AI GAMA - Scroll View Component
# Version: 3.0.0-pre
# ============================================================

from .container import Container
from ..theme import MobileUITheme


class ScrollView(Container):

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, layout=None, component_id=None, visible=True):
        super().__init__(layout=layout, component_id=component_id, visible=visible)

        self.scroll_x = 0
        self.scroll_y = 0

        self.scroll_speed = 20
        self.enable_vertical = True
        self.enable_horizontal = False

        self.background = MobileUITheme.COLORS["surface"]
        self.padding = MobileUITheme.SPACING["md"]

    # ------------------------------------------------------------
    # Scroll control
    # ------------------------------------------------------------

    def set_scroll(self, x=None, y=None):
        if x is not None and self.enable_horizontal:
            self.scroll_x = max(0, x)
        if y is not None and self.enable_vertical:
            self.scroll_y = max(0, y)
        return {"status": "scroll_set", "x": self.scroll_x, "y": self.scroll_y}

    def scroll_up(self):
        if self.enable_vertical:
            self.scroll_y = max(0, self.scroll_y - self.scroll_speed)
        return {"status": "scrolled_up", "scroll_y": self.scroll_y}

    def scroll_down(self):
        if self.enable_vertical:
            self.scroll_y = max(0, self.scroll_y + self.scroll_speed)
        return {"status": "scrolled_down", "scroll_y": self.scroll_y}

    def scroll_left(self):
        if self.enable_horizontal:
            self.scroll_x = max(0, self.scroll_x - self.scroll_speed)
        return {"status": "scrolled_left", "scroll_x": self.scroll_x}

    def scroll_right(self):
        if self.enable_horizontal:
            self.scroll_x = max(0, self.scroll_x + self.scroll_speed)
        return {"status": "scrolled_right", "scroll_x": self.scroll_x}

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "scroll_x": self.scroll_x,
            "scroll_y": self.scroll_y,
            "enable_vertical": self.enable_vertical,
            "enable_horizontal": self.enable_horizontal
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "scroll_x": self.scroll_x,
            "scroll_y": self.scroll_y
        })
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()

        layout_render = None
        if self.layout:
            layout_render = self.layout.render()

        base.update({
            "type": "scroll_view",
            "scroll_x": self.scroll_x,
            "scroll_y": self.scroll_y,
            "background": self.background,
            "padding": self.padding,
            "layout": layout_render
        })
        return base

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        """ScrollView handles scroll events and forwards others to layout."""
        et = event.get("type")

        if et == "scroll_up":
            return self.scroll_up()
        if et == "scroll_down":
            return self.scroll_down()
        if et == "scroll_left":
            return self.scroll_left()
        if et == "scroll_right":
            return self.scroll_right()

        if self.layout and hasattr(self.layout, "on_event"):
            return self.layout.on_event(event)

        return {"status": "ignored", "component": self.component_id, "event": event}

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "type": "scroll_view",
            "scroll_x": self.scroll_x,
            "scroll_y": self.scroll_y,
            "enable_vertical": self.enable_vertical,
            "enable_horizontal": self.enable_horizontal,
            "background": self.background,
            "padding": self.padding
        })
        return base

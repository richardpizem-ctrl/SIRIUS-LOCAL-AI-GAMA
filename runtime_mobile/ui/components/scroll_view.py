# ============================================================
# SIRIUS LOCAL AI GAMA - Scroll View Component
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Scrollable container for long vertical or horizontal layouts.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .container import Container
from ..theme import MobileUITheme


class ScrollView(Container):
    """
    Scrollable container for long layouts.
    Supports vertical and horizontal scrolling.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, layout=None, component_id=None, visible=True):
        super().__init__(layout=layout, component_id=component_id, visible=visible)

        # Scroll offsets
        self.scroll_x = 0
        self.scroll_y = 0

        # Scroll configuration
        self.scroll_speed = 20
        self.enable_vertical = True
        self.enable_horizontal = False

        # Visual properties
        self.background = MobileUITheme.COLORS["surface"]
        self.padding = MobileUITheme.SPACING["md"]

    # ------------------------------------------------------------
    # Scroll control
    # ------------------------------------------------------------

    def scroll_up(self):
        if self.enable_vertical:
            self.scroll_y = max(0, self.scroll_y - self.scroll_speed)
        return {"status": "scrolled_up", "scroll_y": self.scroll_y}

    def scroll_down(self):
        if self.enable_vertical:
            self.scroll_y += self.scroll_speed
        return {"status": "scrolled_down", "scroll_y": self.scroll_y}

    def scroll_left(self):
        if self.enable_horizontal:
            self.scroll_x = max(0, self.scroll_x - self.scroll_speed)
        return {"status": "scrolled_left", "scroll_x": self.scroll_x}

    def scroll_right(self):
        if self.enable_horizontal:
            self.scroll_x += self.scroll_speed
        return {"status": "scrolled_right", "scroll_x": self.scroll_x}

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def update(self):
        base = super().update()
        base.update({
            "scroll_x": self.scroll_x,
            "scroll_y": self.scroll_y
        })
        return base

    # ------------------------------------------------------------
    # Render (placeholder)
    # ------------------------------------------------------------

    def render(self):
        """
        Placeholder render output.
        In UI 3.0.0 this will be handled by the rendering engine.
        """
        layout_render = None
        if self.layout:
            layout_render = self.layout.render()

        return {
            "status": "rendered",
            "component": self.component_id,
            "type": "scroll_view",
            "scroll_x": self.scroll_x,
            "scroll_y": self.scroll_y,
            "background": self.background,
            "padding": self.padding,
            "layout": layout_render,
            "visible": self.visible
        }

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
            "enable_horizontal": self.enable_horizontal
        })
        return base

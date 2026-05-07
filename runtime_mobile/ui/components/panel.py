# ============================================================
# SIRIUS LOCAL AI GAMA - Panel Component
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Visual UI block with background, padding and optional layout.
# Used for sections, cards, widgets, containers, screens.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .container import Container
from ..theme import MobileUITheme


class Panel(Container):
    """
    Visual UI block with background, padding and optional layout.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, layout=None, component_id=None, visible=True):
        super().__init__(layout=layout, component_id=component_id, visible=visible)

        # Panel-specific visual properties
        self.background = MobileUITheme.COLORS["panel"]
        self.border_radius = MobileUITheme.BORDER_RADIUS["md"]
        self.border_color = MobileUITheme.COLORS["border"]
        self.border_width = 1
        self.padding = MobileUITheme.SPACING["lg"]

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
            "type": "panel",
            "background": self.background,
            "border_radius": self.border_radius,
            "border_color": self.border_color,
            "border_width": self.border_width,
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
            "type": "panel",
            "border_radius": self.border_radius,
            "border_color": self.border_color,
            "border_width": self.border_width
        })
        return base

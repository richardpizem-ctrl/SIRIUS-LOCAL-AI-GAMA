# ============================================================
# SIRIUS LOCAL AI GAMA - Horizontal Layout
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Horizontal layout: arranges components from left to right.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .base_layout import BaseUILayout
from ..theme import MobileUITheme


class HorizontalLayout(BaseUILayout):
    """
    Arranges components horizontally (left → right).
    """

    LAYOUT_VERSION = "3.0.0-pre"

    def __init__(self, layout_id=None, visible=True):
        super().__init__(layout_id=layout_id, visible=visible)

        # Horizontal layout specific defaults
        self.padding_left = MobileUITheme.SPACING["lg"]
        self.padding_right = MobileUITheme.SPACING["lg"]

    # ------------------------------------------------------------
    # Render (placeholder)
    # ------------------------------------------------------------

    def render(self):
        """
        Placeholder render output.
        In UI 3.0.0 this will be handled by the rendering engine.
        """
        rendered_components = []
        x_offset = self.padding_left

        for component in self.components:
            component_render = component.render()
            component_render["x_offset"] = x_offset
            rendered_components.append(component_render)

            # Move right by component width + spacing
            width = component_render.get("width", 80)
            x_offset += width + self.spacing

        return {
            "status": "rendered",
            "layout": self.layout_id,
            "type": "horizontal",
            "background": self.background,
            "padding_left": self.padding_left,
            "padding_right": self.padding_right,
            "spacing": self.spacing,
            "components": rendered_components,
            "visible": self.visible
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "type": "horizontal",
            "padding_left": self.padding_left,
            "padding_right": self.padding_right
        })
        return base

# ============================================================
# SIRIUS LOCAL AI GAMA - Vertical Layout
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Vertical layout: stacks components from top to bottom.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .base_layout import BaseUILayout
from ..theme import MobileUITheme


class VerticalLayout(BaseUILayout):
    """
    Arranges components vertically (top → bottom).
    """

    LAYOUT_VERSION = "3.0.0-pre"

    def __init__(self, layout_id=None, visible=True):
        super().__init__(layout_id=layout_id, visible=visible)

        # Vertical layout specific defaults
        self.padding_top = MobileUITheme.SPACING["lg"]
        self.padding_bottom = MobileUITheme.SPACING["lg"]

    # ------------------------------------------------------------
    # Render (placeholder)
    # ------------------------------------------------------------

    def render(self):
        """
        Placeholder render output.
        In UI 3.0.0 this will be handled by the rendering engine.
        """
        rendered_components = []
        y_offset = self.padding_top

        for component in self.components:
            component_render = component.render()
            component_render["y_offset"] = y_offset
            rendered_components.append(component_render)

            # Move down by component height + spacing
            height = component_render.get("height", 20)
            y_offset += height + self.spacing

        return {
            "status": "rendered",
            "layout": self.layout_id,
            "type": "vertical",
            "background": self.background,
            "padding_top": self.padding_top,
            "padding_bottom": self.padding_bottom,
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
            "type": "vertical",
            "padding_top": self.padding_top,
            "padding_bottom": self.padding_bottom
        })
        return base

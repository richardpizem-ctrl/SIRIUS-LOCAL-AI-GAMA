# ============================================================
# SIRIUS LOCAL AI GAMA - Stack Layout
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Stack layout: overlays components on top of each other.
# Useful for popups, modals, debug overlays, layered UI.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .base_layout import BaseUILayout
from ..theme import MobileUITheme


class StackLayout(BaseUILayout):
    """
    Overlays components on top of each other.
    The first component is the bottom layer,
    the last component is the top layer.
    """

    LAYOUT_VERSION = "3.0.0-pre"

    def __init__(self, layout_id=None, visible=True):
        super().__init__(layout_id=layout_id, visible=visible)

        # Stack layout specific defaults
        self.padding = MobileUITheme.SPACING["md"]

    # ------------------------------------------------------------
    # Render (placeholder)
    # ------------------------------------------------------------

    def render(self):
        """
        Placeholder render output.
        In UI 3.0.0 this will be handled by the rendering engine.
        Each component is rendered at the same base position,
        but in different layers (z-index).
        """
        rendered_components = []
        z_index = 0

        for component in self.components:
            component_render = component.render()
            component_render["z_index"] = z_index
            component_render["padding"] = self.padding
            rendered_components.append(component_render)

            z_index += 1

        return {
            "status": "rendered",
            "layout": self.layout_id,
            "type": "stack",
            "background": self.background,
            "padding": self.padding,
            "components": rendered_components,
            "visible": self.visible
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "type": "stack",
            "padding": self.padding
        })
        return base

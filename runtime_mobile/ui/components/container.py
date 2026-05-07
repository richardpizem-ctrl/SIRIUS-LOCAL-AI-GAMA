# ============================================================
# SIRIUS LOCAL AI GAMA - Container Component
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Container component that holds a layout.
# This allows nested UI structures (panels, sections, screens).
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Container(BaseUIComponent):
    """
    A UI component that contains a layout.
    This is the bridge between components and layout systems.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, layout=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.layout = layout
        self.background = MobileUITheme.COLORS["surface"]
        self.padding = MobileUITheme.SPACING["md"]

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()

        layout_info = None
        if self.layout:
            layout_info = self.layout.initialize()

        base.update({
            "layout": layout_info,
            "background": self.background,
            "padding": self.padding
        })
        return base

    def update(self):
        base = super().update()

        layout_info = None
        if self.layout:
            layout_info = self.layout.update()

        base.update({
            "layout": layout_info
        })
        return base

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
            "type": "container",
            "background": self.background,
            "padding": self.padding,
            "layout": layout_render,
            "visible": self.visible
        }

    def shutdown(self):
        layout_info = None
        if self.layout:
            layout_info = self.layout.shutdown()

        base = super().shutdown()
        base.update({"layout": layout_info})
        return base

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "type": "container",
            "layout": self.layout.get_info() if self.layout else None
        })
        return base


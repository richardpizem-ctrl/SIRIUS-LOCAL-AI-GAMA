# ============================================================
# SIRIUS LOCAL AI GAMA - Text Label Component
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Simple text label component for the Mobile UI.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class TextLabel(BaseUIComponent):
    """
    Basic text label component.
    Displays static or dynamic text.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, text="", component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)
        self.text = text

        # Theme defaults
        self.color = MobileUITheme.COLORS["text"]
        self.font_family = MobileUITheme.FONT["family"]
        self.font_size = MobileUITheme.FONT["size_normal"]

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "text": self.text,
            "color": self.color,
            "font": self.font_family,
            "size": self.font_size
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "text": self.text
        })
        return base

    def render(self):
        """
        Placeholder render output.
        In UI 3.0.0 this will be handled by the rendering engine.
        """
        return {
            "status": "rendered",
            "component": self.component_id,
            "text": self.text,
            "color": self.color,
            "font": self.font_family,
            "size": self.font_size,
            "visible": self.visible
        }

    # ------------------------------------------------------------
    # API
    # ------------------------------------------------------------

    def set_text(self, new_text):
        self.text = new_text
        return {
            "status": "text_updated",
            "component": self.component_id,
            "text": self.text
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "text": self.text,
            "font": self.font_family,
            "size": self.font_size
        })
        return base

# ============================================================
# SIRIUS LOCAL AI GAMA - Icon Component
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Lightweight icon component using Unicode or text symbols.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Icon(BaseUIComponent):
    """
    Lightweight icon component using Unicode or text symbols.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, symbol="★", size=18, color=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.symbol = symbol
        self.size = size
        self.color = color or MobileUITheme.COLORS["text"]
        self.padding = MobileUITheme.SPACING["sm"]

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "symbol": self.symbol,
            "size": self.size,
            "color": self.color
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "symbol": self.symbol,
            "size": self.size
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
        return {
            "status": "rendered",
            "component": self.component_id,
            "type": "icon",
            "symbol": self.symbol,
            "size": self.size,
            "color": self.color,
            "padding": self.padding,
            "visible": self.visible
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "type": "icon",
            "symbol": self.symbol,
            "size": self.size,
            "color": self.color
        })
        return base

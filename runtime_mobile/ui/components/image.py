# ============================================================
# SIRIUS LOCAL AI GAMA - Image Component
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Lightweight image component for displaying pictures.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Image(BaseUIComponent):
    """
    Lightweight image component for displaying pictures.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, source=None, size=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        # Path or runtime image reference
        self.source = source

        # (width, height) or None for auto
        self.size = size

        # Visual properties
        self.background = MobileUITheme.COLORS["surface"]
        self.border_radius = MobileUITheme.BORDER_RADIUS["sm"]
        self.padding = MobileUITheme.SPACING["sm"]

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "source": self.source,
            "size": self.size
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "source": self.source,
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
            "type": "image",
            "source": self.source,
            "size": self.size,
            "background": self.background,
            "border_radius": self.border_radius,
            "padding": self.padding,
            "visible": self.visible
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "type": "image",
            "source": self.source,
            "size": self.size
        })
        return base

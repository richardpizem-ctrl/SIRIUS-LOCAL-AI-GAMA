# ============================================================
# SIRIUS LOCAL AI GAMA - Image Component
# Version: 3.0.0-pre
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Image(BaseUIComponent):

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, source=None, size=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.source = source
        self.size = size  # (width, height) or None

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
            "size": self.size,
            "background": self.background,
            "border_radius": self.border_radius,
            "padding": self.padding
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "source": self.source,
            "size": self.size,
            "background": self.background,
            "border_radius": self.border_radius
        })
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()
        base.update({
            "type": "image",
            "source": self.source,
            "size": self.size,
            "background": self.background,
            "border_radius": self.border_radius,
            "padding": self.padding
        })
        return base

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        """Images normally do not handle events, but forward them."""
        return {
            "status": "ignored",
            "component": self.component_id,
            "event": event
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "type": "image",
            "source": self.source,
            "size": self.size,
            "background": self.background,
            "border_radius": self.border_radius,
            "padding": self.padding
        })
        return base

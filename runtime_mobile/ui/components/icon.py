# ============================================================
# SIRIUS LOCAL AI GAMA - Icon Component
# Version: 3.0.0-pre
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Icon(BaseUIComponent):

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
            "color": self.color,
            "padding": self.padding
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "symbol": self.symbol,
            "size": self.size,
            "color": self.color
        })
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()
        base.update({
            "type": "icon",
            "symbol": self.symbol,
            "size": self.size,
            "color": self.color,
            "padding": self.padding
        })
        return base

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        """Icons normally do not handle events, but forward them."""
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
            "type": "icon",
            "symbol": self.symbol,
            "size": self.size,
            "color": self.color,
            "padding": self.padding
        })
        return base

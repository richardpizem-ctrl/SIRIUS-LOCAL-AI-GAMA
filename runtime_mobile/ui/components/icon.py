# ============================================================
# SIRIUS LOCAL AI GAMA - Icon Component
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - hover + disabled states
# - event bubbling support
# - layout flags (dirty, needs_render)
# - unified metadata schema v3
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Icon(BaseUIComponent):

    COMPONENT_VERSION = "3.1.0"

    def __init__(self, symbol="★", size=18, color=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.symbol = symbol
        self.size = size
        self.color = color or MobileUITheme.COLORS["text"]
        self.padding = MobileUITheme.SPACING["sm"]

        # Interaction states
        self._hover = False
        self._disabled = False

    # ------------------------------------------------------------
    # State control
    # ------------------------------------------------------------

    def set_disabled(self, value: bool):
        self._disabled = bool(value)
        self.dirty = True

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "symbol": self.symbol,
            "size": self.size,
            "color": self.color,
            "padding": self.padding,
            "disabled": self._disabled,
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "symbol": self.symbol,
            "size": self.size,
            "color": self.color,
            "hover": self._hover,
            "disabled": self._disabled,
        })
        return base

    def render(self):
        base = super().render()

        # Determine color
        if self._disabled:
            color = MobileUITheme.COLORS.get("text_disabled", "#AAAAAA")
        elif self._hover:
            color = MobileUITheme.COLORS.get("text_hover", self.color)
        else:
            color = self.color

        base.update({
            "type": "icon",
            "symbol": self.symbol,
            "size": self.size,
            "color": color,
            "padding": self.padding,
            "disabled": self._disabled,
        })
        return base

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Icons normally do not handle events, but support hover + bubbling.
        """
        et = event.get("type")

        if et == "hover":
            self._hover = True
            self.dirty = True
            return {"status": "handled", "bubble": False}

        if et == "hover_end":
            self._hover = False
            self.dirty = True
            return {"status": "handled", "bubble": False}

        return {
            "status": "ignored",
            "component": self.component_id,
            "event": event,
            "bubble": True
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
            "padding": self.padding,
            "hover": self._hover,
            "disabled": self._disabled,
        })
        return base

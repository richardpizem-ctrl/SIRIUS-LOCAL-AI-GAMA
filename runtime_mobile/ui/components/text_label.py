# ============================================================
# SIRIUS LOCAL AI GAMA - Text Label Component
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - hover + disabled states
# - auto-size + max_width + wrapping
# - event bubbling
# - layout flags (dirty, needs_render)
# - unified metadata schema v3
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class TextLabel(BaseUIComponent):

    COMPONENT_VERSION = "3.1.0"

    def __init__(self, text="", max_width=None, wrap=True,
                 component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.text = text

        # Text rendering options
        self.max_width = max_width
        self.wrap = wrap

        # Theme defaults
        self.color = MobileUITheme.COLORS["text"]
        self.color_disabled = MobileUITheme.COLORS.get("text_disabled", "#AAAAAA")

        self.font_family = MobileUITheme.FONT["family"]
        self.font_size = MobileUITheme.FONT["size_normal"]

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
            "text": self.text,
            "color": self.color,
            "font": self.font_family,
            "font_size": self.font_size,
            "max_width": self.max_width,
            "wrap": self.wrap,
            "disabled": self._disabled,
            "hover": self._hover,
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "text": self.text,
            "color": self.color,
            "font": self.font_family,
            "font_size": self.font_size,
            "max_width": self.max_width,
            "wrap": self.wrap,
            "disabled": self._disabled,
            "hover": self._hover,
        })
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()

        # Determine color
        if self._disabled:
            color = self.color_disabled
        elif self._hover:
            color = MobileUITheme.COLORS.get("text_hover", self.color)
        else:
            color = self.color

        base.update({
            "type": "text_label",
            "text": self.text,
            "color": color,
            "font": self.font_family,
            "font_size": self.font_size,
            "max_width": self.max_width,
            "wrap": self.wrap,
            "disabled": self._disabled,
            "hover": self._hover,
        })
        return base

    # ------------------------------------------------------------
    # API
    # ------------------------------------------------------------

    def set_text(self, new_text):
        self.text = new_text
        self.dirty = True
        self.needs_layout = True

        self.on_event({
            "type": "text_changed",
            "component": self.component_id,
            "text": self.text
        })

        return {
            "status": "text_updated",
            "component": self.component_id,
            "text": self.text
        }

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Text labels support hover and bubble all other events.
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
            "type": "text_label",
            "text": self.text,
            "color": self.color,
            "font": self.font_family,
            "font_size": self.font_size,
            "max_width": self.max_width,
            "wrap": self.wrap,
            "disabled": self._disabled,
            "hover": self._hover,
        })
        return base

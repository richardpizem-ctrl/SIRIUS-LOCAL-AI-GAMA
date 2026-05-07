# ============================================================
# SIRIUS LOCAL AI GAMA - Text Label Component
# Version: 3.0.0-pre
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class TextLabel(BaseUIComponent):

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, text="", component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.text = text

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
            "font_size": self.font_size
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "text": self.text,
            "color": self.color,
            "font": self.font_family,
            "font_size": self.font_size
        })
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()
        base.update({
            "type": "text_label",
            "text": self.text,
            "color": self.color,
            "font": self.font_family,
            "font_size": self.font_size
        })
        return base

    # ------------------------------------------------------------
    # API
    # ------------------------------------------------------------

    def set_text(self, new_text):
        self.text = new_text

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
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        """Text labels normally do not handle events, but forward them."""
        return {
            "status": "ok",
            "component": self.component_id,
            "event": event
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
            "font_size": self.font_size
        })
        return base

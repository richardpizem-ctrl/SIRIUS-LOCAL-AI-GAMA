# ============================================================
# SIRIUS LOCAL AI GAMA - Button Component
# Version: 3.0.0-pre
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Button(BaseUIComponent):

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, text="", on_click=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.text = text
        self.on_click = on_click

        # Theme defaults
        self.bg_color = MobileUITheme.COLORS["primary"]
        self.bg_color_pressed = MobileUITheme.COLORS["primary_dark"]
        self.text_color = MobileUITheme.COLORS["text"]
        self.font_family = MobileUITheme.FONT["family"]
        self.font_size = MobileUITheme.FONT["size_normal"]
        self.height = MobileUITheme.COMPONENTS["button_height"]
        self.corner_radius = MobileUITheme.COMPONENTS["corner_radius"]

        self._pressed = False

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "text": self.text,
            "height": self.height,
            "corner_radius": self.corner_radius
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "pressed": self._pressed
        })
        return base

    def render(self):
        base = super().render()
        base.update({
            "text": self.text,
            "background": self.bg_color_pressed if self._pressed else self.bg_color,
            "text_color": self.text_color,
            "font": self.font_family,
            "font_size": self.font_size,
            "corner_radius": self.corner_radius,
        })
        return base

    # ------------------------------------------------------------
    # Interaction API
    # ------------------------------------------------------------

    def press(self):
        self._pressed = True
        self.on_event({"type": "press", "component": self.component_id})
        return {"status": "pressed", "component": self.component_id}

    def release(self):
        self._pressed = False

        callback_result = None
        if callable(self.on_click):
            callback_result = self.on_click({
                "component": self.component_id,
                "text": self.text,
                "pressed": False
            })

        self.on_event({"type": "release", "component": self.component_id})

        return {
            "status": "released",
            "component": self.component_id,
            "callback_result": callback_result
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "text": self.text,
            "pressed": self._pressed,
            "text_color": self.text_color,
            "background": self.bg_color,
            "font": self.font_family,
            "font_size": self.font_size,
            "corner_radius": self.corner_radius,
        })
        return base

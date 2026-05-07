# ============================================================
# SIRIUS LOCAL AI GAMA - Button Component
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Interactive button component for the Mobile UI.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Button(BaseUIComponent):
    """
    Basic button component.
    Supports text, click callbacks and theme styling.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, text="", on_click=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.text = text
        self.on_click = on_click  # callback function

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
        """
        Placeholder render output.
        In UI 3.0.0 this will be handled by the rendering engine.
        """
        return {
            "status": "rendered",
            "component": self.component_id,
            "text": self.text,
            "background": self.bg_color_pressed if self._pressed else self.bg_color,
            "text_color": self.text_color,
            "font": self.font_family,
            "size": self.font_size,
            "height": self.height,
            "corner_radius": self.corner_radius,
            "visible": self.visible
        }

    # ------------------------------------------------------------
    # Interaction API
    # ------------------------------------------------------------

    def press(self):
        """Simulate button press."""
        self._pressed = True
        return {"status": "pressed", "component": self.component_id}

    def release(self):
        """Simulate button release and trigger callback."""
        self._pressed = False

        callback_result = None
        if callable(self.on_click):
            callback_result = self.on_click()

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
            "height": self.height,
            "corner_radius": self.corner_radius
        })
        return base

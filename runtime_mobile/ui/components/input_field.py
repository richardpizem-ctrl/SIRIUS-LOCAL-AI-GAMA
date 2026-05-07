# ============================================================
# SIRIUS LOCAL AI GAMA - Input Field Component
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Text input component with placeholder, focus state and value.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class InputField(BaseUIComponent):
    """
    Basic text input field with placeholder and focus state.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, placeholder="", value="", component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.placeholder = placeholder
        self.value = value
        self.is_focused = False

        # Visual properties
        self.background = MobileUITheme.COLORS["surface"]
        self.border_color = MobileUITheme.COLORS["border"]
        self.border_width = 1
        self.border_radius = MobileUITheme.BORDER_RADIUS["sm"]
        self.padding = MobileUITheme.SPACING["md"]
        self.text_color = MobileUITheme.COLORS["text"]
        self.placeholder_color = MobileUITheme.COLORS["muted"]

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "placeholder": self.placeholder,
            "value": self.value,
            "focused": self.is_focused
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "value": self.value,
            "focused": self.is_focused
        })
        return base

    # ------------------------------------------------------------
    # Interaction
    # ------------------------------------------------------------

    def focus(self):
        self.is_focused = True
        return {"status": "focused", "component": self.component_id}

    def blur(self):
        self.is_focused = False
        return {"status": "blurred", "component": self.component_id}

    def set_value(self, text):
        self.value = text
        return {"status": "value_set", "value": self.value}

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
            "type": "input_field",
            "value": self.value,
            "placeholder": self.placeholder,
            "focused": self.is_focused,
            "background": self.background,
            "border_color": self.border_color,
            "border_width": self.border_width,
            "border_radius": self.border_radius,
            "padding": self.padding,
            "text_color": self.text_color,
            "placeholder_color": self.placeholder_color,
            "visible": self.visible
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "type": "input_field",
            "placeholder": self.placeholder,
            "value": self.value,
            "focused": self.is_focused
        })
        return base

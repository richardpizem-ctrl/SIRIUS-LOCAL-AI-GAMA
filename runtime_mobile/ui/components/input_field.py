# ============================================================
# SIRIUS LOCAL AI GAMA - Input Field Component
# Version: 3.0.0-pre
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class InputField(BaseUIComponent):

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
            "focused": self.is_focused,
            "background": self.background,
            "border_color": self.border_color,
            "border_width": self.border_width,
            "border_radius": self.border_radius,
            "padding": self.padding,
            "text_color": self.text_color,
            "placeholder_color": self.placeholder_color
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "value": self.value,
            "focused": self.is_focused,
            "background": self.background,
            "border_color": self.border_color,
            "border_width": self.border_width,
            "border_radius": self.border_radius,
            "padding": self.padding,
            "text_color": self.text_color,
            "placeholder_color": self.placeholder_color
        })
        return base

    # ------------------------------------------------------------
    # Interaction
    # ------------------------------------------------------------

    def focus(self):
        self.is_focused = True
        self.on_event({"type": "focus", "component": self.component_id})
        return {"status": "focused", "component": self.component_id}

    def blur(self):
        self.is_focused = False
        self.on_event({"type": "blur", "component": self.component_id})
        return {"status": "blurred", "component": self.component_id}

    def set_value(self, text):
        self.value = text
        self.on_event({"type": "input", "component": self.component_id, "value": text})
        return {"status": "value_set", "value": self.value}

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()
        base.update({
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
            "placeholder_color": self.placeholder_color
        })
        return base

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        """Input fields handle focus, blur and text input events."""
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
            "type": "input_field",
            "placeholder": self.placeholder,
            "value": self.value,
            "focused": self.is_focused,
            "background": self.background,
            "border_color": self.border_color,
            "border_width": self.border_width,
            "border_radius": self.border_radius,
            "padding": self.padding,
            "text_color": self.text_color,
            "placeholder_color": self.placeholder_color
        })
        return base

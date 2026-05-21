# ============================================================
# SIRIUS LOCAL AI GAMA - Button Component
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - pressed/hover/disabled states
# - event bubbling support
# - layout flags (dirty, needs_render)
# - safe callback execution
# - unified metadata schema v3
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Button(BaseUIComponent):

    COMPONENT_VERSION = "3.1.0"

    def __init__(self, text="", on_click=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.text = text
        self.on_click = on_click

        # Theme defaults
        self.bg_color = MobileUITheme.COLORS["primary"]
        self.bg_color_pressed = MobileUITheme.COLORS["primary_dark"]
        self.bg_color_disabled = MobileUITheme.COLORS.get("disabled", "#777777")

        self.text_color = MobileUITheme.COLORS["text"]
        self.text_color_disabled = MobileUITheme.COLORS.get("text_disabled", "#CCCCCC")

        self.font_family = MobileUITheme.FONT["family"]
        self.font_size = MobileUITheme.FONT["size_normal"]

        self.height = MobileUITheme.COMPONENTS["button_height"]
        self.corner_radius = MobileUITheme.COMPONENTS["corner_radius"]

        # Interaction states
        self._pressed = False
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
            "height": self.height,
            "corner_radius": self.corner_radius,
            "disabled": self._disabled,
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "pressed": self._pressed,
            "hover": self._hover,
            "disabled": self._disabled,
        })
        return base

    def render(self):
        base = super().render()

        # Determine background
        if self._disabled:
            bg = self.bg_color_disabled
            text_color = self.text_color_disabled
        elif self._pressed:
            bg = self.bg_color_pressed
            text_color = self.text_color
        else:
            bg = self.bg_color
            text_color = self.text_color

        base.update({
            "text": self.text,
            "background": bg,
            "text_color": text_color,
            "font": self.font_family,
            "font_size": self.font_size,
            "corner_radius": self.corner_radius,
            "disabled": self._disabled,
        })

        return base

    # ------------------------------------------------------------
    # Interaction API
    # ------------------------------------------------------------

    def press(self):
        if self._disabled:
            return {"status": "ignored", "reason": "disabled", "component": self.component_id}

        self._pressed = True
        self.dirty = True

        self.on_event({"type": "press", "component": self.component_id})
        return {"status": "pressed", "component": self.component_id}

    def release(self):
        if self._disabled:
            return {"status": "ignored", "reason": "disabled", "component": self.component_id}

        self._pressed = False
        self.dirty = True

        callback_result = None
        if callable(self.on_click):
            try:
                callback_result = self.on_click({
                    "component": self.component_id,
                    "text": self.text,
                    "pressed": False
                })
            except Exception as e:
                callback_result = {"error": str(e)}

        self.on_event({"type": "release", "component": self.component_id})

        return {
            "status": "released",
            "component": self.component_id,
            "callback_result": callback_result
        }

    # ------------------------------------------------------------
    # Event hook (override)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Button-specific event handling.
        Supports bubbling.
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

        return {"status": "ignored", "bubble": True}

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "text": self.text,
            "pressed": self._pressed,
            "hover": self._hover,
            "disabled": self._disabled,
            "text_color": self.text_color,
            "background": self.bg_color,
            "font": self.font_family,
            "font_size": self.font_size,
            "corner_radius": self.corner_radius,
        })
        return base

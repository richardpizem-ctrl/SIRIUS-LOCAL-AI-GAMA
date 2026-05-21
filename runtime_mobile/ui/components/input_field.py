# ============================================================
# SIRIUS LOCAL AI GAMA - Input Field Component
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - focus/blur/input pipeline v3
# - disabled + error + hover states
# - cursor + selection metadata
# - event bubbling
# - layout flags (dirty, needs_render)
# - unified metadata schema v3
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class InputField(BaseUIComponent):

    COMPONENT_VERSION = "3.1.0"

    def __init__(self, placeholder="", value="", component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.placeholder = placeholder
        self.value = value

        # Interaction states
        self.is_focused = False
        self._hover = False
        self._disabled = False
        self._error = False

        # Cursor + selection
        self.cursor_pos = len(value)
        self.selection = None  # (start, end) or None

        # Visual properties
        self.background = MobileUITheme.COLORS["surface"]
        self.border_color = MobileUITheme.COLORS["border"]
        self.border_color_focused = MobileUITheme.COLORS.get("primary", "#4A90E2")
        self.border_color_error = MobileUITheme.COLORS.get("error", "#FF4444")

        self.border_width = 1
        self.border_radius = MobileUITheme.BORDER_RADIUS["sm"]
        self.padding = MobileUITheme.SPACING["md"]

        self.text_color = MobileUITheme.COLORS["text"]
        self.placeholder_color = MobileUITheme.COLORS["muted"]

    # ------------------------------------------------------------
    # State control
    # ------------------------------------------------------------

    def set_disabled(self, value: bool):
        self._disabled = bool(value)
        self.dirty = True

    def set_error(self, value: bool):
        self._error = bool(value)
        self.dirty = True

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "placeholder": self.placeholder,
            "value": self.value,
            "focused": self.is_focused,
            "disabled": self._disabled,
            "error": self._error,
            "cursor_pos": self.cursor_pos,
            "selection": self.selection,
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
            "disabled": self._disabled,
            "error": self._error,
            "cursor_pos": self.cursor_pos,
            "selection": self.selection,
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
        if self._disabled:
            return {"status": "ignored", "reason": "disabled"}

        self.is_focused = True
        self.border_color = self.border_color_focused
        self.dirty = True

        self.on_event({"type": "focus", "component": self.component_id})
        return {"status": "focused", "component": self.component_id}

    def blur(self):
        self.is_focused = False
        self.border_color = self.border_color_error if self._error else MobileUITheme.COLORS["border"]
        self.dirty = True

        self.on_event({"type": "blur", "component": self.component_id})
        return {"status": "blurred", "component": self.component_id}

    def set_value(self, text):
        if self._disabled:
            return {"status": "ignored", "reason": "disabled"}

        self.value = text
        self.cursor_pos = len(text)
        self.selection = None
        self.dirty = True

        self.on_event({"type": "input", "component": self.component_id, "value": text})
        return {"status": "value_set", "value": self.value}

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()

        # Determine border color
        if self._disabled:
            border = MobileUITheme.COLORS.get("disabled_border", "#999999")
        elif self._error:
            border = self.border_color_error
        elif self.is_focused:
            border = self.border_color_focused
        else:
            border = self.border_color

        base.update({
            "type": "input_field",
            "value": self.value,
            "placeholder": self.placeholder,
            "focused": self.is_focused,
            "disabled": self._disabled,
            "error": self._error,
            "cursor_pos": self.cursor_pos,
            "selection": self.selection,
            "background": self.background,
            "border_color": border,
            "border_width": self.border_width,
            "border_radius": self.border_radius,
            "padding": self.padding,
            "text_color": self.text_color,
            "placeholder_color": self.placeholder_color
        })
        return base

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Input fields handle focus, blur, input, hover.
        All other events bubble upward.
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
            "status": "ok",
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
            "type": "input_field",
            "placeholder": self.placeholder,
            "value": self.value,
            "focused": self.is_focused,
            "disabled": self._disabled,
            "error": self._error,
            "cursor_pos": self.cursor_pos,
            "selection": self.selection,
            "background": self.background,
            "border_color": self.border_color,
            "border_width": self.border_width,
            "border_radius": self.border_radius,
            "padding": self.padding,
            "text_color": self.text_color,
            "placeholder_color": self.placeholder_color
        })
        return base

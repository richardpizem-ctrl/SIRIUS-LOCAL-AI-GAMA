# ============================================================
# SIRIUS LOCAL AI GAMA - Toggle Component
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - hover + disabled states
# - drag/tap toggle pipeline v3
# - event bubbling
# - safe callback execution
# - layout flags (dirty, needs_render)
# - unified metadata schema v3
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Toggle(BaseUIComponent):

    COMPONENT_VERSION = "3.1.0"

    def __init__(self, value=False, on_change=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        # Value model
        self.value = bool(value)
        self.on_change = on_change

        # Visuals
        self.padding = MobileUITheme.SPACING["sm"]
        self.track_color_on = MobileUITheme.COLORS["accent"]
        self.track_color_off = MobileUITheme.COLORS["border"]
        self.knob_color = MobileUITheme.COLORS["surface"]
        self.size = (40, 22)

        # Interaction states
        self._hover = False
        self._disabled = False
        self._dragging = False

    # ------------------------------------------------------------
    # State control
    # ------------------------------------------------------------

    def set_disabled(self, value: bool):
        self._disabled = bool(value)
        self.dirty = True

    # ------------------------------------------------------------
    # Interaction
    # ------------------------------------------------------------

    def toggle(self):
        if self._disabled:
            return {"status": "ignored", "reason": "disabled"}

        self.value = not self.value
        self.dirty = True

        # Callback
        callback_result = None
        if callable(self.on_change):
            try:
                callback_result = self.on_change(self.value)
            except Exception as e:
                callback_result = {"error": str(e)}

        # Event
        self.on_event({
            "type": "value_changed",
            "component": self.component_id,
            "value": self.value
        })

        return {"status": "toggled", "value": self.value, "callback_result": callback_result}

    def set_value(self, new_value: bool):
        if self._disabled:
            return {"status": "ignored", "reason": "disabled"}

        self.value = bool(new_value)
        self.dirty = True

        callback_result = None
        if callable(self.on_change):
            try:
                callback_result = self.on_change(self.value)
            except Exception as e:
                callback_result = {"error": str(e)}

        self.on_event({
            "type": "value_changed",
            "component": self.component_id,
            "value": self.value
        })

        return {"status": "value_set", "value": self.value, "callback_result": callback_result}

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "value": self.value,
            "size": self.size,
            "padding": self.padding,
            "track_color_on": self.track_color_on,
            "track_color_off": self.track_color_off,
            "knob_color": self.knob_color,
            "disabled": self._disabled,
            "hover": self._hover,
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "value": self.value,
            "disabled": self._disabled,
            "hover": self._hover,
            "dragging": self._dragging,
        })
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()

        # Track color
        if self._disabled:
            track = MobileUITheme.COLORS.get("disabled_border", "#999999")
        else:
            track = self.track_color_on if self.value else self.track_color_off

        base.update({
            "type": "toggle",
            "value": self.value,
            "track_color": track,
            "knob_color": self.knob_color,
            "size": self.size,
            "padding": self.padding,
            "disabled": self._disabled,
            "hover": self._hover,
            "dragging": self._dragging,
        })
        return base

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        et = event.get("type")

        if self._disabled:
            return {"status": "ignored", "reason": "disabled", "bubble": False}

        # Hover
        if et == "hover":
            self._hover = True
            self.dirty = True
            return {"status": "handled", "bubble": False}

        if et == "hover_end":
            self._hover = False
            self.dirty = True
            return {"status": "handled", "bubble": False}

        # Tap toggle
        if et == "toggle":
            return self.toggle()

        # Direct set
        if et == "set_value":
            return self.set_value(event.get("value"))

        # Drag start
        if et == "drag_start":
            self._dragging = True
            self.dirty = True
            return {"status": "drag_started", "bubble": False}

        # Drag move (0..1 normalized)
        if et == "drag_move":
            pos = event.get("position")
            if pos is not None:
                return self.set_value(pos >= 0.5)
            return {"status": "ignored", "bubble": False}

        # Drag end
        if et == "drag_end":
            self._dragging = False
            self.dirty = True
            return {"status": "drag_ended", "bubble": False}

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
            "type": "toggle",
            "value": self.value,
            "track_color_on": self.track_color_on,
            "track_color_off": self.track_color_off,
            "knob_color": self.knob_color,
            "size": self.size,
            "padding": self.padding,
            "disabled": self._disabled,
            "hover": self._hover,
            "dragging": self._dragging,
        })
        return base

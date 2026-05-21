# ============================================================
# SIRIUS LOCAL AI GAMA - Slider Component
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - drag interaction v3
# - hover + disabled states
# - event bubbling
# - safe callback execution
# - percent clamping + rounding
# - layout flags (dirty, needs_render)
# - unified metadata schema v3
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Slider(BaseUIComponent):

    COMPONENT_VERSION = "3.1.0"

    def __init__(
        self,
        value=0,
        min_value=0,
        max_value=100,
        step=1,
        on_change=None,
        component_id=None,
        visible=True
    ):
        super().__init__(component_id=component_id, visible=visible)

        # Value model
        self.value = float(value)
        self.min_value = float(min_value)
        self.max_value = float(max_value)
        self.step = float(step)
        self.on_change = on_change

        # Visuals
        self.track_color = MobileUITheme.COLORS["border"]
        self.track_color_active = MobileUITheme.COLORS["accent"]
        self.knob_color = MobileUITheme.COLORS["surface"]
        self.padding = MobileUITheme.SPACING["md"]
        self.size = (160, 24)

        # Interaction states
        self._hover = False
        self._dragging = False
        self._disabled = False

    # ------------------------------------------------------------
    # State control
    # ------------------------------------------------------------

    def set_disabled(self, value: bool):
        self._disabled = bool(value)
        self.dirty = True

    # ------------------------------------------------------------
    # Value control (v3)
    # ------------------------------------------------------------

    def _apply_step(self, v):
        """Apply step rounding."""
        if self.step > 0:
            steps = round((v - self.min_value) / self.step)
            return self.min_value + steps * self.step
        return v

    def _clamp(self, v):
        return max(self.min_value, min(self.max_value, v))

    def set_value(self, new_value):
        if self._disabled:
            return {"status": "ignored", "reason": "disabled"}

        new_value = float(new_value)
        new_value = self._clamp(new_value)
        new_value = self._apply_step(new_value)

        self.value = new_value
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

        return {
            "status": "value_set",
            "value": self.value,
            "callback_result": callback_result
        }

    def increase(self):
        return self.set_value(self.value + self.step)

    def decrease(self):
        return self.set_value(self.value - self.step)

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "value": self.value,
            "min": self.min_value,
            "max": self.max_value,
            "step": self.step,
            "size": self.size,
            "padding": self.padding,
            "disabled": self._disabled,
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "value": self.value,
            "disabled": self._disabled,
            "dragging": self._dragging,
            "hover": self._hover,
        })
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()

        # Percent
        if self.max_value == self.min_value:
            percent = 0
        else:
            percent = (self.value - self.min_value) / (self.max_value - self.min_value)
            percent = max(0.0, min(1.0, percent))

        # Colors
        if self._disabled:
            track = MobileUITheme.COLORS.get("disabled_border", "#999999")
            knob = MobileUITheme.COLORS.get("disabled_surface", "#777777")
        else:
            track = self.track_color_active if self._dragging else self.track_color
            knob = self.knob_color

        base.update({
            "type": "slider",
            "value": self.value,
            "min": self.min_value,
            "max": self.max_value,
            "step": self.step,
            "percent": percent,
            "track_color": track,
            "knob_color": knob,
            "size": self.size,
            "padding": self.padding,
            "disabled": self._disabled,
            "dragging": self._dragging,
            "hover": self._hover,
        })
        return base

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """Slider handles drag/tap events for value changes."""
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

        # Drag start
        if et == "drag_start":
            self._dragging = True
            self.dirty = True
            return {"status": "drag_started", "bubble": False}

        # Drag move
        if et == "drag_move":
            pos = event.get("position")
            if pos is not None:
                # pos is normalized 0..1
                new_val = self.min_value + pos * (self.max_value - self.min_value)
                return self.set_value(new_val)
            return {"status": "ignored", "bubble": False}

        # Drag end
        if et == "drag_end":
            self._dragging = False
            self.dirty = True
            return {"status": "drag_ended", "bubble": False}

        # Simple increments
        if et == "increase":
            return self.increase()

        if et == "decrease":
            return self.decrease()

        if et == "set_value":
            return self.set_value(event.get("value"))

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
            "type": "slider",
            "value": self.value,
            "min": self.min_value,
            "max": self.max_value,
            "step": self.step,
            "track_color": self.track_color,
            "track_color_active": self.track_color_active,
            "knob_color": self.knob_color,
            "size": self.size,
            "padding": self.padding,
            "disabled": self._disabled,
            "dragging": self._dragging,
            "hover": self._hover,
        })
        return base

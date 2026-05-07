# ============================================================
# SIRIUS LOCAL AI GAMA - Slider Component
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Value slider with min/max range and callback support.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Slider(BaseUIComponent):
    """
    Horizontal slider for selecting a numeric value.
    """

    COMPONENT_VERSION = "3.0.0-pre"

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

        self.value = float(value)
        self.min_value = float(min_value)
        self.max_value = float(max_value)
        self.step = float(step)
        self.on_change = on_change  # callback(value)

        # Visual properties
        self.track_color = MobileUITheme.COLORS["border"]
        self.track_color_active = MobileUITheme.COLORS["accent"]
        self.knob_color = MobileUITheme.COLORS["surface"]
        self.padding = MobileUITheme.SPACING["md"]
        self.size = (160, 24)  # width, height

    # ------------------------------------------------------------
    # Value control
    # ------------------------------------------------------------

    def set_value(self, new_value):
        new_value = float(new_value)

        # Clamp to range
        new_value = max(self.min_value, min(self.max_value, new_value))

        # Apply step
        if self.step > 0:
            steps = round((new_value - self.min_value) / self.step)
            new_value = self.min_value + steps * self.step

        self.value = new_value

        if self.on_change:
            self.on_change(self.value)

        return {"status": "value_set", "value": self.value}

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
            "step": self.step
        })
        return base

    def update(self):
        base = super().update()
        base.update({"value": self.value})
        return base

    # ------------------------------------------------------------
    # Render (placeholder)
    # ------------------------------------------------------------

    def render(self):
        """
        Placeholder render output.
        In UI 3.0.0 this will be handled by the rendering engine.
        """

        # Percentage for active track
        percent = (self.value - self.min_value) / (self.max_value - self.min_value)

        return {
            "status": "rendered",
            "component": self.component_id,
            "type": "slider",
            "value": self.value,
            "min": self.min_value,
            "max": self.max_value,
            "step": self.step,
            "percent": percent,
            "track_color": self.track_color,
            "track_color_active": self.track_color_active,
            "knob_color": self.knob_color,
            "size": self.size,
            "padding": self.padding,
            "visible": self.visible
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
            "step": self.step
        })
        return base

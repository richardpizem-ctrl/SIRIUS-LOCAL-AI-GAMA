# ============================================================
# SIRIUS LOCAL AI GAMA - Slider Component
# Version: 3.0.0-pre
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Slider(BaseUIComponent):

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
        self.on_change = on_change

        self.track_color = MobileUITheme.COLORS["border"]
        self.track_color_active = MobileUITheme.COLORS["accent"]
        self.knob_color = MobileUITheme.COLORS["surface"]
        self.padding = MobileUITheme.SPACING["md"]
        self.size = (160, 24)

    # ------------------------------------------------------------
    # Value control
    # ------------------------------------------------------------

    def set_value(self, new_value):
        new_value = float(new_value)

        new_value = max(self.min_value, min(self.max_value, new_value))

        if self.step > 0:
            steps = round((new_value - self.min_value) / self.step)
            new_value = self.min_value + steps * self.step

        self.value = new_value

        if self.on_change:
            self.on_change(self.value)

        self.on_event({
            "type": "value_changed",
            "component": self.component_id,
            "value": self.value
        })

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
            "step": self.step,
            "size": self.size,
            "padding": self.padding
        })
        return base

    def update(self):
        base = super().update()
        base.update({"value": self.value})
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()

        if self.max_value == self.min_value:
            percent = 0
        else:
            percent = (self.value - self.min_value) / (self.max_value - self.min_value)

        base.update({
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
            "padding": self.padding
        })
        return base

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        """Slider handles drag/tap events for value changes."""
        et = event.get("type")

        if et == "increase":
            return self.increase()
        if et == "decrease":
            return self.decrease()
        if et == "set_value":
            return self.set_value(event.get("value"))

        return {
            "status": "ignored",
            "component": self.component_id,
            "event": event
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
            "padding": self.padding
        })
        return base

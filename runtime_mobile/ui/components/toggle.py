# ============================================================
# SIRIUS LOCAL AI GAMA - Toggle Component
# Version: 3.0.0-pre
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Toggle(BaseUIComponent):

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, value=False, on_change=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.value = bool(value)
        self.on_change = on_change

        self.padding = MobileUITheme.SPACING["sm"]
        self.track_color_on = MobileUITheme.COLORS["accent"]
        self.track_color_off = MobileUITheme.COLORS["border"]
        self.knob_color = MobileUITheme.COLORS["surface"]
        self.size = (40, 22)

    # ------------------------------------------------------------
    # Interaction
    # ------------------------------------------------------------

    def toggle(self):
        self.value = not self.value

        if self.on_change:
            self.on_change(self.value)

        self.on_event({
            "type": "value_changed",
            "component": self.component_id,
            "value": self.value
        })

        return {"status": "toggled", "value": self.value}

    def set_value(self, new_value: bool):
        self.value = bool(new_value)

        if self.on_change:
            self.on_change(self.value)

        self.on_event({
            "type": "value_changed",
            "component": self.component_id,
            "value": self.value
        })

        return {"status": "value_set", "value": self.value}

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
            "knob_color": self.knob_color
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "value": self.value,
            "track_color_on": self.track_color_on,
            "track_color_off": self.track_color_off,
            "knob_color": self.knob_color
        })
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()

        track_color = self.track_color_on if self.value else self.track_color_off

        base.update({
            "type": "toggle",
            "value": self.value,
            "track_color": track_color,
            "knob_color": self.knob_color,
            "size": self.size,
            "padding": self.padding
        })
        return base

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        et = event.get("type")

        if et == "toggle":
            return self.toggle()
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
            "type": "toggle",
            "value": self.value,
            "track_color_on": self.track_color_on,
            "track_color_off": self.track_color_off,
            "knob_color": self.knob_color,
            "size": self.size,
            "padding": self.padding
        })
        return base

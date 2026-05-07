# ============================================================
# SIRIUS LOCAL AI GAMA - Toggle Component
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# ON/OFF toggle switch with callback support.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Toggle(BaseUIComponent):
    """
    Simple ON/OFF toggle switch.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, value=False, on_change=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.value = value
        self.on_change = on_change  # callback(value)

        # Visual properties
        self.padding = MobileUITheme.SPACING["sm"]
        self.track_color_on = MobileUITheme.COLORS["accent"]
        self.track_color_off = MobileUITheme.COLORS["border"]
        self.knob_color = MobileUITheme.COLORS["surface"]
        self.size = (40, 22)  # width, height

    # ------------------------------------------------------------
    # Interaction
    # ------------------------------------------------------------

    def toggle(self):
        self.value = not self.value

        if self.on_change:
            self.on_change(self.value)

        return {"status": "toggled", "value": self.value}

    def set_value(self, new_value: bool):
        self.value = bool(new_value)

        if self.on_change:
            self.on_change(self.value)

        return {"status": "value_set", "value": self.value}

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({"value": self.value})
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
        track_color = self.track_color_on if self.value else self.track_color_off

        return {
            "status": "rendered",
            "component": self.component_id,
            "type": "toggle",
            "value": self.value,
            "track_color": track_color,
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
            "type": "toggle",
            "value": self.value
        })
        return base

# ============================================================
# SIRIUS LOCAL AI GAMA - Panel Component
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - full Container 3.1 compatibility
# - event bubbling + safe layout routing
# - border + background rendering v3
# - layout invalidation (dirty, needs_layout)
# - unified metadata schema v3
# ============================================================

from .container import Container
from ..theme import MobileUITheme


class Panel(Container):

    COMPONENT_VERSION = "3.1.0"

    def __init__(self, layout=None, component_id=None, visible=True):
        super().__init__(layout=layout, component_id=component_id, visible=visible)

        # Panel-specific visual properties
        self.background = MobileUITheme.COLORS["panel"]
        self.border_radius = MobileUITheme.BORDER_RADIUS["md"]
        self.border_color = MobileUITheme.COLORS["border"]
        self.border_width = 1
        self.padding = MobileUITheme.SPACING["lg"]

    # ------------------------------------------------------------
    # Render (UI Engine 3.1)
    # ------------------------------------------------------------

    def render(self):
        base = super().render()

        base.update({
            "type": "panel",
            "background": self.background,
            "border_radius": self.border_radius,
            "border_color": self.border_color,
            "border_width": self.border_width,
            "padding": self.padding,
        })

        return base

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Panels forward events to layout if present.
        Layout may choose to bubble or stop propagation.
        """
        if self.layout and hasattr(self.layout, "on_event"):
            try:
                result = self.layout.on_event(event)
                if isinstance(result, dict):
                    return result
            except Exception as e:
                return {
                    "status": "error",
                    "component": self.component_id,
                    "error": str(e),
                    "bubble": True
                }

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
            "type": "panel",
            "background": self.background,
            "border_radius": self.border_radius,
            "border_color": self.border_color,
            "border_width": self.border_width,
            "padding": self.padding,
        })
        return base

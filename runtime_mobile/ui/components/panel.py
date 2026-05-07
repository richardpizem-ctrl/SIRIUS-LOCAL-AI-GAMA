# ============================================================
# SIRIUS LOCAL AI GAMA - Panel Component
# Version: 3.0.0-pre
# ============================================================

from .container import Container
from ..theme import MobileUITheme


class Panel(Container):

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, layout=None, component_id=None, visible=True):
        super().__init__(layout=layout, component_id=component_id, visible=visible)

        # Panel-specific visual properties
        self.background = MobileUITheme.COLORS["panel"]
        self.border_radius = MobileUITheme.BORDER_RADIUS["md"]
        self.border_color = MobileUITheme.COLORS["border"]
        self.border_width = 1
        self.padding = MobileUITheme.SPACING["lg"]

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()

        base.update({
            "type": "panel",
            "background": self.background,
            "border_radius": self.border_radius,
            "border_color": self.border_color,
            "border_width": self.border_width,
            "padding": self.padding
        })

        return base

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        """Forward events to layout if present."""
        if self.layout and hasattr(self.layout, "on_event"):
            return self.layout.on_event(event)

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
            "type": "panel",
            "background": self.background,
            "border_radius": self.border_radius,
            "border_color": self.border_color,
            "border_width": self.border_width,
            "padding": self.padding
        })
        return base

# ============================================================
# SIRIUS LOCAL AI GAMA - Container Component
# Version: 3.0.0-pre
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Container(BaseUIComponent):

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, layout=None, component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        self.layout = layout
        self.background = MobileUITheme.COLORS["surface"]
        self.padding = MobileUITheme.SPACING["md"]

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()

        layout_info = None
        if self.layout:
            layout_info = self.layout.initialize()

        base.update({
            "layout": layout_info,
            "background": self.background,
            "padding": self.padding
        })
        return base

    def update(self):
        base = super().update()

        layout_info = None
        if self.layout:
            layout_info = self.layout.update()

        base.update({
            "layout": layout_info
        })
        return base

    def render(self):
        base = super().render()

        layout_render = None
        if self.layout:
            layout_render = self.layout.render()

        base.update({
            "type": "container",
            "background": self.background,
            "padding": self.padding,
            "layout": layout_render,
        })
        return base

    def shutdown(self):
        layout_info = None
        if self.layout:
            layout_info = self.layout.shutdown()

        base = super().shutdown()
        base.update({"layout": layout_info})
        return base

    # ------------------------------------------------------------
    # Layout Management
    # ------------------------------------------------------------

    def set_layout(self, layout):
        """Replace current layout."""
        self.layout = layout

    def clear_layout(self):
        """Remove layout."""
        self.layout = None

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        """Forward UI events to layout if needed."""
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
            "type": "container",
            "background": self.background,
            "padding": self.padding,
            "layout": self.layout.get_info() if self.layout else None
        })
        return base

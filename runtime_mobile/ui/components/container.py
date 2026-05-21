# ============================================================
# SIRIUS LOCAL AI GAMA - Container Component
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - layout invalidation (needs_layout, dirty)
# - event bubbling + layout event routing
# - unified metadata schema v3
# - safe layout lifecycle delegation
# - background + padding rendering v3
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Container(BaseUIComponent):

    COMPONENT_VERSION = "3.1.0"

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
            try:
                layout_info = self.layout.initialize()
            except Exception as e:
                layout_info = {"error": str(e)}

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
            try:
                layout_info = self.layout.update()
            except Exception as e:
                layout_info = {"error": str(e)}

        base.update({
            "layout": layout_info
        })
        return base

    def render(self):
        base = super().render()

        layout_render = None
        if self.layout:
            try:
                layout_render = self.layout.render()
            except Exception as e:
                layout_render = {"error": str(e)}

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
            try:
                layout_info = self.layout.shutdown()
            except Exception as e:
                layout_info = {"error": str(e)}

        base = super().shutdown()
        base.update({"layout": layout_info})
        return base

    # ------------------------------------------------------------
    # Layout Management
    # ------------------------------------------------------------

    def set_layout(self, layout):
        """Replace current layout."""
        self.layout = layout
        self.needs_layout = True
        self.dirty = True

    def clear_layout(self):
        """Remove layout."""
        self.layout = None
        self.needs_layout = True
        self.dirty = True

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Forward UI events to layout if needed.
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
            "type": "container",
            "background": self.background,
            "padding": self.padding,
            "layout": self.layout.get_info() if self.layout else None
        })
        return base

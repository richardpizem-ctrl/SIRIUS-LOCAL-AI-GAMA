# ============================================================
# SIRIUS LOCAL AI GAMA - Stack Layout
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - z-index layering v3
# - safe component rendering
# - event bubbling (top → bottom)
# - layout invalidation (dirty, needs_layout)
# - unified metadata schema v3
# ============================================================

from .base_layout import BaseUILayout
from ..theme import MobileUITheme


class StackLayout(BaseUILayout):

    LAYOUT_VERSION = "3.1.0"

    def __init__(self, layout_id=None, visible=True):
        super().__init__(layout_id=layout_id, visible=visible)
        self.padding = MobileUITheme.SPACING["md"]

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "padding": self.padding
        })
        return base

    def update(self):
        return super().update()

    # ------------------------------------------------------------
    # Render (UI Engine 3.1)
    # ------------------------------------------------------------

    def render(self):
        base = {
            "status": "rendered",
            "layout": self.layout_id,
            "type": "stack",
            "background": self.background,
            "padding": self.padding,
            "visible": self.visible,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
        }

        rendered_components = []
        z_index = 0

        for component in self.components:
            try:
                c = component.render()
            except Exception as e:
                c = {"error": str(e), "component": component.component_id}

            c["z_index"] = z_index
            c["padding"] = self.padding

            rendered_components.append(c)
            z_index += 1

        base["components"] = rendered_components
        self.needs_render = False
        return base

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        StackLayout forwards events from TOP to BOTTOM.
        Top-most component receives the event first.
        """
        results = []

        for component in reversed(self.components):
            if hasattr(component, "on_event"):
                try:
                    results.append(component.on_event(event))
                except Exception as e:
                    results.append({
                        "status": "error",
                        "error": str(e),
                        "component": component.component_id
                    })

        return {
            "status": "events_forwarded",
            "layout": self.layout_id,
            "results": results,
            "bubble": True
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "type": "stack",
            "padding": self.padding,
            "background": self.background,
            "components": [c.component_id for c in self.components]
        })
        return base

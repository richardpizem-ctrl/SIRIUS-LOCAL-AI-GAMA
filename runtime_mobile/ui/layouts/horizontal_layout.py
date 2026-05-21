# ============================================================
# SIRIUS LOCAL AI GAMA - Horizontal Layout
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - layout invalidation (dirty, needs_layout)
# - safe component rendering
# - vertical alignment v3 (top/center/bottom)
# - event bubbling
# - unified metadata schema v3
# ============================================================

from .base_layout import BaseUILayout
from ..theme import MobileUITheme


class HorizontalLayout(BaseUILayout):

    LAYOUT_VERSION = "3.1.0"

    def __init__(self, layout_id=None, visible=True):
        super().__init__(layout_id=layout_id, visible=visible)

        # Padding
        self.padding_left = MobileUITheme.SPACING["lg"]
        self.padding_right = MobileUITheme.SPACING["lg"]

        # Vertical alignment: "top", "center", "bottom"
        self.align_vertical = "center"

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "padding_left": self.padding_left,
            "padding_right": self.padding_right,
            "align_vertical": self.align_vertical,
        })
        return base

    def update(self):
        return super().update()

    # ------------------------------------------------------------
    # Render (UI Engine 3.1)
    # ------------------------------------------------------------

    def render(self):
        # Base layout metadata
        base = {
            "status": "rendered",
            "layout": self.layout_id,
            "type": "horizontal",
            "background": self.background,
            "spacing": self.spacing,
            "padding_left": self.padding_left,
            "padding_right": self.padding_right,
            "visible": self.visible,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
        }

        rendered_components = []
        x_offset = self.padding_left

        for component in self.components:
            try:
                c = component.render()
            except Exception as e:
                c = {"error": str(e), "component": component.component_id}

            # Determine width
            width = c.get("width")
            if width is None:
                width = component.width or 0

            # Vertical alignment
            if self.align_vertical == "top":
                y_offset = 0
            elif self.align_vertical == "bottom":
                y_offset = (self.height or 0) - (c.get("height") or 0)
            else:
                # center
                y_offset = ((self.height or 0) - (c.get("height") or 0)) / 2

            c["x_offset"] = x_offset
            c["y_offset"] = y_offset
            c["align_vertical"] = self.align_vertical

            rendered_components.append(c)
            x_offset += width + self.spacing

        base["components"] = rendered_components
        self.needs_render = False
        return base

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        results = []
        for c in self.components:
            if hasattr(c, "on_event"):
                try:
                    results.append(c.on_event(event))
                except Exception as e:
                    results.append({"status": "error", "error": str(e), "component": c.component_id})

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
            "type": "horizontal",
            "padding_left": self.padding_left,
            "padding_right": self.padding_right,
            "align_vertical": self.align_vertical,
            "spacing": self.spacing,
            "background": self.background,
            "components": [c.component_id for c in self.components],
        })
        return base

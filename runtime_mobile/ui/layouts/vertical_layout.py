# ============================================================
# SIRIUS LOCAL AI GAMA - Vertical Layout
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - layout invalidation (dirty, needs_layout)
# - safe component rendering
# - horizontal alignment v3 (left/center/right)
# - event bubbling
# - unified metadata schema v3
# ============================================================

from .base_layout import BaseUILayout
from ..theme import MobileUITheme


class VerticalLayout(BaseUILayout):

    LAYOUT_VERSION = "3.1.0"

    def __init__(self, layout_id=None, visible=True):
        super().__init__(layout_id=layout_id, visible=visible)

        # Padding
        self.padding_top = MobileUITheme.SPACING["lg"]
        self.padding_bottom = MobileUITheme.SPACING["lg"]

        # Horizontal alignment: "left", "center", "right"
        self.align_horizontal = "left"

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "padding_top": self.padding_top,
            "padding_bottom": self.padding_bottom,
            "align_horizontal": self.align_horizontal,
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
            "type": "vertical",
            "background": self.background,
            "spacing": self.spacing,
            "padding_top": self.padding_top,
            "padding_bottom": self.padding_bottom,
            "align_horizontal": self.align_horizontal,
            "visible": self.visible,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
        }

        rendered_components = []
        y_offset = self.padding_top

        for component in self.components:
            try:
                c = component.render()
            except Exception as e:
                c = {"error": str(e), "component": component.component_id}

            # Determine height
            height = c.get("height")
            if height is None:
                height = component.height or 0

            # Horizontal alignment
            if self.align_horizontal == "left":
                x_offset = 0
            elif self.align_horizontal == "right":
                x_offset = (self.width or 0) - (c.get("width") or 0)
            else:
                # center
                x_offset = ((self.width or 0) - (c.get("width") or 0)) / 2

            c["y_offset"] = y_offset
            c["x_offset"] = x_offset
            c["align_horizontal"] = self.align_horizontal

            rendered_components.append(c)
            y_offset += height + self.spacing

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
                    results.append({
                        "status": "error",
                        "error": str(e),
                        "component": c.component_id
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
            "type": "vertical",
            "padding_top": self.padding_top,
            "padding_bottom": self.padding_bottom,
            "align_horizontal": self.align_horizontal,
            "spacing": self.spacing,
            "background": self.background,
            "components": [c.component_id for c in self.components],
        })
        return base

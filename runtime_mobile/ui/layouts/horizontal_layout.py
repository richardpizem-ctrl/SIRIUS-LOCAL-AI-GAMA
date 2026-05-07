# ============================================================
# SIRIUS LOCAL AI GAMA - Horizontal Layout
# Version: 3.0.0-pre
# ============================================================

from .base_layout import BaseUILayout
from ..theme import MobileUITheme


class HorizontalLayout(BaseUILayout):

    LAYOUT_VERSION = "3.0.0-pre"

    def __init__(self, layout_id=None, visible=True):
        super().__init__(layout_id=layout_id, visible=visible)

        self.padding_left = MobileUITheme.SPACING["lg"]
        self.padding_right = MobileUITheme.SPACING["lg"]

        # Vertical alignment: top, center, bottom
        self.align_vertical = "center"

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "padding_left": self.padding_left,
            "padding_right": self.padding_right,
            "align_vertical": self.align_vertical
        })
        return base

    def update(self):
        base = super().update()
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
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
            c = component.render()

            width = c.get("width")
            if width is None:
                width = component.width or 0

            c["x_offset"] = x_offset
            c["y_offset"] = 0
            c["align_vertical"] = self.align_vertical

            rendered_components.append(c)
            x_offset += width + self.spacing

        base["components"] = rendered_components
        return base

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        results = []
        for c in self.components:
            if hasattr(c, "on_event"):
                results.append(c.on_event(event))
        return {
            "status": "events_forwarded",
            "layout": self.layout_id,
            "results": results
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
            "components": [c.component_id for c in self.components]
        })
        return base

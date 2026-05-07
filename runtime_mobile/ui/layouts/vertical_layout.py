# ============================================================
# SIRIUS LOCAL AI GAMA - Vertical Layout
# Version: 3.0.0-pre
# ============================================================

from .base_layout import BaseUILayout
from ..theme import MobileUITheme


class VerticalLayout(BaseUILayout):

    LAYOUT_VERSION = "3.0.0-pre"

    def __init__(self, layout_id=None, visible=True):
        super().__init__(layout_id=layout_id, visible=visible)

        self.padding_top = MobileUITheme.SPACING["lg"]
        self.padding_bottom = MobileUITheme.SPACING["lg"]

        # Horizontal alignment: left, center, right
        self.align_horizontal = "left"

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "padding_top": self.padding_top,
            "padding_bottom": self.padding_bottom,
            "align_horizontal": self.align_horizontal
        })
        return base

    def update(self):
        return super().update()

    # ------------------------------------------------------------
    # Render
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
            "height": self.height
        }

        rendered_components = []
        y_offset = self.padding_top

        for component in self.components:
            c = component.render()

            height = c.get("height")
            if height is None:
                height = component.height or 0

            c["y_offset"] = y_offset
            c["x_offset"] = 0
            c["align_horizontal"] = self.align_horizontal

            rendered_components.append(c)
            y_offset += height + self.spacing

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
            "type": "vertical",
            "padding_top": self.padding_top,
            "padding_bottom": self.padding_bottom,
            "align_horizontal": self.align_horizontal,
            "spacing": self.spacing,
            "background": self.background,
            "components": [c.component_id for c in self.components]
        })
        return base

# ============================================================
# SIRIUS LOCAL AI GAMA - Stack Layout
# Version: 3.0.0-pre
# ============================================================

from .base_layout import BaseUILayout
from ..theme import MobileUITheme


class StackLayout(BaseUILayout):

    LAYOUT_VERSION = "3.0.0-pre"

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
    # Render
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
            "height": self.height
        }

        rendered_components = []
        z_index = 0

        for component in self.components:
            c = component.render()

            c["z_index"] = z_index
            c["padding"] = self.padding

            rendered_components.append(c)
            z_index += 1

        base["components"] = rendered_components
        return base

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        StackLayout forwards events to components from top to bottom.
        The top-most component receives the event first.
        """
        results = []

        for component in reversed(self.components):
            if hasattr(component, "on_event"):
                results.append(component.on_event(event))

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
            "type": "stack",
            "padding": self.padding,
            "background": self.background,
            "components": [c.component_id for c in self.components]
        })
        return base

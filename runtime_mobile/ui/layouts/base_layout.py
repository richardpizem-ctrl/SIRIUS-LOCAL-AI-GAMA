# ============================================================
# SIRIUS LOCAL AI GAMA - Base UI Layout
# Version: 3.0.0-pre
# ============================================================

from ..components.base_component import BaseUIComponent
from ..theme import MobileUITheme


class BaseUILayout:

    LAYOUT_VERSION = "3.0.0-pre"

    def __init__(self, layout_id=None, visible=True):
        self.layout_id = layout_id or self.__class__.__name__
        self.visible = visible
        self.components = []

        self.spacing = MobileUITheme.SPACING["md"]
        self.background = MobileUITheme.COLORS["surface"]

        # Layout bounding box (UI Manager fills these)
        self.x = 0
        self.y = 0
        self.width = None
        self.height = None

    # ------------------------------------------------------------
    # Component Management
    # ------------------------------------------------------------

    def add_component(self, component: BaseUIComponent):
        self.components.append(component)
        return {
            "status": "component_added",
            "layout": self.layout_id,
            "component": component.component_id
        }

    def insert_component(self, index: int, component: BaseUIComponent):
        self.components.insert(index, component)
        return {
            "status": "component_inserted",
            "layout": self.layout_id,
            "index": index,
            "component": component.component_id
        }

    def remove_component(self, component: BaseUIComponent):
        if component in self.components:
            self.components.remove(component)
            return {
                "status": "component_removed",
                "layout": self.layout_id,
                "component": component.component_id
            }
        return {"status": "error", "reason": "component_not_found"}

    def clear_components(self):
        self.components = []
        return {"status": "components_cleared", "layout": self.layout_id}

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        initialized = [c.initialize() for c in self.components]
        return {
            "status": "initialized",
            "layout": self.layout_id,
            "background": self.background,
            "spacing": self.spacing,
            "components": initialized
        }

    def update(self):
        updates = [c.update() for c in self.components]
        return {
            "status": "updated",
            "layout": self.layout_id,
            "components": updates
        }

    def render(self):
        rendered = [c.render() for c in self.components]
        return {
            "status": "rendered",
            "layout": self.layout_id,
            "background": self.background,
            "spacing": self.spacing,
            "components": rendered,
            "visible": self.visible,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height
        }

    def shutdown(self):
        shutdowns = [c.shutdown() for c in self.components]
        return {
            "status": "shutdown",
            "layout": self.layout_id,
            "components": shutdowns
        }

    # ------------------------------------------------------------
    # Event routing
    # ------------------------------------------------------------

    def on_event(self, event):
        """Forward events to all components."""
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
        return {
            "layout": self.layout_id,
            "version": self.LAYOUT_VERSION,
            "visible": self.visible,
            "background": self.background,
            "spacing": self.spacing,
            "components": [c.component_id for c in self.components],
            "count": len(self.components)
        }

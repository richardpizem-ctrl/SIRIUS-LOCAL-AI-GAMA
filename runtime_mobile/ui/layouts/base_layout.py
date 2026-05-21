# ============================================================
# SIRIUS LOCAL AI GAMA - Base UI Layout
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - layout invalidation (dirty, needs_layout)
# - event bubbling + safe component routing
# - unified metadata schema v3
# - safe lifecycle delegation
# - background + spacing rendering v3
# ============================================================

from ..components.base_component import BaseUIComponent
from ..theme import MobileUITheme


class BaseUILayout:

    LAYOUT_VERSION = "3.1.0"

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

        # Layout Engine 3.1 flags
        self.dirty = True
        self.needs_layout = True
        self.needs_render = True

    # ------------------------------------------------------------
    # Component Management
    # ------------------------------------------------------------

    def add_component(self, component: BaseUIComponent):
        self.components.append(component)
        self.needs_layout = True
        self.dirty = True
        return {
            "status": "component_added",
            "layout": self.layout_id,
            "component": component.component_id
        }

    def insert_component(self, index: int, component: BaseUIComponent):
        self.components.insert(index, component)
        self.needs_layout = True
        self.dirty = True
        return {
            "status": "component_inserted",
            "layout": self.layout_id,
            "index": index,
            "component": component.component_id
        }

    def remove_component(self, component: BaseUIComponent):
        if component in self.components:
            self.components.remove(component)
            self.needs_layout = True
            self.dirty = True
            return {
                "status": "component_removed",
                "layout": self.layout_id,
                "component": component.component_id
            }
        return {"status": "error", "reason": "component_not_found"}

    def clear_components(self):
        self.components = []
        self.needs_layout = True
        self.dirty = True
        return {"status": "components_cleared", "layout": self.layout_id}

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        initialized = []
        for c in self.components:
            try:
                initialized.append(c.initialize())
            except Exception as e:
                initialized.append({"error": str(e), "component": c.component_id})

        return {
            "status": "initialized",
            "layout": self.layout_id,
            "background": self.background,
            "spacing": self.spacing,
            "components": initialized
        }

    def update(self):
        updates = []
        for c in self.components:
            try:
                updates.append(c.update())
            except Exception as e:
                updates.append({"error": str(e), "component": c.component_id})

        return {
            "status": "updated",
            "layout": self.layout_id,
            "components": updates
        }

    def render(self):
        rendered = []
        for c in self.components:
            try:
                rendered.append(c.render())
            except Exception as e:
                rendered.append({"error": str(e), "component": c.component_id})

        self.needs_render = False

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
            "height": self.height,
        }

    def shutdown(self):
        shutdowns = []
        for c in self.components:
            try:
                shutdowns.append(c.shutdown())
            except Exception as e:
                shutdowns.append({"error": str(e), "component": c.component_id})

        return {
            "status": "shutdown",
            "layout": self.layout_id,
            "components": shutdowns
        }

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Forward events to all components.
        Components may choose to bubble or stop propagation.
        """
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
        return {
            "layout": self.layout_id,
            "version": self.LAYOUT_VERSION,
            "visible": self.visible,
            "background": self.background,
            "spacing": self.spacing,
            "components": [c.component_id for c in self.components],
            "count": len(self.components),
            "flags": {
                "dirty": self.dirty,
                "needs_layout": self.needs_layout,
                "needs_render": self.needs_render,
            },
            "bounds": {
                "x": self.x,
                "y": self.y,
                "width": self.width,
                "height": self.height,
            }
        }

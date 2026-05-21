# ============================================================
# SIRIUS LOCAL AI GAMA - Base UI Component
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - layout flags (dirty, needs_layout, needs_render)
# - animation hooks (on_animate)
# - event bubbling support
# - unified metadata schema v3
# - safe rendering contract for Layout Engine 3.1
# ============================================================

class BaseUIComponent:
    """
    Base class for all UI components in the GAMA Mobile UI.
    Provides a consistent API for rendering, updating, events,
    layout metadata, animation hooks, and component introspection.
    """

    COMPONENT_VERSION = "3.1.0"

    def __init__(self, component_id=None, visible=True):
        self.component_id = component_id or self.__class__.__name__
        self.visible = visible

        # Layout metadata (read by UI Manager + Layout Engine)
        self.x = 0
        self.y = 0
        self.width = None
        self.height = None
        self.z_index = 0

        # Layout flags (UI Engine 3.1)
        self.dirty = True
        self.needs_layout = True
        self.needs_render = True

        # Animation state (optional)
        self.animations = []

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        """Called once when the component is created."""
        return {
            "status": "initialized",
            "component": self.component_id,
            "version": self.COMPONENT_VERSION,
            "visible": self.visible,
            "type": self.__class__.__name__,
        }

    def update(self):
        """Called every frame by UI Manager."""
        return {
            "status": "updated",
            "component": self.component_id
        }

    def render(self):
        """Called by Rendering Engine 3.1."""
        self.needs_render = False
        return {
            "status": "rendered",
            "component": self.component_id,
            "visible": self.visible,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "z_index": self.z_index,
        }

    def shutdown(self):
        """Called when component is removed."""
        return {
            "status": "shutdown",
            "component": self.component_id
        }

    # ------------------------------------------------------------
    # Visibility
    # ------------------------------------------------------------

    def show(self):
        self.visible = True
        self.dirty = True

    def hide(self):
        self.visible = False
        self.dirty = True

    def toggle(self):
        self.visible = not self.visible
        self.dirty = True

    # ------------------------------------------------------------
    # Animation Hook (UI Engine 3.1)
    # ------------------------------------------------------------

    def on_animate(self, dt: float):
        """
        Called by Animation Engine 3.1.
        dt = delta time in seconds.
        Override in subclasses if needed.
        """
        return {
            "status": "animated",
            "component": self.component_id,
            "dt": dt,
        }

    # ------------------------------------------------------------
    # Event hook (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Override in subclasses to handle UI events.
        Return dict with:
            - status: "handled" | "ignored"
            - bubble: True/False (if event should bubble upward)
        """
        return {
            "status": "ignored",
            "bubble": True,
            "component": self.component_id,
            "event": event
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "component": self.component_id,
            "version": self.COMPONENT_VERSION,
            "visible": self.visible,
            "type": self.__class__.__name__,
            "layout": {
                "x": self.x,
                "y": self.y,
                "width": self.width,
                "height": self.height,
                "z_index": self.z_index,
            },
            "flags": {
                "dirty": self.dirty,
                "needs_layout": self.needs_layout,
                "needs_render": self.needs_render,
            },
            "animations": len(self.animations),
        }

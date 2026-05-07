# ============================================================
# SIRIUS LOCAL AI GAMA - Base UI Component
# Version: 3.0.0-pre
# ============================================================

class BaseUIComponent:
    """
    Base class for all UI components in the GAMA Mobile UI.
    Provides a consistent API for rendering, updating, events and metadata.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, component_id=None, visible=True):
        self.component_id = component_id or self.__class__.__name__
        self.visible = visible

        # Layout metadata (UI Manager reads these)
        self.x = 0
        self.y = 0
        self.width = None
        self.height = None
        self.z_index = 0

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        return {
            "status": "initialized",
            "component": self.component_id,
            "version": self.COMPONENT_VERSION,
            "visible": self.visible,
            "type": self.__class__.__name__,
        }

    def update(self):
        return {
            "status": "updated",
            "component": self.component_id
        }

    def render(self):
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
        return {
            "status": "shutdown",
            "component": self.component_id
        }

    # ------------------------------------------------------------
    # Visibility
    # ------------------------------------------------------------

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def toggle(self):
        self.visible = not self.visible

    # ------------------------------------------------------------
    # Event hook
    # ------------------------------------------------------------

    def on_event(self, event):
        """Override in subclasses to handle UI events."""
        return {
            "status": "ignored",
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
            }
        }

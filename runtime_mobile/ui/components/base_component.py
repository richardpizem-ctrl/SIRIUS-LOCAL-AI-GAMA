# ============================================================
# SIRIUS LOCAL AI GAMA - Base UI Component
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Abstract base class for all UI components.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

class BaseUIComponent:
    """
    Base class for all UI components in the GAMA Mobile UI.
    Provides a consistent API for rendering, updating and metadata.
    """

    COMPONENT_VERSION = "3.0.0-pre"

    def __init__(self, component_id=None, visible=True):
        self.component_id = component_id or self.__class__.__name__
        self.visible = visible

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        """
        Called once when the component is created.
        Override in subclasses.
        """
        return {
            "status": "initialized",
            "component": self.component_id
        }

    def update(self):
        """
        Called repeatedly by the UI manager.
        Override in subclasses.
        """
        return {
            "status": "updated",
            "component": self.component_id
        }

    def render(self):
        """
        Placeholder render method.
        In UI 3.0.0 this will be implemented by the rendering engine.
        """
        return {
            "status": "rendered",
            "component": self.component_id,
            "visible": self.visible
        }

    def shutdown(self):
        """
        Called when the component is being removed or UI is closing.
        """
        return {
            "status": "shutdown",
            "component": self.component_id
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "component": self.component_id,
            "version": self.COMPONENT_VERSION,
            "visible": self.visible
        }

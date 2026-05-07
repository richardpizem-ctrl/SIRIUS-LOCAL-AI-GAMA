# ============================================================
# SIRIUS LOCAL AI GAMA - Base UI Layout
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Abstract base layout for arranging UI components.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
# ============================================================

from ..components.base_component import BaseUIComponent
from ..theme import MobileUITheme


class BaseUILayout:
    """
    Base class for all UI layouts.
    A layout manages a collection of UI components and defines
    how they are arranged on the screen.
    """

    LAYOUT_VERSION = "3.0.0-pre"

    def __init__(self, layout_id=None, visible=True):
        self.layout_id = layout_id or self.__class__.__name__
        self.visible = visible
        self.components = []

        # Theme defaults
        self.spacing = MobileUITheme.SPACING["md"]
        self.background = MobileUITheme.COLORS["surface"]

    # ------------------------------------------------------------
    # Component Management
    # ------------------------------------------------------------

    def add_component(self, component: BaseUIComponent):
        """Add a UI component to the layout."""
        self.components.append(component)
        return {
            "status": "component_added",
            "layout": self.layout_id,
            "component": component.component_id
        }

    def remove_component(self, component: BaseUIComponent):
        """Remove a UI component from the layout."""
        if component in self.components:
            self.components.remove(component)
            return {
                "status": "component_removed",
                "layout": self.layout_id,
                "component": component.component_id
            }

        return {
            "status": "error",
            "reason": "component_not_found"
        }

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        """Initialize layout and all components."""
        initialized = []
        for c in self.components:
            initialized.append(c.initialize())

        return {
            "status": "initialized",
            "layout": self.layout_id,
            "components": initialized
        }

    def update(self):
        """Update layout and all components."""
        updates = []
        for c in self.components:
            updates.append(c.update())

        return {
            "status": "updated",
            "layout": self.layout_id,
            "components": updates
        }

    def render(self):
        """
        Placeholder render output.
        In UI 3.0.0 this will be handled by the rendering engine.
        """
        rendered = []
        for c in self.components:
            rendered.append(c.render())

        return {
            "status": "rendered",
            "layout": self.layout_id,
            "background": self.background,
            "spacing": self.spacing,
            "components": rendered,
            "visible": self.visible
        }

    def shutdown(self):
        """Shutdown layout and all components."""
        shutdowns = []
        for c in self.components:
            shutdowns.append(c.shutdown())

        return {
            "status": "shutdown",
            "layout": self.layout_id,
            "components": shutdowns
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "layout": self.layout_id,
            "version": self.LAYOUT_VERSION,
            "components": len(self.components),
            "visible": self.visible
        }

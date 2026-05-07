# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile UI Main Window
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Minimal UI shell for the mobile runtime.
# This is a framework-agnostic placeholder:
# - no pygame
# - no tkinter
# - no kivy
# - no qt
#
# The purpose is to provide a stable API for UI 3.0.0.
# ============================================================

class MobileMainWindow:
    """
    Minimal UI container for GAMA 3.0.0-pre.
    This class does NOT render anything visually.
    It only defines the structure expected by future UI engines.
    """

    UI_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context
        self.title = "SIRIUS LOCAL AI – Mobile Runtime"
        self.width = 360
        self.height = 640

        # Future: attach UI components
        self.components = []

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        """
        Called once when the UI is created.
        """
        return {
            "status": "initialized",
            "ui_version": self.UI_VERSION,
            "title": self.title,
            "size": (self.width, self.height)
        }

    def update(self):
        """
        Called repeatedly by the runtime loop.
        This is where UI would refresh in a real engine.
        """
        return {
            "status": "updated",
            "components": len(self.components)
        }

    def shutdown(self):
        """
        Called when the UI is being closed.
        """
        return {
            "status": "shutdown",
            "ui_version": self.UI_VERSION
        }

    # ------------------------------------------------------------
    # Component Management
    # ------------------------------------------------------------

    def add_component(self, component):
        """
        Add a UI component (placeholder).
        """
        self.components.append(component)
        return {
            "status": "component_added",
            "component": component.__class__.__name__
        }

    def remove_component(self, component):
        """
        Remove a UI component (placeholder).
        """
        if component in self.components:
            self.components.remove(component)
            return {
                "status": "component_removed",
                "component": component.__class__.__name__
            }

        return {
            "status": "error",
            "reason": "component_not_found"
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "module": "ui.main_window",
            "version": self.UI_VERSION,
            "components": len(self.components)
        }


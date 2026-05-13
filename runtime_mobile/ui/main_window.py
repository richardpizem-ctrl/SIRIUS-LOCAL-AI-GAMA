# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile UI Main Window
# Version: 3.0.0-pre
# ============================================================

class MobileMainWindow:

    UI_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context
        self.title = "SIRIUS LOCAL AI – Mobile Runtime"

        # Window geometry
        self.x = 0
        self.y = 0
        self.width = 360
        self.height = 640

        # Attached UI components (layouts or components)
        self.components = []

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        initialized = []
        for c in self.components:
            if hasattr(c, "initialize"):
                initialized.append(c.initialize())

        return {
            "status": "initialized",
            "ui_version": self.UI_VERSION,
            "title": self.title,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "components": initialized
        }

    def update(self):
        updates = []
        for c in self.components:
            if hasattr(c, "update"):
                updates.append(c.update())

        return {
            "status": "updated",
            "components": updates
        }

    def render(self):
        rendered = []
        for c in self.components:
            if hasattr(c, "render"):
                rendered.append(c.render())

        return {
            "status": "rendered",
            "window": self.title,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "components": rendered
        }

    def shutdown(self):
        shutdowns = []
        for c in self.components:
            if hasattr(c, "shutdown"):
                shutdowns.append(c.shutdown())

        return {
            "status": "shutdown",
            "ui_version": self.UI_VERSION,
            "components": shutdowns
        }

    # ------------------------------------------------------------
    # Component Management
    # ------------------------------------------------------------

    def add_component(self, component):
        self.components.append(component)

        if hasattr(component, "initialize"):
            component.initialize()

        return {
            "status": "component_added",
            "component": component.__class__.__name__
        }

    def remove_component(self, component):
        if component in self.components:
            if hasattr(component, "shutdown"):
                component.shutdown()

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
    # Event Routing
    # ------------------------------------------------------------

    def on_event(self, event):
        results = []
        for c in self.components:
            if hasattr(c, "on_event"):
                results.append(c.on_event(event))

        return {
            "status": "events_forwarded",
            "results": results
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        return {
            "module": "ui.main_window",
            "version": self.UI_VERSION,
            "components": len(self.components),
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height
        }

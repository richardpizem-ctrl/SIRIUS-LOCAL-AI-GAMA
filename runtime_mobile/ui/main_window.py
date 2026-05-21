# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile UI Main Window
# Version: 3.1.0
# ============================================================

class MobileMainWindow:

    UI_VERSION = "3.1.0"

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

        # Window state flags (UI Engine 3.1)
        self.visible = True
        self.dirty = True
        self.needs_layout = True
        self.needs_render = True

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        initialized = []
        for c in self.components:
            if hasattr(c, "initialize"):
                try:
                    initialized.append(c.initialize())
                except Exception as e:
                    initialized.append({"error": str(e), "component": c.__class__.__name__})

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
                try:
                    updates.append(c.update())
                except Exception as e:
                    updates.append({"error": str(e), "component": c.__class__.__name__})

        return {
            "status": "updated",
            "components": updates
        }

    def render(self):
        rendered = []
        for c in self.components:
            if hasattr(c, "render"):
                try:
                    rendered.append(c.render())
                except Exception as e:
                    rendered.append({"error": str(e), "component": c.__class__.__name__})

        self.needs_render = False

        return {
            "status": "rendered",
            "window": self.title,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "visible": self.visible,
            "components": rendered
        }

    def shutdown(self):
        shutdowns = []
        for c in self.components:
            if hasattr(c, "shutdown"):
                try:
                    shutdowns.append(c.shutdown())
                except Exception as e:
                    shutdowns.append({"error": str(e), "component": c.__class__.__name__})

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
        self.needs_layout = True
        self.dirty = True

        if hasattr(component, "initialize"):
            try:
                component.initialize()
            except Exception:
                # Initialization errors are reported via initialize(), not here
                pass

        return {
            "status": "component_added",
            "component": component.__class__.__name__
        }

    def remove_component(self, component):
        if component in self.components:
            if hasattr(component, "shutdown"):
                try:
                    component.shutdown()
                except Exception:
                    pass

            self.components.remove(component)
            self.needs_layout = True
            self.dirty = True

            return {
                "status": "component_removed",
                "component": component.__class__.__name__
            }

        return {
            "status": "error",
            "reason": "component_not_found"
        }

    # ------------------------------------------------------------
    # Event Routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        results = []
        for c in self.components:
            if hasattr(c, "on_event"):
                try:
                    results.append(c.on_event(event))
                except Exception as e:
                    results.append({
                        "status": "error",
                        "error": str(e),
                        "component": c.__class__.__name__
                    })

        return {
            "status": "events_forwarded",
            "window": self.title,
            "results": results,
            "bubble": True
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
            "height": self.height,
            "visible": self.visible,
            "flags": {
                "dirty": self.dirty,
                "needs_layout": self.needs_layout,
                "needs_render": self.needs_render,
            }
        }

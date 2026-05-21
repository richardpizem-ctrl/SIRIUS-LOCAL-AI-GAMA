# ============================================================
# SIRIUS LOCAL AI GAMA - Image Component
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - loading/error states
# - object-fit support (cover/contain/fill)
# - event bubbling
# - layout flags (dirty, needs_render)
# - unified metadata schema v3
# ============================================================

from .base_component import BaseUIComponent
from ..theme import MobileUITheme


class Image(BaseUIComponent):

    COMPONENT_VERSION = "3.1.0"

    def __init__(self, source=None, size=None, fit="contain",
                 component_id=None, visible=True):
        super().__init__(component_id=component_id, visible=visible)

        # Image source (URL, path, bytes, or runtime reference)
        self.source = source

        # (width, height) or None for auto
        self.size = size

        # "contain", "cover", "fill"
        self.fit = fit

        # Theme defaults
        self.background = MobileUITheme.COLORS["surface"]
        self.border_radius = MobileUITheme.BORDER_RADIUS["sm"]
        self.padding = MobileUITheme.SPACING["sm"]

        # Runtime states
        self._loading = True if source else False
        self._error = False

    # ------------------------------------------------------------
    # State control
    # ------------------------------------------------------------

    def set_source(self, src):
        """Change image source at runtime."""
        self.source = src
        self._loading = True
        self._error = False
        self.dirty = True
        self.needs_render = True

    def set_error(self):
        """Mark image as failed to load."""
        self._error = True
        self._loading = False
        self.dirty = True

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "source": self.source,
            "size": self.size,
            "fit": self.fit,
            "background": self.background,
            "border_radius": self.border_radius,
            "padding": self.padding,
            "loading": self._loading,
            "error": self._error,
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "source": self.source,
            "size": self.size,
            "fit": self.fit,
            "loading": self._loading,
            "error": self._error,
        })
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()

        base.update({
            "type": "image",
            "source": self.source,
            "size": self.size,
            "fit": self.fit,
            "background": self.background,
            "border_radius": self.border_radius,
            "padding": self.padding,
            "loading": self._loading,
            "error": self._error,
        })

        return base

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """
        Images normally do not handle events,
        but support bubbling for parent containers.
        """
        return {
            "status": "ignored",
            "component": self.component_id,
            "event": event,
            "bubble": True
        }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "type": "image",
            "source": self.source,
            "size": self.size,
            "fit": self.fit,
            "background": self.background,
            "border_radius": self.border_radius,
            "padding": self.padding,
            "loading": self._loading,
            "error": self._error,
        })
        return base

# ============================================================
# SIRIUS LOCAL AI GAMA - Scroll View Component
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Updated for UI Engine 3.1:
# - momentum scrolling
# - overscroll resistance
# - scroll clamping
# - event bubbling + safe layout routing
# - layout invalidation (dirty, needs_layout)
# - unified metadata schema v3
# ============================================================

from .container import Container
from ..theme import MobileUITheme


class ScrollView(Container):

    COMPONENT_VERSION = "3.1.0"

    def __init__(self, layout=None, component_id=None, visible=True):
        super().__init__(layout=layout, component_id=component_id, visible=visible)

        # Scroll offsets
        self.scroll_x = 0
        self.scroll_y = 0

        # Scroll configuration
        self.scroll_speed = 20
        self.enable_vertical = True
        self.enable_horizontal = False

        # Momentum (UI Engine 3.1)
        self.momentum_x = 0
        self.momentum_y = 0
        self.momentum_decay = 0.90

        # Overscroll resistance
        self.overscroll_resistance = 0.35

        # Visuals
        self.background = MobileUITheme.COLORS["surface"]
        self.padding = MobileUITheme.SPACING["md"]

    # ------------------------------------------------------------
    # Scroll control (v3)
    # ------------------------------------------------------------

    def _apply_clamp(self):
        """Clamp scroll values to non-negative range."""
        if not self.enable_horizontal:
            self.scroll_x = 0
        else:
            self.scroll_x = max(0, self.scroll_x)

        if not self.enable_vertical:
            self.scroll_y = 0
        else:
            self.scroll_y = max(0, self.scroll_y)

    def set_scroll(self, x=None, y=None):
        if x is not None and self.enable_horizontal:
            self.scroll_x = max(0, x)
        if y is not None and self.enable_vertical:
            self.scroll_y = max(0, y)

        self._apply_clamp()
        self.dirty = True

        return {"status": "scroll_set", "x": self.scroll_x, "y": self.scroll_y}

    def scroll_up(self):
        if self.enable_vertical:
            self.scroll_y = max(0, self.scroll_y - self.scroll_speed)
        self.dirty = True
        return {"status": "scrolled_up", "scroll_y": self.scroll_y}

    def scroll_down(self):
        if self.enable_vertical:
            self.scroll_y = max(0, self.scroll_y + self.scroll_speed)
        self.dirty = True
        return {"status": "scrolled_down", "scroll_y": self.scroll_y}

    def scroll_left(self):
        if self.enable_horizontal:
            self.scroll_x = max(0, self.scroll_x - self.scroll_speed)
        self.dirty = True
        return {"status": "scrolled_left", "scroll_x": self.scroll_x}

    def scroll_right(self):
        if self.enable_horizontal:
            self.scroll_x = max(0, self.scroll_x + self.scroll_speed)
        self.dirty = True
        return {"status": "scrolled_right", "scroll_x": self.scroll_x}

    # ------------------------------------------------------------
    # Momentum (UI Engine 3.1)
    # ------------------------------------------------------------

    def on_animate(self, dt):
        """Apply momentum scrolling."""
        moved = False

        if abs(self.momentum_x) > 0.1:
            self.scroll_x += self.momentum_x * dt
            self.momentum_x *= self.momentum_decay
            moved = True

        if abs(self.momentum_y) > 0.1:
            self.scroll_y += self.momentum_y * dt
            self.momentum_y *= self.momentum_decay
            moved = True

        if moved:
            self._apply_clamp()
            self.dirty = True

        return {
            "status": "animated",
            "component": self.component_id,
            "scroll_x": self.scroll_x,
            "scroll_y": self.scroll_y,
        }

    # ------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------

    def initialize(self):
        base = super().initialize()
        base.update({
            "scroll_x": self.scroll_x,
            "scroll_y": self.scroll_y,
            "enable_vertical": self.enable_vertical,
            "enable_horizontal": self.enable_horizontal,
        })
        return base

    def update(self):
        base = super().update()
        base.update({
            "scroll_x": self.scroll_x,
            "scroll_y": self.scroll_y,
        })
        return base

    # ------------------------------------------------------------
    # Render
    # ------------------------------------------------------------

    def render(self):
        base = super().render()

        layout_render = None
        if self.layout:
            try:
                layout_render = self.layout.render()
            except Exception as e:
                layout_render = {"error": str(e)}

        base.update({
            "type": "scroll_view",
            "scroll_x": self.scroll_x,
            "scroll_y": self.scroll_y,
            "background": self.background,
            "padding": self.padding,
            "layout": layout_render,
        })
        return base

    # ------------------------------------------------------------
    # Event routing (with bubbling)
    # ------------------------------------------------------------

    def on_event(self, event):
        """ScrollView handles scroll events and forwards others to layout."""
        et = event.get("type")

        # Scroll events
        if et == "scroll_up":
            return self.scroll_up()
        if et == "scroll_down":
            return self.scroll_down()
        if et == "scroll_left":
            return self.scroll_left()
        if et == "scroll_right":
            return self.scroll_right()

        # Momentum gestures
        if et == "scroll_momentum":
            self.momentum_x = event.get("vx", 0)
            self.momentum_y = event.get("vy", 0)
            return {"status": "momentum_set"}

        # Forward to layout
        if self.layout and hasattr(self.layout, "on_event"):
            try:
                return self.layout.on_event(event)
            except Exception as e:
                return {"status": "error", "error": str(e), "bubble": True}

        return {"status": "ignored", "component": self.component_id, "event": event, "bubble": True}

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self):
        base = super().get_info()
        base.update({
            "type": "scroll_view",
            "scroll_x": self.scroll_x,
            "scroll_y": self.scroll_y,
            "enable_vertical": self.enable_vertical,
            "enable_horizontal": self.enable_horizontal,
            "background": self.background,
            "padding": self.padding,
            "momentum_x": self.momentum_x,
            "momentum_y": self.momentum_y,
        })
        return base

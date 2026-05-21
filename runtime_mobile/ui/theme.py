# ============================================================
# SIRIUS LOCAL AI GAMA - UI Theme
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Centralized theme configuration for the Mobile UI.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
#
# All UI components and layouts use this theme.
# ============================================================

class MobileUITheme:
    """
    Defines the global UI theme for GAMA Mobile Runtime.
    Includes colors, spacing, typography and component defaults.
    """

    THEME_VERSION = "3.1.0"

    # ------------------------------------------------------------
    # Colors (UI Engine 3.1)
    # ------------------------------------------------------------
    COLORS = {
        # Base surfaces
        "background": "#0D0D0D",
        "surface": "#1A1A1A",
        "surface_alt": "#161616",

        # Brand
        "primary": "#4A90E2",
        "primary_dark": "#357ABD",
        "accent": "#50E3C2",

        # Text
        "text": "#FFFFFF",
        "text_secondary": "#CCCCCC",
        "text_disabled": "#777777",
        "text_hover": "#E6E6E6",

        # States
        "error": "#FF4D4D",
        "warning": "#FFCC00",
        "success": "#00CC66",

        # Borders
        "border": "#2A2A2A",
        "disabled_border": "#555555",

        # Scrollbars / outlines
        "outline": "#3A3A3A",
        "outline_active": "#4A90E2",
    }

    # ------------------------------------------------------------
    # Typography (UI Engine 3.1)
    # ------------------------------------------------------------
    FONT = {
        "family": "Inter",

        # Sizes
        "size_xs": 10,
        "size_small": 12,
        "size_normal": 14,
        "size_large": 18,
        "size_title": 22,
        "size_headline": 26,
    }

    # ------------------------------------------------------------
    # Layout / Spacing (UI Engine 3.1)
    # ------------------------------------------------------------
    SPACING = {
        "xxs": 2,
        "xs": 4,
        "sm": 8,
        "md": 12,
        "lg": 16,
        "xl": 24,
        "xxl": 32,
    }

    # ------------------------------------------------------------
    # Border radius (UI Engine 3.1)
    # ------------------------------------------------------------
    BORDER_RADIUS = {
        "xs": 2,
        "sm": 4,
        "md": 6,
        "lg": 10,
        "xl": 14,
        "pill": 999,
        "circle": 9999,
    }

    # ------------------------------------------------------------
    # Component Defaults (UI Engine 3.1)
    # ------------------------------------------------------------
    COMPONENTS = {
        "button_height": 42,
        "input_height": 38,
        "slider_height": 24,
        "toggle_width": 40,
        "toggle_height": 22,
        "corner_radius": 6,
        "panel_padding": 16,
        "scroll_padding": 12,
    }

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------
    @classmethod
    def get_info(cls):
        return {
            "module": "ui.theme",
            "version": cls.THEME_VERSION,
            "colors": list(cls.COLORS.keys()),
            "font_family": cls.FONT["family"],
            "font_sizes": {k: v for k, v in cls.FONT.items() if k.startswith("size_")},
            "spacing_levels": list(cls.SPACING.keys()),
            "radius_levels": list(cls.BORDER_RADIUS.keys()),
            "component_defaults": list(cls.COMPONENTS.keys()),
        }

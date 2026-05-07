# ============================================================
# SIRIUS LOCAL AI GAMA - UI Theme
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Centralized theme configuration for the Mobile UI.
# Framework-agnostic: no pygame, no tkinter, no qt, no kivy.
#
# All UI components and layouts will use this theme.
# ============================================================

class MobileUITheme:
    """
    Defines the global UI theme for GAMA Mobile Runtime.
    This includes colors, spacing, typography and component defaults.
    """

    THEME_VERSION = "3.0.0-pre"

    # ------------------------------------------------------------
    # Colors
    # ------------------------------------------------------------
    COLORS = {
        "background": "#0D0D0D",
        "surface": "#1A1A1A",
        "primary": "#4A90E2",
        "primary_dark": "#357ABD",
        "accent": "#50E3C2",
        "text": "#FFFFFF",
        "text_secondary": "#CCCCCC",
        "error": "#FF4D4D",
        "warning": "#FFCC00",
        "success": "#00CC66",
    }

    # ------------------------------------------------------------
    # Typography
    # ------------------------------------------------------------
    FONT = {
        "family": "Inter",
        "size_small": 12,
        "size_normal": 14,
        "size_large": 18,
        "size_title": 22,
    }

    # ------------------------------------------------------------
    # Layout / Spacing
    # ------------------------------------------------------------
    SPACING = {
        "xs": 4,
        "sm": 8,
        "md": 12,
        "lg": 16,
        "xl": 24,
    }

    # ------------------------------------------------------------
    # Border radius
    # ------------------------------------------------------------
    BORDER_RADIUS = {
        "xs": 2,
        "sm": 4,
        "md": 6,
        "lg": 10,
        "xl": 14,
    }

    # ------------------------------------------------------------
    # Component Defaults
    # ------------------------------------------------------------
    COMPONENTS = {
        "button_height": 42,
        "input_height": 38,
        "corner_radius": 6,
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
            "font": cls.FONT["family"],
            "spacing_levels": list(cls.SPACING.keys()),
        }

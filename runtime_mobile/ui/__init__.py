# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile UI Package
# Version: 3.0.0-pre
# ============================================================

"""
GAMA Mobile UI package.

Provides:
- Base UI components (Button, TextLabel, Icon, Image, InputField, Toggle, Container, Panel, ScrollView)
- Base layouts (BaseUILayout, VerticalLayout, HorizontalLayout, StackLayout)
- Shared theme (MobileUITheme) for consistent styling across the runtime.
"""

from .theme import MobileUITheme

# Components
from .components.base_component import BaseUIComponent
from .components.button import Button
from .components.text_label import TextLabel
from .components.icon import Icon
from .components.image import Image
from .components.input_field import InputField
from .components.toggle import Toggle
from .components.container import Container
from .components.panel import Panel
from .components.scroll_view import ScrollView
from .components.slider import Slider

# Layouts
from .layouts.base_layout import BaseUILayout
from .layouts.vertical_layout import VerticalLayout
from .layouts.horizontal_layout import HorizontalLayout
from .layouts.stack_layout import StackLayout

UI_VERSION = "3.0.0-pre"

__all__ = [
    "UI_VERSION",
    "MobileUITheme",
    # Base
    "BaseUIComponent",
    "BaseUILayout",
    # Components
    "Button",
    "TextLabel",
    "Icon",
    "Image",
    "InputField",
    "Toggle",
    "Container",
    "Panel",
    "ScrollView",
    "Slider",
    # Layouts
    "VerticalLayout",
    "HorizontalLayout",
    "StackLayout",
]


# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Entry Point
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Bootstrap for the mobile runtime.
# Wires:
#   - runtime context
#   - dispatcher
#   - runtime core
#   - NL router
#   - UI manager + screens
#
# Framework-agnostic, no direct I/O or UI framework calls.
# ============================================================

from runtime_mobile.core.runtime_context import MobileRuntimeContext
from runtime_mobile.core.runtime_dispatcher import MobileRuntimeDispatcher
from runtime_mobile.core.runtime_core import MobileRuntimeCore
from runtime_mobile.core.router_mobile import MobileNLRouter

from runtime_mobile.ui.ui_manager import UIManager
from runtime_mobile.ui.screen_manager import ScreenManager
from runtime_mobile.ui.screens.home_screen import HomeScreen
from runtime_mobile.ui.screens.debug_screen import DebugScreen


def create_runtime():
    """
    Create and wire all core runtime objects.
    Returns a dict with references to main runtime components.
    """

    # --- Core context ---
    context = MobileRuntimeContext()

    # --- Dispatcher + runtime core ---
    dispatcher = MobileRuntimeDispatcher(context=context)
    runtime_core = MobileRuntimeCore(context=context, dispatcher=dispatcher)

    # --- NL router ---
    nl_router = MobileNLRouter()

    # --- UI layer ---
    ui_manager = UIManager(context=context)
    screen_manager = ScreenManager()

    # Screens
    home_screen = HomeScreen(screen_manager=screen_manager)
    debug_screen = DebugScreen(
        screen_manager=screen_manager,
        debug_provider=getattr(context, "get_debug_log", None),
    )

    screen_manager.register_screen("home", home_screen)
    screen_manager.register_screen("debug", debug_screen)
    screen_manager.set_screen("home")

    return {
        "context": context,
        "dispatcher": dispatcher,
        "runtime_core": runtime_core,
        "nl_router": nl_router,
        "ui_manager": ui_manager,
        "screen_manager": screen_manager,
    }


if __name__ == "__main__":
    # Minimal non-interactive bootstrap (no real loop, no I/O).
    runtime = create_runtime()
    core = runtime["runtime_core"]

    try:
        init_info = core.initialize()
        print("[RUNTIME INIT]", init_info)
    except Exception as e:
        print("[RUNTIME INIT ERROR]", str(e))

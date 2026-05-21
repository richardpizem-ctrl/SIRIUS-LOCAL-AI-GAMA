# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Core
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
# ============================================================

from typing import Any, Dict
from runtime_mobile.core.event import MobileEvent


class MobileRuntimeCore:
    RUNTIME_VERSION = "3.1.0"

    def __init__(self, context, dispatcher):
        self.context = context
        self.dispatcher = dispatcher

        # Optional subsystems (Diagnostics v3, EnergyGovernor v3)
        self.diagnostics = None
        self.energy_governor = None

    # ------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------

    def initialize(self) -> Dict[str, Any]:
        """
        Initializes the mobile runtime.
        Loads context modules and returns structured init info.
        """

        try:
            self.context.load()

            return {
                "status": "initialized",
                "runtime_version": self.RUNTIME_VERSION,
                "context_loaded": getattr(self.context, "loaded", False),
                "dispatcher_ready": self.dispatcher is not None,
            }

        except Exception as e:
            return {
                "status": "error",
                "type": "runtime_init_error",
                "error": str(e),
            }

    # ------------------------------------------------------------
    # Event Processing Pipeline (3.1)
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:

        # 1) Update context state
        try:
            self.context.update_last_event(event.type)
        except Exception as e:
            print(f"[WARN] Failed to update context event: {e}")

        # 2) Diagnostics v3 hook
        if self.diagnostics and hasattr(self.diagnostics, "on_event"):
            try:
                self.diagnostics.on_event(event)
            except Exception as e:
                print(f"[WARN] Diagnostics hook failed: {e}")

        # 3) Energy Governor v3
        if self.energy_governor and hasattr(self.energy_governor, "should_process"):
            try:
                if not self.energy_governor.should_process(event):
                    return {
                        "status": "skipped",
                        "reason": "energy_governor_blocked",
                        "event_type": event.type,
                    }
            except Exception as e:
                print(f"[WARN] Energy governor failed: {e}")

        # 4) Dispatch event
        try:
            result = self.dispatcher.dispatch(event)
        except Exception as e:
            return {
                "status": "error",
                "type": "runtime_dispatch_error",
                "error": str(e),
            }

        return result

    # ------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------

    def get_info(self) -> Dict[str, Any]:
        return {
            "runtime_version": self.RUNTIME_VERSION,
            "context_loaded": getattr(self.context, "loaded", False),
            "dispatcher_ready": self.dispatcher is not None,
            "diagnostics_attached": self.diagnostics is not None,
            "energy_governor_attached": self.energy_governor is not None,
        }

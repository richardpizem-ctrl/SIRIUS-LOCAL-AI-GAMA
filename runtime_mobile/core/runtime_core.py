# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Core
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Main orchestrator for the GAMA mobile runtime.
# Responsibilities:
#   - initialize runtime context + dispatcher
#   - process events
#   - update runtime state
#   - integrate modules (vision, knowledge, security, diagnostics…)
#   - provide safe execution pipeline
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

from typing import Any, Dict

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileRuntimeCore:
    """
    Central orchestrator for the GAMA mobile runtime.

    Version 3-ready features:
    - safe event pipeline
    - diagnostics hooks
    - energy governor hooks
    - unified event routing
    - runtime metadata
    """

    RUNTIME_VERSION = "3.0.0-pre"

    def __init__(self, context, dispatcher):
        self.context = context
        self.dispatcher = dispatcher

        # Optional injected modules (runtime will attach them)
        self.diagnostics = None
        self.energy_governor = None

    # ------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------

    def initialize(self) -> Dict[str, Any]:
        """
        Initializes the mobile runtime.
        Loads context modules.
        """
        try:
            self.context.load()
            return {
                "status": "initialized",
                "runtime_version": self.RUNTIME_VERSION,
                "context_loaded": getattr(self.context, "loaded", True),
            }
        except Exception as e:
            return {
                "status": "error",
                "type": "runtime_init_error",
                "error": str(e),
            }

    # ------------------------------------------------------------
    # Event Processing
    # ------------------------------------------------------------

    def handle_event(self, event: MobileEvent) -> Dict[str, Any]:
        """
        Main event processing pipeline.

        Steps:
        1. Update context state
        2. Run diagnostics hooks (if available)
        3. Run energy governor (if available)
        4. Dispatch event to correct module
        5. Return structured result
        """

        # 1) Update last event
        try:
            self.context.update_last_event(event)
        except Exception as e:
            print(f"[WARN] Failed to update context event: {e}")

        # 2) Diagnostics hook
        if self.diagnostics and hasattr(self.diagnostics, "on_event"):
            try:
                self.diagnostics.on_event(event)
            except Exception as e:
                print(f"[WARN] Diagnostics hook failed: {e}")

        # 3) Energy governor hook
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

        # 5) Return result
        return result

    # ------------------------------------------------------------
    # Runtime Metadata
    # ------------------------------------------------------------

    def get_info(self) -> Dict[str, Any]:
        """Return runtime metadata for diagnostics/UI."""
        return {
            "runtime_version": self.RUNTIME_VERSION,
            "context_loaded": getattr(self.context, "loaded", False),
            "dispatcher_ready": self.dispatcher is not None,
            "diagnostics_attached": self.diagnostics is not None,
            "energy_governor_attached": self.energy_governor is not None,
        }

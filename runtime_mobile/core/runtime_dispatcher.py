# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Dispatcher
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Central dispatcher for the GAMA mobile runtime.
# Responsibilities:
#   - route MobileEvent objects to correct modules
#   - provide safe dispatching
#   - support extended event types (diagnostics, governor, workflow)
#   - integrate with runtime context
#
# Fully prepared for GAMA 3.x architecture.
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes


class MobileRuntimeDispatcher:
    """
    Central dispatcher for the GAMA mobile runtime.
    Routes MobileEvent objects to the correct module.
    """

    DISPATCHER_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main Dispatch Entry
    # ------------------------------------------------------------

    def dispatch(self, event):
        """
        Dispatches an event to the correct module based on event.type.
        Returns the module response.
        """

        et = event.type

        # --------------------------------------------------------
        # SECURITY MODULE
        # --------------------------------------------------------
        if et in (
            MobileEventTypes.SECURITY,
            MobileEventTypes.RESTRICTED_MODE,
            MobileEventTypes.PERMISSION_CHECK,
        ):
            return self.context.security.handle_event(event)

        # --------------------------------------------------------
        # VISION MODULE
        # --------------------------------------------------------
        if et in (
            MobileEventTypes.OCR,
            MobileEventTypes.DETECT,
            MobileEventTypes.SCENE,
            MobileEventTypes.HOMEWORK,
        ):
            return self.context.vision.handle_event(event)

        # --------------------------------------------------------
        # KNOWLEDGE PACKS MODULE
        # --------------------------------------------------------
        if et in (
            MobileEventTypes.PACK_LOOKUP,
            MobileEventTypes.PACK_INFO,
        ):
            return self.context.packs.handle_event(event)

        # --------------------------------------------------------
        # DEVICE DIAGNOSTICS (GAMA 2.0 → 3.0)
        # --------------------------------------------------------
        if et in (
            MobileEventTypes.CHECK_BATTERY,
            MobileEventTypes.CHECK_THERMAL,
            MobileEventTypes.CHECK_MEMORY,
            MobileEventTypes.CHECK_STORAGE,
            MobileEventTypes.DIAGNOSTICS_REPORT,
        ):
            if self.context.diagnostics:
                return self.context.diagnostics.handle_event(event)
            return self._not_available("diagnostics")

        # --------------------------------------------------------
        # ENERGY GOVERNOR
        # --------------------------------------------------------
        if et in (
            MobileEventTypes.GOVERNOR_POLICY_UPDATE,
            MobileEventTypes.GOVERNOR_BLOCK,
        ):
            if self.context.energy_governor:
                return self.context.energy_governor.handle_event(event)
            return self._not_available("energy_governor")

        # --------------------------------------------------------
        # WORKFLOW ENGINE 2.0 / 3.0
        # --------------------------------------------------------
        if et in (
            MobileEventTypes.WORKFLOW_START,
            MobileEventTypes.WORKFLOW_STEP,
            MobileEventTypes.WORKFLOW_COMPLETE,
            MobileEventTypes.WORKFLOW_ABORT,
        ):
            if self.context.workflow:
                return self.context.workflow.handle_event(event)
            return self._not_available("workflow")

        # --------------------------------------------------------
        # LAN OFFLINE BRIDGE
        # --------------------------------------------------------
        if et in (
            MobileEventTypes.LAN_MESSAGE,
            MobileEventTypes.LAN_SYNC,
            MobileEventTypes.LAN_STATUS,
        ):
            if self.context.lan_bridge:
                return self.context.lan_bridge.handle_event(event)
            return self._not_available("lan_bridge")

        # --------------------------------------------------------
        # APP CONTROL
        # --------------------------------------------------------
        if et == MobileEventTypes.OPEN_APP:
            return {
                "status": "ok",
                "action": "open_app",
            }

        # --------------------------------------------------------
        # HELP
        # --------------------------------------------------------
        if et == MobileEventTypes.SHOW_HELP:
            return {
                "status": "ok",
                "help": "Available commands: lookup, open, battery, wifi, read, analyze, diagnostics, governor, workflow"
            }

        # --------------------------------------------------------
        # UNKNOWN EVENT
        # --------------------------------------------------------
        return {
            "status": "error",
            "reason": "unknown_event",
            "event_type": et,
        }

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _not_available(self, module_name: str):
        """Fallback when a module is not attached to runtime."""
        return {
            "status": "not_available",
            "module": module_name,
            "message": f"Module '{module_name}' is not attached to runtime."
        }

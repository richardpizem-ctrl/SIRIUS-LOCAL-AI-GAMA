# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Dispatcher
# Version: 3.0.0-pre
# ============================================================

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileRuntimeDispatcher:

    DISPATCHER_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

    def dispatch(self, event: MobileEvent):

        et = event.type

        # SECURITY MODULE
        if et in (
            MobileEventTypes.SECURITY,
            MobileEventTypes.RESTRICTED_MODE,
            MobileEventTypes.PERMISSION_CHECK,
        ):
            if hasattr(self.context.security, "handle_event"):
                return self.context.security.handle_event(event)
            if hasattr(self.context.security, "evaluate"):
                return self.context.security.evaluate(event)
            return self._not_available("security")

        # VISION MODULE
        if et in (
            MobileEventTypes.OCR,
            MobileEventTypes.DETECT,
            MobileEventTypes.SCENE,
            MobileEventTypes.HOMEWORK,
        ):
            if hasattr(self.context.vision, "handle_event"):
                return self.context.vision.handle_event(event)
            if hasattr(self.context.vision, "process"):
                return self.context.vision.process(event)
            return self._not_available("vision")

        # KNOWLEDGE PACKS MODULE
        if et in (
            MobileEventTypes.PACK_LOOKUP,
            MobileEventTypes.PACK_INFO,
            MobileEventTypes.PACK_QUERY,
        ):
            if hasattr(self.context.packs, "handle_event"):
                return self.context.packs.handle_event(event)
            if hasattr(self.context.packs, "query"):
                return self.context.packs.query(event.payload.get("text", ""))
            return self._not_available("packs")

        # DEVICE DIAGNOSTICS
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

        # ENERGY GOVERNOR
        if et in (
            MobileEventTypes.GOVERNOR_POLICY_UPDATE,
            MobileEventTypes.GOVERNOR_BLOCK,
        ):
            if self.context.energy_governor:
                return self.context.energy_governor.handle_event(event)
            return self._not_available("energy_governor")

        # WORKFLOW ENGINE
        if et in (
            MobileEventTypes.WORKFLOW_START,
            MobileEventTypes.WORKFLOW_STEP,
            MobileEventTypes.WORKFLOW_COMPLETE,
            MobileEventTypes.WORKFLOW_ABORT,
        ):
            if self.context.workflow:
                return self.context.workflow.handle_event(event)
            return self._not_available("workflow")

        # LAN OFFLINE BRIDGE
        if et in (
            MobileEventTypes.LAN_MESSAGE,
            MobileEventTypes.LAN_SYNC,
            MobileEventTypes.LAN_STATUS,
        ):
            if self.context.lan_bridge:
                return self.context.lan_bridge.handle_event(event)
            return self._not_available("lan_bridge")

        # APP CONTROL
        if et == MobileEventTypes.OPEN_APP:
            return {"status": "ok", "action": "open_app"}

        # HELP
        if et == MobileEventTypes.SHOW_HELP:
            return {
                "status": "ok",
                "help": "Available commands: lookup, open, battery, wifi, read, analyze, diagnostics, governor, workflow"
            }

        # UNKNOWN EVENT
        return {
            "status": "error",
            "reason": "unknown_event",
            "event_type": et,
        }

    def _not_available(self, module_name: str):
        return {
            "status": "not_available",
            "module": module_name,
            "message": f"Module '{module_name}' is not attached to runtime."
        }

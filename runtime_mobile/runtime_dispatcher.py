# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Dispatcher
# Version: 3.0.0-pre
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes


class MobileRuntimeDispatcher:
    """
    Dispatches MobileEvent objects to the correct runtime module.
    Acts as a bridge between the NL Router and runtime modules.
    """

    DISPATCHER_VERSION = "3.0.0-pre"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main Dispatch Method
    # ------------------------------------------------------------

    def dispatch(self, event):
        """Dispatch event to the correct module based on event type."""

        etype = event.type
        self.context.update_last_event(event)

        # --------------------------------------------------------
        # VISION MODULE
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.OCR,
            MobileEventTypes.DETECT,
            MobileEventTypes.SCENE,
            MobileEventTypes.ANALYZE,
            MobileEventTypes.HOMEWORK,
        ]:
            result = self.context.vision_engine.on_event(event)
            result["module"] = "vision"
            return result

        # --------------------------------------------------------
        # KNOWLEDGE PACKS
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.PACK_LOOKUP,
            MobileEventTypes.PACK_INFO,
            MobileEventTypes.PACK_QUERY,
        ]:
            result = self.context.knowledge_packs.on_event(event)
            result["module"] = "knowledge_packs"
            return result

        # --------------------------------------------------------
        # TEXT QUERY / ASSISTANT
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.TEXT_QUERY,
            MobileEventTypes.ASSISTANT,
        ]:
            if hasattr(self.context, "assistant"):
                result = self.context.assistant.on_event(event)
                result["module"] = "assistant"
                return result

        # --------------------------------------------------------
        # SECURITY
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.SECURITY,
            MobileEventTypes.PERMISSION_CHECK,
            MobileEventTypes.RESTRICTED_MODE,
        ]:
            result = self.context.security.on_event(event)
            result["module"] = "security"
            return result

        # --------------------------------------------------------
        # DIAGNOSTICS
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.CHECK_BATTERY,
            MobileEventTypes.CHECK_THERMAL,
            MobileEventTypes.CHECK_MEMORY,
            MobileEventTypes.CHECK_STORAGE,
            MobileEventTypes.DIAGNOSTICS_REPORT,
        ]:
            if self.context.diagnostics:
                result = self.context.diagnostics.on_event(event)
                result["module"] = "diagnostics"
                return result

        # --------------------------------------------------------
        # ENERGY GOVERNOR
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.GOVERNOR_POLICY_UPDATE,
            MobileEventTypes.GOVERNOR_BLOCK,
        ]:
            if self.context.energy_governor:
                result = self.context.energy_governor.on_event(event)
                result["module"] = "energy_governor"
                return result

        # --------------------------------------------------------
        # WORKFLOW ENGINE
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.WORKFLOW_START,
            MobileEventTypes.WORKFLOW_STEP,
            MobileEventTypes.WORKFLOW_COMPLETE,
            MobileEventTypes.WORKFLOW_ABORT,
        ]:
            if self.context.workflow:
                result = self.context.workflow.on_event(event)
                result["module"] = "workflow"
                return result

        # --------------------------------------------------------
        # LAN OFFLINE BRIDGE
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.LAN_MESSAGE,
            MobileEventTypes.LAN_SYNC,
            MobileEventTypes.LAN_STATUS,
        ]:
            if self.context.lan_bridge:
                result = self.context.lan_bridge.on_event(event)
                result["module"] = "lan_bridge"
                return result

        # --------------------------------------------------------
        # HELP
        # --------------------------------------------------------
        if etype == MobileEventTypes.SHOW_HELP:
            return {
                "status": "ok",
                "module": "system",
                "help": "Available commands: scan, detect, scene, homework, lookup, query, assistant, security, diagnostics, workflow, lan, help"
            }

        # --------------------------------------------------------
        # UNKNOWN EVENT
        # --------------------------------------------------------
        return {
            "status": "error",
            "reason": "unknown_event",
            "event_type": etype,
            "module": "none"
        }

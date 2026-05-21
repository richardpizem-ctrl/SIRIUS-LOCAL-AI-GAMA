# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile Runtime Dispatcher
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
# ============================================================

from runtime_mobile.core.event_types import MobileEventTypes


class MobileRuntimeDispatcher:
    """
    Dispatches MobileEvent objects to the correct runtime module.
    Acts as a bridge between the NL Router and runtime modules.
    """

    DISPATCHER_VERSION = "3.1.0"

    def __init__(self, context):
        self.context = context

    # ------------------------------------------------------------
    # Main Dispatch Method
    # ------------------------------------------------------------

    def dispatch(self, event):
        """Dispatch event to the correct module based on event type."""

        etype = getattr(event, "type", None)
        if etype is None:
            return {
                "status": "error",
                "reason": "missing_event_type",
                "module": "none",
            }

        # Context already updated in RuntimeCore, but keep it safe here too
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
            MobileEventTypes.VISION,
            MobileEventTypes.VISION_CAPABILITIES,
        ]:
            if not self.context.vision_engine:
                return {
                    "status": "error",
                    "reason": "vision_engine_missing",
                    "module": "vision",
                }
            result = self.context.vision_engine.on_event(event) or {}
            result["module"] = "vision"
            return result

        # --------------------------------------------------------
        # KNOWLEDGE PACKS
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.PACK_LOOKUP,
            MobileEventTypes.PACK_INFO,
            MobileEventTypes.PACK_QUERY,
            MobileEventTypes.PACK_SUGGEST,
        ]:
            if not self.context.knowledge_packs:
                return {
                    "status": "error",
                    "reason": "knowledge_packs_missing",
                    "module": "knowledge_packs",
                }
            result = self.context.knowledge_packs.on_event(event) or {}
            result["module"] = "knowledge_packs"
            return result

        # --------------------------------------------------------
        # TEXT QUERY / ASSISTANT
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.TEXT_QUERY,
            MobileEventTypes.ASSISTANT,
            MobileEventTypes.ASSISTANT_CONTEXT,
        ]:
            if getattr(self.context, "assistant", None):
                result = self.context.assistant.on_event(event) or {}
                result["module"] = "assistant"
                return result
            return {
                "status": "error",
                "reason": "assistant_missing",
                "module": "assistant",
            }

        # --------------------------------------------------------
        # SECURITY
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.SECURITY,
            MobileEventTypes.PERMISSION_CHECK,
            MobileEventTypes.RESTRICTED_MODE,
            MobileEventTypes.SECURITY_ALERT,
        ]:
            if not self.context.security:
                return {
                    "status": "error",
                    "reason": "security_module_missing",
                    "module": "security",
                }
            result = self.context.security.on_event(event) or {}
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
            MobileEventTypes.DEVICE_INFO,
        ]:
            if self.context.diagnostics:
                result = self.context.diagnostics.on_event(event) or {}
                result["module"] = "diagnostics"
                return result
            return {
                "status": "error",
                "reason": "diagnostics_missing",
                "module": "diagnostics",
            }

        # --------------------------------------------------------
        # ENERGY GOVERNOR
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.GOVERNOR_POLICY_UPDATE,
            MobileEventTypes.GOVERNOR_BLOCK,
            MobileEventTypes.GOVERNOR_STATE,
        ]:
            if self.context.energy_governor:
                result = self.context.energy_governor.on_event(event) or {}
                result["module"] = "energy_governor"
                return result
            return {
                "status": "error",
                "reason": "energy_governor_missing",
                "module": "energy_governor",
            }

        # --------------------------------------------------------
        # WORKFLOW ENGINE
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.WORKFLOW_START,
            MobileEventTypes.WORKFLOW_STEP,
            MobileEventTypes.WORKFLOW_COMPLETE,
            MobileEventTypes.WORKFLOW_ABORT,
            MobileEventTypes.WORKFLOW_ERROR,
        ]:
            if self.context.workflow:
                result = self.context.workflow.on_event(event) or {}
                result["module"] = "workflow"
                return result
            return {
                "status": "error",
                "reason": "workflow_missing",
                "module": "workflow",
            }

        # --------------------------------------------------------
        # LAN OFFLINE BRIDGE
        # --------------------------------------------------------
        if etype in [
            MobileEventTypes.LAN_MESSAGE,
            MobileEventTypes.LAN_SYNC,
            MobileEventTypes.LAN_STATUS,
            MobileEventTypes.LAN_DISCOVERY,
        ]:
            if self.context.lan_bridge:
                result = self.context.lan_bridge.on_event(event) or {}
                result["module"] = "lan_bridge"
                return result
            return {
                "status": "error",
                "reason": "lan_bridge_missing",
                "module": "lan_bridge",
            }

        # --------------------------------------------------------
        # SYSTEM / RUNTIME
        # --------------------------------------------------------
        if etype == MobileEventTypes.RUNTIME_INFO:
            return {
                "status": "ok",
                "module": "system",
                "runtime": self.context.get_info(),
            }

        if etype in [MobileEventTypes.OPEN_APP, MobileEventTypes.HEARTBEAT]:
            return {
                "status": "ok",
                "module": "system",
                "event_type": etype,
            }

        if etype == MobileEventTypes.APP_STATE:
            # purely informational; state is usually updated elsewhere
            return {
                "status": "ok",
                "module": "system",
                "app_state": self.context.state.get("app_state"),
            }

        # --------------------------------------------------------
        # HELP
        # --------------------------------------------------------
        if etype == MobileEventTypes.SHOW_HELP:
            return {
                "status": "ok",
                "module": "system",
                "help": (
                    "Available commands: scan, detect, scene, homework, "
                    "lookup, query, suggest, assistant, security, diagnostics, "
                    "workflow, lan, runtime info, help"
                ),
            }

        # --------------------------------------------------------
        # UNKNOWN EVENT
        # --------------------------------------------------------
        return {
            "status": "error",
            "reason": "unknown_event",
            "event_type": etype,
            "module": "none",
        }

# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile NL Router
# Version: 3.0.0-pre
# ============================================================

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileNLRouter:

    ROUTER_VERSION = "3.0.0-pre"

    def route(self, text: str) -> MobileEvent:

        if not text or not isinstance(text, str):
            return MobileEvent(MobileEventTypes.UNKNOWN)

        t = text.strip().lower()

        # APP CONTROL
        if "open" in t:
            return MobileEvent(MobileEventTypes.OPEN_APP)

        if "help" in t:
            return MobileEvent(MobileEventTypes.SHOW_HELP)

        # DIAGNOSTICS
        if "battery" in t:
            return MobileEvent(MobileEventTypes.CHECK_BATTERY)

        if "temperature" in t or "thermal" in t:
            return MobileEvent(MobileEventTypes.CHECK_THERMAL)

        if "memory" in t or "ram" in t:
            return MobileEvent(MobileEventTypes.CHECK_MEMORY)

        if "storage" in t or "disk" in t:
            return MobileEvent(MobileEventTypes.CHECK_STORAGE)

        # ENERGY GOVERNOR
        if "eco mode" in t or "low power" in t:
            return MobileEvent(MobileEventTypes.GOVERNOR_POLICY_UPDATE, policy="eco")

        if "balanced mode" in t:
            return MobileEvent(MobileEventTypes.GOVERNOR_POLICY_UPDATE, policy="balanced")

        if "turbo mode" in t:
            return MobileEvent(MobileEventTypes.GOVERNOR_POLICY_UPDATE, policy="turbo")

        # SECURITY
        if "permission" in t or "allow" in t or "deny" in t:
            return MobileEvent(MobileEventTypes.SECURITY, permission="generic")

        if "restricted" in t:
            enabled = "on" in t or "enable" in t
            return MobileEvent(MobileEventTypes.RESTRICTED_MODE, enabled=enabled)

        # VISION
        if "ocr" in t or "read" in t or "text from image" in t:
            return MobileEvent(MobileEventTypes.OCR, mode="ocr", image=None)

        if "detect" in t or "objects" in t:
            return MobileEvent(MobileEventTypes.DETECT, mode="detect", image=None)

        if "scene" in t or "what is in the picture" in t:
            return MobileEvent(MobileEventTypes.SCENE, mode="scene", image=None)

        if "homework" in t or "solve" in t:
            return MobileEvent(MobileEventTypes.HOMEWORK, mode="homework", image=None)

        # KNOWLEDGE PACKS
        if "lookup" in t or "search" in t:
            parts = t.split()
            pack_name = parts[1] if len(parts) >= 3 else "default"
            key = parts[2] if len(parts) >= 3 else "query"
            return MobileEvent(MobileEventTypes.PACK_LOOKUP, pack=pack_name, key=key)

        # WORKFLOW
        if "start workflow" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_START)

        if "next step" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_STEP)

        if "finish workflow" in t or "complete workflow" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_COMPLETE)

        if "abort workflow" in t or "cancel workflow" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_ABORT)

        # LAN
        if "lan sync" in t or "offline sync" in t or "local sync" in t:
            return MobileEvent(MobileEventTypes.LAN_SYNC)

        # DEFAULT
        return MobileEvent(MobileEventTypes.UNKNOWN)

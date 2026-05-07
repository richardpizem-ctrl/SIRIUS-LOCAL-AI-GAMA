# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile NL Router
# Version: 3.0.0-pre
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Natural Language router for the GAMA mobile runtime.
# Converts user text commands into MobileEvent objects.
#
# GAMA 3-ready features:
#   - extended event types (diagnostics, governor, workflow, scene)
#   - normalized text parsing
#   - multi-word command detection
#   - structured payloads
#   - safe fallback routing
# ============================================================

from runtime_mobile.core.event_types import MobileEvent, MobileEventTypes


class MobileNLRouter:
    """
    Natural Language router for the GAMA mobile runtime.
    Converts user text commands into MobileEvent objects.
    """

    ROUTER_VERSION = "3.0.0-pre"

    # ------------------------------------------------------------
    # Main Routing Entry
    # ------------------------------------------------------------

    def route(self, text: str) -> MobileEvent:
        """
        Input:
            text (str): User text command.

        Output:
            MobileEvent: Parsed event with type + payload.
        """

        if not text or not isinstance(text, str):
            return MobileEvent(MobileEventTypes.UNKNOWN)

        t = text.strip().lower()

        # --------------------------------------------------------
        # APP CONTROL
        # --------------------------------------------------------
        if "open" in t:
            return MobileEvent(MobileEventTypes.OPEN_APP)

        if "help" in t:
            return MobileEvent(MobileEventTypes.SHOW_HELP)

        # --------------------------------------------------------
        # DEVICE DIAGNOSTICS (GAMA 2.0 → 3.0)
        # --------------------------------------------------------
        if "battery" in t:
            return MobileEvent(MobileEventTypes.CHECK_BATTERY)

        if "temperature" in t or "thermal" in t:
            return MobileEvent(MobileEventTypes.CHECK_THERMAL)

        if "memory" in t or "ram" in t:
            return MobileEvent(MobileEventTypes.CHECK_MEMORY)

        if "storage" in t or "disk" in t:
            return MobileEvent(MobileEventTypes.CHECK_STORAGE)

        # --------------------------------------------------------
        # ENERGY GOVERNOR
        # --------------------------------------------------------
        if "eco mode" in t or "low power" in t:
            return MobileEvent(
                MobileEventTypes.GOVERNOR_POLICY_UPDATE,
                {"policy": "eco"}
            )

        if "balanced mode" in t:
            return MobileEvent(
                MobileEventTypes.GOVERNOR_POLICY_UPDATE,
                {"policy": "balanced"}
            )

        if "turbo mode" in t:
            return MobileEvent(
                MobileEventTypes.GOVERNOR_POLICY_UPDATE,
                {"policy": "turbo"}
            )

        # --------------------------------------------------------
        # SECURITY
        # --------------------------------------------------------
        if "permission" in t or "allow" in t or "deny" in t:
            return MobileEvent(
                MobileEventTypes.SECURITY,
                {"permission": "generic"}
            )

        if "restricted" in t:
            enabled = "on" in t or "enable" in t
            return MobileEvent(
                MobileEventTypes.RESTRICTED_MODE,
                {"enabled": enabled}
            )

        # --------------------------------------------------------
        # VISION
        # --------------------------------------------------------
        if "ocr" in t or "read" in t or "text from image" in t:
            return MobileEvent(
                MobileEventTypes.OCR,
                {"mode": "ocr"}
            )

        if "detect" in t or "objects" in t:
            return MobileEvent(
                MobileEventTypes.DETECT,
                {"mode": "detect"}
            )

        if "scene" in t or "what is in the picture" in t:
            return MobileEvent(
                MobileEventTypes.SCENE,
                {"mode": "scene"}
            )

        if "homework" in t or "solve" in t:
            return MobileEvent(
                MobileEventTypes.HOMEWORK,
                {"mode": "homework"}
            )

        # --------------------------------------------------------
        # KNOWLEDGE PACKS
        # Format: "lookup <pack> <key>"
        # --------------------------------------------------------
        if "lookup" in t or "search" in t:
            parts = t.split()

            pack_name = None
            key = None

            if len(parts) >= 3:
                pack_name = parts[1]
                key = parts[2]

            return MobileEvent(
                MobileEventTypes.PACK_LOOKUP,
                {
                    "pack": pack_name if pack_name else "default",
                    "key": key if key else "query"
                }
            )

        # --------------------------------------------------------
        # WORKFLOW ENGINE 2.0 / 3.0
        # --------------------------------------------------------
        if "start workflow" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_START)

        if "next step" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_STEP)

        if "finish workflow" in t or "complete workflow" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_COMPLETE)

        if "abort workflow" in t or "cancel workflow" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_ABORT)

        # --------------------------------------------------------
        # LAN OFFLINE BRIDGE
        # --------------------------------------------------------
        if "sync" in t or "lan" in t:
            return MobileEvent(MobileEventTypes.LAN_SYNC)

        # --------------------------------------------------------
        # DEFAULT FALLBACK
        # --------------------------------------------------------
        return MobileEvent(MobileEventTypes.UNKNOWN)

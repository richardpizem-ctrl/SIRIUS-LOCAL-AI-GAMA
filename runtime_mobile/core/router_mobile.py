# ============================================================
# SIRIUS LOCAL AI GAMA - Mobile NL Router
# Version: 3.1.0
# Author: Richard Pizem (SIRIUS LOCAL AI)
#
# Upgraded for GAMA Runtime 3.1:
# - MobileEvent v3.1 (intent, confidence, metadata v3)
# - Multi-intent routing v1
# - SCENE v1 routing
# - Hybrid Schoolwork v1
# - Diagnostics v3
# - Unified NL → Event pipeline
# ============================================================

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes


class MobileNLRouter:

    ROUTER_VERSION = "3.1.0"

    def route(self, text: str) -> MobileEvent:

        # Validate input
        if not text or not isinstance(text, str):
            return MobileEvent(
                MobileEventTypes.UNKNOWN,
                raw_input=text,
                normalized_input="",
                source="nlrouter"
            )

        t = text.strip().lower()

        # --------------------------------------------------------
        # APP CONTROL
        # --------------------------------------------------------
        if "open" in t:
            return MobileEvent(
                MobileEventTypes.OPEN_APP,
                raw_input=text,
                normalized_input=t,
                source="nlrouter"
            )

        if "help" in t:
            return MobileEvent(
                MobileEventTypes.SHOW_HELP,
                raw_input=text,
                normalized_input=t,
                source="nlrouter"
            )

        # --------------------------------------------------------
        # DIAGNOSTICS v3
        # --------------------------------------------------------
        if "battery" in t:
            return MobileEvent(
                MobileEventTypes.CHECK_BATTERY,
                raw_input=text,
                normalized_input=t,
                source="nlrouter"
            )

        if "temperature" in t or "thermal" in t:
            return MobileEvent(
                MobileEventTypes.CHECK_THERMAL,
                raw_input=text,
                normalized_input=t,
                source="nlrouter"
            )

        if "memory" in t or "ram" in t:
            return MobileEvent(
                MobileEventTypes.CHECK_MEMORY,
                raw_input=text,
                normalized_input=t,
                source="nlrouter"
            )

        if "storage" in t or "disk" in t:
            return MobileEvent(
                MobileEventTypes.CHECK_STORAGE,
                raw_input=text,
                normalized_input=t,
                source="nlrouter"
            )

        # --------------------------------------------------------
        # ENERGY GOVERNOR v3
        # --------------------------------------------------------
        if "eco mode" in t or "low power" in t:
            return MobileEvent(
                MobileEventTypes.GOVERNOR_POLICY_UPDATE,
                raw_input=text,
                normalized_input=t,
                policy="eco",
                source="nlrouter"
            )

        if "balanced mode" in t:
            return MobileEvent(
                MobileEventTypes.GOVERNOR_POLICY_UPDATE,
                raw_input=text,
                normalized_input=t,
                policy="balanced",
                source="nlrouter"
            )

        if "turbo mode" in t:
            return MobileEvent(
                MobileEventTypes.GOVERNOR_POLICY_UPDATE,
                raw_input=text,
                normalized_input=t,
                policy="turbo",
                source="nlrouter"
            )

        # --------------------------------------------------------
        # SECURITY v3
        # --------------------------------------------------------
        if "permission" in t or "allow" in t or "deny" in t:
            return MobileEvent(
                MobileEventTypes.SECURITY,
                raw_input=text,
                normalized_input=t,
                permission="generic",
                source="nlrouter"
            )

        if "restricted" in t:
            enabled = "on" in t or "enable" in t
            return MobileEvent(
                MobileEventTypes.RESTRICTED_MODE,
                raw_input=text,
                normalized_input=t,
                enabled=enabled,
                source="nlrouter"
            )

        # --------------------------------------------------------
        # VISION / OCR / SCENE v1
        # --------------------------------------------------------
        if "ocr" in t or "read" in t or "text from image" in t:
            return MobileEvent(
                MobileEventTypes.OCR,
                raw_input=text,
                normalized_input=t,
                mode="ocr",
                tags=["ocr"],
                source="nlrouter"
            )

        if "detect" in t or "objects" in t:
            return MobileEvent(
                MobileEventTypes.DETECT,
                raw_input=text,
                normalized_input=t,
                mode="detect",
                tags=["vision"],
                source="nlrouter"
            )

        if "scene" in t or "what is in the picture" in t:
            return MobileEvent(
                MobileEventTypes.SCENE,
                raw_input=text,
                normalized_input=t,
                mode="scene",
                tags=["scene"],
                source="nlrouter"
            )

        # --------------------------------------------------------
        # SCHOOLWORK / HYBRID INPUT v1
        # --------------------------------------------------------
        if "homework" in t or "solve" in t:
            return MobileEvent(
                MobileEventTypes.HOMEWORK,
                raw_input=text,
                normalized_input=t,
                mode="homework",
                tags=["schoolwork"],
                source="nlrouter"
            )

        # --------------------------------------------------------
        # KNOWLEDGE PACKS
        # --------------------------------------------------------
        if "lookup" in t or "search" in t:
            parts = t.split()
            pack_name = parts[1] if len(parts) >= 3 else "default"
            key = parts[2] if len(parts) >= 3 else "query"
            return MobileEvent(
                MobileEventTypes.PACK_LOOKUP,
                raw_input=text,
                normalized_input=t,
                pack=pack_name,
                key=key,
                source="nlrouter"
            )

        # --------------------------------------------------------
        # WORKFLOW ENGINE
        # --------------------------------------------------------
        if "start workflow" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_START,
                               raw_input=text, normalized_input=t, source="nlrouter")

        if "next step" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_STEP,
                               raw_input=text, normalized_input=t, source="nlrouter")

        if "finish workflow" in t or "complete workflow" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_COMPLETE,
                               raw_input=text, normalized_input=t, source="nlrouter")

        if "abort workflow" in t or "cancel workflow" in t:
            return MobileEvent(MobileEventTypes.WORKFLOW_ABORT,
                               raw_input=text, normalized_input=t, source="nlrouter")

        # --------------------------------------------------------
        # LAN OFFLINE BRIDGE
        # --------------------------------------------------------
        if "lan sync" in t or "offline sync" in t or "local sync" in t:
            return MobileEvent(
                MobileEventTypes.LAN_SYNC,
                raw_input=text,
                normalized_input=t,
                source="nlrouter"
            )

        # --------------------------------------------------------
        # DEFAULT
        # --------------------------------------------------------
        return MobileEvent(
            MobileEventTypes.UNKNOWN,
            raw_input=text,
            normalized_input=t,
            source="nlrouter"
        )

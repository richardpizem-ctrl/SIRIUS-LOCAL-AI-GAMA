"""
SIRIUS LOCAL AI GAMA – Event Diagnostics v3
Mobile Runtime 3.2.0

This module provides:
- event hit counters
- pack usage tracking
- vision/routing diagnostics
- legacy event conversion logs
- security alert tracking
- preparation for Diagnostics Engine 4.0
"""

DIAGNOSTICS_VERSION = "3.2.0"


# ---------------------------------------------------------
# Internal counters
# ---------------------------------------------------------

event_hits = {}
pack_usage = {}
vision_usage = {}
routing_decisions = []
security_alerts = 0
legacy_event_conversions = 0


# ---------------------------------------------------------
# Event hit tracking
# ---------------------------------------------------------

def track_event(event_name: str):
    """
    Count how many times each event is triggered.
    """
    global event_hits
    event_hits[event_name] = event_hits.get(event_name, 0) + 1


# ---------------------------------------------------------
# Pack usage tracking
# ---------------------------------------------------------

def track_pack_usage(pack_name: str):
    """
    Count how many times each knowledge pack is used.
    """
    global pack_usage
    pack_usage[pack_name] = pack_usage.get(pack_name, 0) + 1


# ---------------------------------------------------------
# Vision usage tracking
# ---------------------------------------------------------

def track_vision(event_name: str):
    """
    Track usage of vision-related events.
    """
    global vision_usage
    vision_usage[event_name] = vision_usage.get(event_name, 0) + 1


# ---------------------------------------------------------
# Routing diagnostics
# ---------------------------------------------------------

def log_routing(input_text: str, vision_payload: dict, result_event: str):
    """
    Log routing decisions for debugging and analytics.
    """
    routing_decisions.append({
        "text": input_text,
        "vision": vision_payload,
        "result": result_event
    })


# ---------------------------------------------------------
# Legacy event conversion tracking
# ---------------------------------------------------------

def track_legacy_conversion():
    """
    Count how many legacy events were converted.
    """
    global legacy_event_conversions
    legacy_event_conversions += 1


# ---------------------------------------------------------
# Security alert tracking
# ---------------------------------------------------------

def track_security_alert():
    """
    Count SECURITY_ALERT events.
    """
    global security_alerts
    security_alerts += 1


# ---------------------------------------------------------
# Diagnostics snapshot
# ---------------------------------------------------------

def get_diagnostics() -> dict:
    """
    Return a full diagnostics snapshot.
    """
    return {
        "version": DIAGNOSTICS_VERSION,
        "event_hits": event_hits,
        "pack_usage": pack_usage,
        "vision_usage": vision_usage,
        "routing_decisions": routing_decisions[-20:],  # last 20 entries
        "security_alerts": security_alerts,
        "legacy_event_conversions": legacy_event_conversions,
    }


# ---------------------------------------------------------
# Reset diagnostics (for testing)
# ---------------------------------------------------------

def reset_diagnostics():
    """
    Reset all diagnostics counters.
    """
    global event_hits, pack_usage, vision_usage
    global routing_decisions, security_alerts, legacy_event_conversions

    event_hits = {}
    pack_usage = {}
    vision_usage = {}
    routing_decisions = []
    security_alerts = 0
    legacy_event_conversions = 0

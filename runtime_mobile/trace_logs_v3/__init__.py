"""
trace_logs_v3

GAMA Runtime 3.4.0 – Trace Logs v3
Deterministic, safe trace logging module for SCHOOLWORK reasoning pipeline.

Exports:
- TraceManager
- TraceWriter
- build_trace_record_v3
"""

from .trace_manager import TraceManager
from .trace_writer import TraceWriter
from .trace_schema_v3 import build_trace_record_v3

__all__ = [
    "TraceManager",
    "TraceWriter",
    "build_trace_record_v3",
]

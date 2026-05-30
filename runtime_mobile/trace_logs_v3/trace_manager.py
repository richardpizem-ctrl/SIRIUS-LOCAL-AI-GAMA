"""
trace_manager.py

GAMA Runtime 3.4.0 – Trace Logs v3
Deterministic, safe trace orchestration for SCHOOLWORK reasoning pipeline.

This module:
- generates deterministic trace IDs
- builds trace records using the v3 schema
- delegates safe writing to TraceWriter
- never stores raw content (only meta-data)
"""

from typing import Dict, Optional

from .trace_schema_v3 import build_trace_record_v3
from .trace_writer import TraceWriter


class TraceManager:
    """
    Orchestrates creation and persistence of trace logs for the SCHOOLWORK reasoning pipeline.

    Design rules:
    - No randomness (deterministic trace IDs).
    - No raw OCR/text content – only semantic/meta fields.
    - Stable schema via build_trace_record_v3().
    - Safe for schools and families.
    """

    _counter: int = 0  # class-level deterministic counter

    def __init__(self, writer: Optional[TraceWriter] = None) -> None:
        self._writer: TraceWriter = writer or TraceWriter()

    @classmethod
    def _next_trace_id(cls) -> str:
        """
        Returns a deterministic, monotonic trace ID.

        Example: TRC3-00000001, TRC3-00000002, ...
        """
        cls._counter += 1
        return f"TRC3-{cls._counter:08d}"

    def create_trace(
        self,
        *,
        module: str,
        normalized_input_meta: Optional[Dict] = None,
        subject_meta: Optional[Dict] = None,
        pack_meta: Optional[Dict] = None,
        reasoning_steps_meta: Optional[Dict] = None,
        fallback_meta: Optional[Dict] = None,
        context_meta: Optional[Dict] = None,
    ) -> str:
        """
        Creates a new trace record and writes it using TraceWriter.

        All *_meta arguments must contain only:
        - semantic flags
        - categories
        - IDs
        - non-sensitive technical metadata

        No raw user content, no OCR text, no screenshots.
        """

        trace_id = self._next_trace_id()

        record = build_trace_record_v3(
            trace_id=trace_id,
            module=module,
            normalized_input_meta=normalized_input_meta or {},
            subject_meta=subject_meta or {},
            pack_meta=pack_meta or {},
            reasoning_steps_meta=reasoning_steps_meta or {},
            fallback_meta=fallback_meta or {},
            context_meta=context_meta or {},
        )

        self._writer.write(record)
        return trace_id

    def trace_reasoning_pipeline(
        self,
        *,
        module: str,
        normalized_input_meta: Dict,
        subject_meta: Dict,
        pack_meta: Dict,
        reasoning_steps_meta: Dict,
        fallback_meta: Dict,
        context_meta: Dict,
    ) -> str:
        """
        Convenience wrapper for the standard SCHOOLWORK reasoning pipeline.

        Intended call site:
        - after reasoning is complete
        - when all meta blocks are available
        """

        return self.create_trace(
            module=module,
            normalized_input_meta=normalized_input_meta,
            subject_meta=subject_meta,
            pack_meta=pack_meta,
            reasoning_steps_meta=reasoning_steps_meta,
            fallback_meta=fallback_meta,
            context_meta=context_meta,
        )

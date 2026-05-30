"""
trace_writer.py

GAMA Runtime 3.4.0 – Trace Logs v3
Safe, deterministic writer for SCHOOLWORK reasoning trace records.

Rules:
- Never store raw OCR/text content.
- Never store sensitive user data.
- Only semantic meta-data is allowed.
- Deterministic field ordering.
- Fully offline, safe for families and schools.
"""

import json
import os
from typing import Dict, Any


class TraceWriter:
    """
    Writes trace records to a safe, deterministic JSONL file.

    Output format:
    - One JSON object per line (JSONL)
    - Deterministic key ordering
    - No raw content, only meta-data
    """

    def __init__(self, output_dir: str = "runtime_mobile/trace_logs_v3/output") -> None:
        self.output_dir = output_dir
        self.output_file = os.path.join(self.output_dir, "trace_logs_v3.jsonl")

        # Ensure directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def _sanitize(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ensures the record contains ONLY safe meta-data.

        This function:
        - removes any unexpected fields
        - enforces deterministic ordering
        - guarantees no raw content is present
        """

        allowed_top_fields = {
            "version",
            "timestamp",
            "trace_id",
            "module",
            "normalized_input_meta",
            "subject_meta",
            "pack_meta",
            "reasoning_steps_meta",
            "fallback_meta",
            "context_meta",
        }

        sanitized = {}

        for key in sorted(record.keys()):
            if key in allowed_top_fields:
                sanitized[key] = record[key]

        return sanitized

    def write(self, record: Dict[str, Any]) -> None:
        """
        Writes a sanitized trace record to the JSONL file.
        """

        safe_record = self._sanitize(record)

        with open(self.output_file, "a", encoding="utf-8") as f:
            json.dump(
                safe_record,
                f,
                ensure_ascii=False,
                sort_keys=True,  # deterministic ordering
            )
            f.write("\n")

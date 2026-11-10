"""
restricted_filters.py
---------------------
Filtering layer for Restricted Mode v3.

Responsibilities:
- Sanitize payload data
- Remove forbidden keywords
- Block unsafe or disallowed content
- Provide deterministic filtering behavior
- Support SchoolMode v2 and Family Security 3.x

This module is fully deterministic:
- No dynamic imports
- No reflection
- No eval/exec
Prepared for Self‑Repair Layer 4.4.
"""


class RestrictedFilters:
    """
    Deterministic payload filtering engine.
    """

    # Forbidden keywords (soft block)
    FORBIDDEN_KEYWORDS = [
        "hack",
        "bypass",
        "exploit",
        "cheat",
        "script",
        "eval(",
        "exec(",
        "<script",
    ]

    # -------------------------------------------------------------

    def apply_filters(self, payload: dict) -> dict | None:
        """
        Applies all filters to the payload.
        Returns sanitized payload or None if blocked.
        """

        if not isinstance(payload, dict):
            return None

        sanitized = {}

        for key, value in payload.items():
            if isinstance(value, str):
                cleaned = self._sanitize_text(value)
                if cleaned is None:
                    return None
                sanitized[key] = cleaned

            elif isinstance(value, (int, float, bool)):
                sanitized[key] = value

            elif isinstance(value, dict):
                nested = self.apply_filters(value)
                if nested is None:
                    return None
                sanitized[key] = nested

            else:
                # Unsupported type → block
                return None

        return sanitized

    # -------------------------------------------------------------

    def _sanitize_text(self, text: str) -> str | None:
        """
        Removes forbidden keywords from text.
        If forbidden content is found → block.
        """

        lower = text.lower()

        for word in self.FORBIDDEN_KEYWORDS:
            if word in lower:
                return None

        return text

# TODO: Validate
"""Constants."""

from collections.abc import Mapping, Sequence
from pathlib import Path

TRIVIAL_MINUS_PATH = Path(__file__).parent
FILES_PATH = TRIVIAL_MINUS_PATH / "_files"

type JSON_VALUE = (
    str | int | float | bool | Mapping[str, JSON_VALUE] | Sequence[JSON_VALUE] | None
)
"""Anything that can appear in a parsed JSON document."""

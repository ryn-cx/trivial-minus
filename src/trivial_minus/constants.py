# TODO: Validate
"""Constants."""

import re
from collections.abc import Mapping, Sequence
from pathlib import Path

TRIVIAL_MINUS_PATH = Path(__file__).parent
FILES_PATH = TRIVIAL_MINUS_PATH / "_files"

type JSON_VALUE = (
    str | int | float | bool | Mapping[str, JSON_VALUE] | Sequence[JSON_VALUE] | None
)
"""Anything that can appear in a parsed JSON document."""

LD_JSON_RE = re.compile(
    r'<script type="application/ld\+json">(?P<json>.*?)</script>',
    re.DOTALL,
)
"""The schema.org blocks a page carries."""

HUB_RE = re.compile(r"var __hub\s*=\s*(?P<json>\{.*?\});")
"""Matches the hub object a collections page hands its own scripts."""

COLLECTION_CAROUSELS_RE = re.compile(
    r"collectionConfig\s*=\s*(?P<json>\[.*?\]);",
    re.DOTALL,
)
"""Matches the carousels a collections page hands its own scripts."""

COLLECTION_CATEGORIES_RE = re.compile(
    r"collectionCategories\s*=\s*(?P<json>\[.*?\]);",
    re.DOTALL,
)
"""Matches the category tabs the collections hub hands its own scripts."""

# TODO: Validate
"""Turns a downloaded show page into the object ShowModel reads."""

from __future__ import annotations

import re

SEASON_RE = re.compile(r'aria-label="Season \d+"[^>]*?\bdata-value="(?P<season>\d+)"')
"""A season in the selector, whose `data-value` is what the episodes list wants."""


# TODO: Validate
def extract_show(page: str) -> dict[str, list[int]]:
    """Return the seasons a show page lists, sorted.

    A show page is HTML rather than JSON, so the seasons are read out of the
    selector the site fills its dropdown with and handed over as an object the
    model can be built from and validated against. The list is empty when the
    page has no season selector, which is what a show with a single season looks
    like.
    """
    seasons = {int(match.group("season")) for match in SEASON_RE.finditer(page)}
    return {"seasons": sorted(seasons)}

# TODO: Validate
"""Contains the ShowHTML class."""

from __future__ import annotations

import re
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from trivial_minus.exceptions import ResourceNotFoundError, ShowNotFoundError

if TYPE_CHECKING:
    from trivial_minus import TrivialMinus

logger = getLogger(__name__)
logger.addHandler(NullHandler())

_SEASON_RE = re.compile(r'aria-label="Season \d+"[^>]*?\bdata-value="(?P<season>\d+)"')


class ShowHTML:
    """Download the raw HTML of a show page.

    Source: https://www.paramountplus.com/shows/{show_id}/

    This endpoint only fetches the page. It does not map to a JSON model, so
    callers are responsible for parsing whatever they need out of the HTML.
    """

    def __init__(self, client: TrivialMinus) -> None:
        """Initialize the endpoint with the TrivialMinus client."""
        self._client = client

    def download(self, show_id: str) -> str:
        """Download the show page and return its raw HTML.

        Args:
            show_id: The show slug, e.g. ``south-park``.

        Returns:
            The raw HTML of the show page.

        Raises:
            ShowNotFoundError: If the show does not exist.
        """
        log_id = f"{type(self).__name__} (show_id={show_id!r})"
        url = f"https://www.paramountplus.com/shows/{show_id}/"
        try:
            return self._client.download_html(
                url,
                referer="https://www.paramountplus.com/shows/",
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ShowNotFoundError(
                show_id,
                err.status_code,
                err.response,
            ) from err

    @staticmethod
    def extract_season_numbers(html: str) -> list[int]:
        """Extract the available season numbers from a show page's HTML.

        The numbers are read from the season-filter selector, where each season
        is an anchor whose ``data-value`` holds the number the episodes endpoint
        expects for that season.

        Args:
            html: The show page HTML, e.g. from :meth:`download`.

        Returns:
            The season numbers, sorted ascending with duplicates removed. Empty
            if the page contains no season selector.
        """
        return sorted(
            {int(match.group("season")) for match in _SEASON_RE.finditer(html)},
        )

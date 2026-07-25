# TODO: Validate
"""Contains the Seasons class."""

from __future__ import annotations

import re
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from trivialminus.exceptions import (
    ExtractionError,
    ResourceNotFoundError,
    ShowNotFoundError,
)

if TYPE_CHECKING:
    from trivialminus import TrivialMinus

logger = getLogger(__name__)
logger.addHandler(NullHandler())

_SEASON_RE = re.compile(r'aria-label="Season \d+"[^>]*?\bdata-value="(?P<season>\d+)"')


class Seasons:
    """Return the list of available season numbers for a show.

    Source: https://www.paramountplus.com/shows/{show_id}/

    Unlike the other endpoints this one does not map to a JSON model. The season
    numbers are not exposed by an XHR endpoint, so they are read out of the
    season-filter selector in the show page HTML and returned on their own.
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
    def parse(html: str) -> list[int]:
        """Return the season numbers found in a show page's HTML.

        Args:
            html: The show page HTML.

        Returns:
            The available season numbers, sorted ascending with duplicates removed.
        """
        return sorted(
            {int(match.group("season")) for match in _SEASON_RE.finditer(html)},
        )

    def download_and_parse(self, show_id: str) -> list[int]:
        """Download the show page and return its available season numbers.

        Args:
            show_id: The show slug, e.g. ``south-park``.

        Returns:
            The available season numbers, sorted ascending.

        Raises:
            ShowNotFoundError: If the show does not exist.
            ExtractionError: If no seasons could be found in the page HTML.
        """
        seasons = self.parse(self.download(show_id))
        if not seasons:
            msg = f"No seasons found in the page HTML for show {show_id!r}"
            raise ExtractionError(msg)
        return seasons

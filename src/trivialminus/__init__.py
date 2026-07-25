# TODO: Validate
"""Contains the TrivialMinus class."""

from __future__ import annotations

import json
import re
import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, NoReturn

from get_around import GetAround

from trivialminus.episodes import Episodes
from trivialminus.exceptions import ExtractionError, HTTPError, ResourceNotFoundError
from trivialminus.movie import Movie
from trivialminus.search import Search

if TYPE_CHECKING:
    from collections.abc import Mapping

    import httpx
    from httpx._types import QueryParamTypes

logger = getLogger(__name__)
logger.addHandler(NullHandler())

_LD_JSON_RE = re.compile(
    r'<script type="application/ld\+json">(?P<json>.*?)</script>',
    re.DOTALL,
)


def _raise_for_status(response: httpx.Response) -> NoReturn:
    """Raise the most specific error for a non-OK response."""
    if response.status_code == HTTPStatus.NOT_FOUND:
        raise ResourceNotFoundError(response.status_code, response.text)
    raise HTTPError(response.status_code, response.text)


class TrivialMinus:
    """Paramount+ API wrapper."""

    def __init__(self, get_around_client: GetAround | None = None) -> None:
        """Initialize the TrivialMinus client."""
        self.get_around_client = get_around_client or GetAround()

        self.episodes = Episodes(self)
        self.movie = Movie(self)
        self.search = Search(self)

    def _json_headers(self, referer: str) -> dict[str, str]:
        return {
            # "Host": Set by httpx
            # "User-Agent": Set by httpx
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.9",
            # "Accept-Encoding": Set by httpx
            "Referer": referer,
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }

    def _page_headers(self, referer: str) -> dict[str, str]:
        return {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": referer,
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Priority": "u=0, i",
        }

    def download_json(
        self,
        url: str,
        *,
        referer: str,
        params: QueryParamTypes | None = None,
        log_id: str,
    ) -> dict[str, Any]:
        """Download a JSON page.."""
        logger.debug("Downloading: %s", log_id)
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            params=params,
            headers=self._json_headers(referer),
            follow_redirects=True,
        )
        if response.status_code != HTTPStatus.OK:
            _raise_for_status(response)
        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.json()

    def download_ld_json(
        self,
        url: str,
        *,
        referer: str,
        schema_type: str,
        log_id: str,
    ) -> dict[str, Any]:
        """Download an HTML page and return the embedded ld+json block."""
        logger.debug("Downloading: %s", log_id)
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            headers=self._page_headers(referer),
            follow_redirects=True,
        )
        if response.status_code != HTTPStatus.OK:
            _raise_for_status(response)
        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return self._extract_ld_json(response.text, schema_type)

    @staticmethod
    def _extract_ld_json(html: str, schema_type: str) -> dict[str, Any]:
        """Return the first `ld+json` block whose `@type` matches.

        Args:
            html: The page HTML to search.
            schema_type: The schema.org `@type` to return, e.g. `Movie`.
        """
        for match in _LD_JSON_RE.finditer(html):
            block: Mapping[str, Any] = json.loads(match.group("json"))
            if block.get("@type") == schema_type:
                return dict(block)
        msg = f"No ld+json block with @type {schema_type!r} found in the page HTML"
        raise ExtractionError(msg)

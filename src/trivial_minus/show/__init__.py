# TODO: Validate
"""Contains the Show class."""

from __future__ import annotations

import json
import re
from html import unescape
from logging import NullHandler, getLogger
from typing import Any

from trivial_minus.base_api_endpoint import BaseEndpoint
from trivial_minus.constants import LD_JSON_RE
from trivial_minus.exceptions import (
    ExtractionError,
    ResourceNotFoundError,
    ShowNotFoundError,
)
from trivial_minus.show.models import ShowModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

SEASON_RE = re.compile(r'aria-label="Season \d+"[^>]*?\bdata-value="(?P<season>\d+)"')
"""Matches a season in the selector, capturing the value the episodes list wants."""

REGISTRY_SHOW_RE = re.compile(r"CBS\.Registry\.Show\s*=\s*(?P<json>\{.*?\});")
"""Matches the show object the page hands its own scripts."""

SECTION_RE = re.compile(
    r'data-sectionid="(?P<section_id>\d+)"[^>]*>\s*'
    r'<h2 class="video-section-title">(?P<title>[^<]*)',
)
"""Matches a video carousel, capturing the id the section endpoint wants."""

RECOMMENDATIONS_RE = re.compile(
    r"related-shows-carousel.*?</section>",
    re.DOTALL,
)
"""Matches the You May Also Like carousel."""

RECOMMENDATION_RE = re.compile(
    r'<a\s[^>]*?href="(?P<url>[^"]+)"[^>]*?'
    r'aa-link="(?:related shows\|\|\||\|carousel\|\|)\d+\|(?P<title>[^|]*)\|',
)
"""Matches a tile in the You May Also Like carousel, shows and movies alike."""


# TODO: Validate
def extract_show(page: str) -> dict[str, Any]:
    """Extract the show blocks, seasons, sections and recommendations."""
    return {
        "show": extract_registry_show(page),
        "series": extract_series(page),
        "seasons": extract_seasons(page),
        "sections": extract_sections(page),
        "recommendations": extract_recommendations(page),
    }


# TODO: Validate
def extract_registry_show(page: str) -> dict[str, Any]:
    """Extract the show object the page hands its own scripts.

    Raises:
        ExtractionError: If the page carries no show object.
    """
    match = REGISTRY_SHOW_RE.search(page)
    if match is None:
        msg = "The downloaded page carries no show object"
        raise ExtractionError(msg, page)
    return json.loads(match.group("json"))


# TODO: Validate
def extract_series(page: str) -> dict[str, Any]:
    """Extract the schema.org series block the page carries.

    Raises:
        ExtractionError: If the page carries no series block.
    """
    for match in LD_JSON_RE.finditer(page):
        block: dict[str, Any] = json.loads(match.group("json"))
        if block.get("@type") == "TVSeries":
            return block
    msg = "The downloaded page carries no series block"
    raise ExtractionError(msg, page)


# TODO: Validate
def extract_seasons(page: str) -> list[int]:
    """Extract the sorted season numbers from the season selector.

    The list is empty when the page has no season selector, which is how a show
    with a single season looks.
    """
    return sorted({int(match.group("season")) for match in SEASON_RE.finditer(page)})


# TODO: Validate
def extract_recommendations(page: str) -> list[dict[str, str]]:
    """Extract the You May Also Like carousel, in the order it is shown.

    Each tile gives its title and the path the site links it at. The list is
    empty when the page has no such carousel.
    """
    carousel = RECOMMENDATIONS_RE.search(page)
    if carousel is None:
        return []
    return [
        {"title": unescape(match.group("title")), "url": match.group("url")}
        for match in RECOMMENDATION_RE.finditer(carousel.group())
    ]


# TODO: Validate
def extract_sections(page: str) -> list[dict[str, Any]]:
    """Extract the id and title of every video carousel the page lists.

    The carousels are served empty and filled in by the section endpoint, so
    what the page carries is the id and the title of each one.
    """
    return [
        {"id": int(match.group("section_id")), "title": match.group("title").strip()}
        for match in SECTION_RE.finditer(page)
    ]


# TODO: Validate
class Show(BaseEndpoint):
    """Contains the show.

    The site has no show endpoint, so what is downloaded is the page and what
    is kept is the two JSON blocks written into it, plus the seasons read out of
    the selector the site fills its dropdown with and the video carousels the
    section endpoint fills in.

    Source: https://www.paramountplus.com/shows/{show_id}/

    Example request:
        - GET /shows/{show_id}/
            - HTTP/2
        - Host: www.paramountplus.com
        - User-Agent: __REDACTED__
        - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        - Accept-Language: en-US,en;q=0.9
        - Referer: https://www.paramountplus.com/shows/
        - Sec-Fetch-Dest: document
        - Sec-Fetch-Mode: navigate
        - Sec-Fetch-Site: same-origin
        - Priority: u=0, i
    """

    # TODO: Validate
    def __call__(self, show_id: str) -> ShowModel:
        """Download and parse the show file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(show_id), log_id)

    # TODO: Validate
    def download(self, show_id: str) -> str:
        """Download the show page.

        Raises:
            ShowNotFoundError: If the show does not exist.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                endpoint=f"shows/{show_id}/",
                params={},
                headers=self._client.page_headers(
                    "https://www.paramountplus.com/shows/",
                ),
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ShowNotFoundError(show_id, err.status_code, err.response) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ShowModel:
        """Load a show file into its model."""
        return model_validate_json(extract_show(data), log_id or self.default_log_id)

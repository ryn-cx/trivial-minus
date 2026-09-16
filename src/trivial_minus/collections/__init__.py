# TODO: Validate
"""Contains the Collections class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from trivial_minus.base_api_endpoint import BaseEndpoint
from trivial_minus.collection import extract_carousels, extract_hub
from trivial_minus.collections.models import CollectionsModel, model_validate_json
from trivial_minus.constants import COLLECTION_CATEGORIES_RE
from trivial_minus.exceptions import ExtractionError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
def extract_collections(page: str) -> dict[str, Any]:
    """Extract the categories and the carousels the collections hub lists."""
    return {
        "hub": extract_hub(page),
        "categories": extract_categories(page),
        "carousels": extract_carousels(page),
    }


# TODO: Validate
def extract_categories(page: str) -> list[dict[str, Any]]:
    """Extract the categories the hub sorts its collections into.

    Raises:
        ExtractionError: If the page carries no categories.
    """
    match = COLLECTION_CATEGORIES_RE.search(page)
    if match is None:
        msg = "The downloaded page carries no categories"
        raise ExtractionError(msg, page)
    return json.loads(match.group("json"))


# TODO: Validate
class Collections(BaseEndpoint):
    """Contains the collections hub.

    The site serves no JSON for the hub, so what is downloaded is the page and
    what is kept is the JSON blocks written into it. The collections themselves
    are in the All Collections A-Z carousel, which the carousel endpoint reads.
    The page is the All Collections category, so the carousels of the other
    categories are not on it.

    Source: https://www.paramountplus.com/collections/

    Example request:
        - GET /collections/
            - HTTP/2
        - Host: www.paramountplus.com
        - User-Agent: __REDACTED__
        - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        - Accept-Language: en-US,en;q=0.9
        - Referer: https://www.paramountplus.com/
        - Sec-Fetch-Dest: document
        - Sec-Fetch-Mode: navigate
        - Sec-Fetch-Site: same-origin
        - Priority: u=0, i
    """

    # TODO: Validate
    def __call__(self) -> CollectionsModel:
        """Download and parse the collections hub file."""
        return self.load(self.download(), self.default_log_id)

    # TODO: Validate
    def download(self) -> str:
        """Download the collections hub page."""
        return self._client.download(
            endpoint="collections/",
            params={},
            headers=self._client.page_headers("https://www.paramountplus.com/"),
            log_id=self.default_log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> CollectionsModel:
        """Load a collections hub file into its model."""
        return model_validate_json(
            extract_collections(data),
            log_id or self.default_log_id,
        )

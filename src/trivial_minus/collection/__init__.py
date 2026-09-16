# TODO: Validate
"""Contains the Collection class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any
from urllib.parse import unquote_plus

from trivial_minus.base_api_endpoint import BaseEndpoint
from trivial_minus.collection.models import CollectionModel, model_validate_json
from trivial_minus.constants import COLLECTION_CAROUSELS_RE, HUB_RE
from trivial_minus.exceptions import CollectionNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
def extract_collection(page: str) -> dict[str, Any]:
    """Extract the collection and the carousels the page lists."""
    return {
        "hub": extract_hub(page),
        "carousels": extract_carousels(page),
    }


# TODO: Validate
def extract_hub(page: str) -> dict[str, Any]:
    """Extract the hub object the page hands its own scripts.

    Raises:
        CollectionNotFoundError: If the page carries no hub object, which is how
            a collection the site does not have looks, since it redirects to a
            page that is not a collection at all.
    """
    match = HUB_RE.search(page)
    if match is None:
        msg = "The downloaded page carries no collection"
        raise CollectionNotFoundError(msg, page)
    return json.loads(match.group("json"))


# TODO: Validate
def extract_carousels(page: str) -> list[dict[str, Any]]:
    """Extract the carousels the page lists, with the token each one is read by.

    The carousels are served empty and filled in by the carousel endpoint, so
    what the page carries is the token and the title of each one. The titles are
    written the way a query string writes them, so they are read back out.
    """
    match = COLLECTION_CAROUSELS_RE.search(page)
    if match is None:
        return []
    carousels: list[dict[str, Any]] = json.loads(match.group("json"))
    for carousel in carousels:
        carousel["title"] = unquote_plus(carousel["title"])
    return carousels


# TODO: Validate
class Collection(BaseEndpoint):
    """Contains one collection, such as True Crime.

    The site serves no JSON for a collection, so what is downloaded is the page
    and what is kept is the two JSON blocks written into it. The shows and
    movies themselves are in the carousels, which the carousel endpoint reads.

    Source: https://www.paramountplus.com/collections/{collection_id}/

    Example request:
        - GET /collections/{collection_id}/
            - HTTP/2
        - Host: www.paramountplus.com
        - User-Agent: __REDACTED__
        - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        - Accept-Language: en-US,en;q=0.9
        - Referer: https://www.paramountplus.com/collections/
        - Sec-Fetch-Dest: document
        - Sec-Fetch-Mode: navigate
        - Sec-Fetch-Site: same-origin
        - Priority: u=0, i
    """

    # TODO: Validate
    def __call__(self, collection_id: str) -> CollectionModel:
        """Download and parse the collection file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(collection_id), log_id)

    # TODO: Validate
    def download(self, collection_id: str) -> str:
        """Download the collection page.

        Raises:
            CollectionNotFoundError: If the collection does not exist.
        """
        log_id = self.get_log_id(self.download, locals())
        page = self._client.download(
            endpoint=f"collections/{collection_id}/",
            params={},
            headers=self._client.page_headers(
                "https://www.paramountplus.com/collections/",
            ),
            log_id=log_id,
        )
        extract_hub(page)
        return page

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> CollectionModel:
        """Load a collection file into its model."""
        return model_validate_json(
            extract_collection(data),
            log_id or self.default_log_id,
        )

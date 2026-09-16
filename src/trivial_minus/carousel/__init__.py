# TODO: Validate
"""Contains the Carousel class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any
from urllib.parse import quote

from trivial_minus.base_api_endpoint import BaseEndpoint
from trivial_minus.carousel.models import CarouselModel, model_validate_json
from trivial_minus.exceptions import EmptyCarouselError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

LIMIT = 99
"""The most the site hands over at a time, since 100 or more is answered with 20."""


# TODO: Validate
def read_response(response: str) -> dict[str, Any]:
    """Parse the Carousel response, which is written as a string when it fails."""
    parsed = json.loads(response)
    if isinstance(parsed, str):
        parsed = json.loads(parsed)
    return parsed


# TODO: Validate
def extract_carousel(response: str) -> dict[str, Any]:
    """Extract the carousel from the Carousel response."""
    return read_response(response)["result"]


# TODO: Validate
class Carousel(BaseEndpoint):
    """Contains the shows, movies or collections one carousel holds.

    A carousel is read by the token the collection page carries for it, from
    `Collection.carousels` or `Collections.carousels`. The collection in the URL
    is not what picks the entries, the token is, so a token asked for under the
    wrong collection still answers with that carousel.

    Source: https://www.paramountplus.com/collections/{collection_id}/

    Example request:
        - GET /carousels/collections/configItems/{collection_id}/{token}
            - /offset/{offset}/limit/{limit}/
            - HTTP/2
        - Host: www.paramountplus.com
        - User-Agent: __REDACTED__
        - Accept: application/json, text/javascript, */*; q=0.01
        - Accept-Language: en-US,en;q=0.9
        - Referer: https://www.paramountplus.com/collections/{collection_id}/
        - X-Requested-With: XMLHttpRequest
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
    """

    # TODO: Validate
    def __call__(
        self,
        collection_id: str,
        *,
        token: str,
        offset: int = 0,
        limit: int = LIMIT,
    ) -> CarouselModel:
        """Download and parse the carousel file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(collection_id, token=token, offset=offset, limit=limit),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        collection_id: str,
        *,
        token: str,
        offset: int = 0,
        limit: int = LIMIT,
    ) -> str:
        """Download the carousel file.

        The count the file carries is how many entries it holds, not how many the
        carousel has, so the way to the end of a long carousel is to keep asking
        until the site answers that there is nothing left.

        Raises:
            EmptyCarouselError: If the carousel holds nothing at that offset.
            HTTPError: If the token is not one the site reads.
        """
        log_id = self.get_log_id(self.download, locals())
        endpoint = (
            f"carousels/collections/configItems/{collection_id}"
            f"/{quote(token, safe='')}/offset/{offset}/limit/{limit}/"
        )
        referer = f"https://www.paramountplus.com/collections/{collection_id}/"
        response = self._client.download(
            endpoint=endpoint,
            params={},
            headers=self._client.json_headers(referer),
            log_id=log_id,
        )
        return self._validate_download(response, offset)

    # TODO: Validate
    def download_all(
        self,
        collection_id: str,
        *,
        token: str,
        limit: int = LIMIT,
    ) -> list[str]:
        pages: list[str] = []
        offset = 0
        while True:
            try:
                page = self.download(
                    collection_id,
                    token=token,
                    offset=offset,
                    limit=limit,
                )
            except EmptyCarouselError:
                return pages
            pages.append(page)
            count = self.entry_count(page)
            offset += count
            if count < limit:
                return pages

    # TODO: Validate
    @staticmethod
    def entry_count(response: str) -> int:
        entries = extract_carousel(response)["data"]
        return len(entries) if isinstance(entries, list) else 0

    # TODO: Validate
    def _validate_download(self, response: str, offset: int) -> str:
        if not read_response(response)["success"]:
            raise EmptyCarouselError(offset, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> CarouselModel:
        """Load a carousel file into its model."""
        return model_validate_json(
            extract_carousel(data),
            log_id or self.default_log_id,
        )

# TODO: Validate
"""Contains the Episodes class."""

from __future__ import annotations

from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any, override

from trivialminus.base_api_endpoint import BaseEndpoint
from trivialminus.constants import WEB_DOMAIN
from trivialminus.episodes.models import EpisodesModel
from trivialminus.exceptions import EpisodesNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Episodes(BaseEndpoint[EpisodesModel]):
    """Manage the episodes file.

    Wraps the `xhr` route that populates a show's episode list, one season and
    page at a time. Fully anonymous: no cookie or subscription is required.

    Source: https://www.paramountplus.com/shows/south-park/

    Example request:
        - GET /shows/south-park/xhr/episodes/page/0/size/18/xs/0/season/28/ HTTP/2
        - Host: www.paramountplus.com
        - User-Agent: __REDACTED__
        - Accept: application/json, text/javascript, */*; q=0.01
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.paramountplus.com/shows/south-park/
        - X-Requested-With: XMLHttpRequest
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - Cookie: __REDACTED__

    An unknown or empty season returns a valid response with an empty
    `result.data` list.
    """

    _response_model = EpisodesModel

    @override
    def download(
        self,
        show: str,
        *,
        season: int,
        page: int = 0,
        size: int = 18,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        referer = f"https://{WEB_DOMAIN}/shows/{show}/"
        url = (
            f"https://{WEB_DOMAIN}/shows/{show}/xhr/episodes"
            f"/page/{page}/size/{size}/xs/0/season/{season}/"
        )
        try:
            response = self._client.download_json(url, referer=referer, log_id=log_id)
        except ResourceNotFoundError as err:
            raise EpisodesNotFoundError(
                show,
                season,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, show, season)

    def _validate_download(
        self,
        response: dict[str, Any],
        show: str,
        season: int,
    ) -> dict[str, Any]:
        # An unknown or empty season returns an empty 200 rather than a 404, so
        # the not-found error is raised manually.
        if not response["result"]["data"]:
            raise EpisodesNotFoundError(show, season, HTTPStatus.OK, response)
        return response

    @override
    def download_and_parse(
        self,
        show: str,
        *,
        season: int,
        page: int = 0,
        size: int = 18,
    ) -> EpisodesModel:
        return self.parse(self.download(show, season=season, page=page, size=size))

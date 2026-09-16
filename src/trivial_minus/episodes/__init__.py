# TODO: Validate
"""Contains the Episodes class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from trivial_minus.base_api_endpoint import BaseEndpoint
from trivial_minus.episodes.models import EpisodesModel, model_validate_json
from trivial_minus.exceptions import (
    ResourceNotFoundError,
    ShowNotFoundError,
    TrivialMinusError,
    WrongSeasonError,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())

SIZE = 18


# TODO: Validate
def extract_episodes(response: str) -> dict[str, Any]:
    """Extract the episodes from the Episodes response."""
    if result := json.loads(response)["result"]:
        return result

    msg = "The response has no episodes in it"
    raise TrivialMinusError(msg)


# TODO: Validate
class Episodes(BaseEndpoint):
    """Contains the season episodes.

    Source: https://www.paramountplus.com/shows/{show_id}/

    Example request:
        - GET /shows/{show_id}/xhr/episodes/page/{page}/size/{size}
            - /xs/0/season/{season_number}/
            - HTTP/2
        - Host: www.paramountplus.com
        - User-Agent: __REDACTED__
        - Accept: application/json, text/javascript, */*; q=0.01
        - Accept-Language: en-US,en;q=0.9
        - Referer: https://www.paramountplus.com/shows/{show_id}/
        - X-Requested-With: XMLHttpRequest
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
    """

    # TODO: Validate
    def __call__(
        self,
        show_id: str,
        *,
        season_number: int,
        page: int = 0,
        size: int = SIZE,
    ) -> EpisodesModel:
        """Download and parse the season's episodes file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(show_id, season_number=season_number, page=page, size=size),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        show_id: str,
        *,
        season_number: int,
        page: int = 0,
        size: int = SIZE,
    ) -> str:
        """Download the season episodes file.

        A season the show does not have is not an error to the site: it answers
        with an empty list, the same answer a season with nothing in it gives.

        Raises:
            ShowNotFoundError: If the show does not exist.
            WrongSeasonError: If the file is for a different season.
        """
        log_id = self.get_log_id(self.download, locals())
        endpoint = (
            f"shows/{show_id}/xhr/episodes/page/{page}/size/{size}"
            f"/xs/0/season/{season_number}/"
        )
        referer = f"https://www.paramountplus.com/shows/{show_id}/"
        try:
            response = self._client.download(
                endpoint=endpoint,
                params={},
                headers=self._client.json_headers(referer),
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ShowNotFoundError(show_id, err.status_code, err.response) from err
        return self._validate_download(response, season_number)

    # TODO: Validate
    def _validate_download(self, response: str, season_number: int) -> str:
        for episode in json.loads(response)["result"]["data"]:
            if int(episode["season_number"]) != season_number:
                raise WrongSeasonError(season_number, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> EpisodesModel:
        """Load a season episodes file into its model."""
        return model_validate_json(
            extract_episodes(data),
            log_id or self.default_log_id,
        )

# TODO: Validate
"""Contains the Section class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from trivial_minus.base_api_endpoint import BaseEndpoint
from trivial_minus.exceptions import (
    ResourceNotFoundError,
    SectionNotFoundError,
    ShowNotFoundError,
)
from trivial_minus.section.models import SectionModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

LIMIT = 20
"""How many videos the site's own carousel asks for at a time."""


# TODO: Validate
def extract_section(response: str) -> dict[str, Any]:
    """Extract the section from the Section response."""
    return json.loads(response)["result"]


# TODO: Validate
class Section(BaseEndpoint):
    """Contains one of the video carousels a show page carries.

    A section is a carousel such as Clips or The Ready Room, and its id comes
    from `Show.sections`. The show in the URL is not what picks the videos, the
    section id is, so a section id asked for under the wrong show still answers
    with that section.

    Source: https://www.paramountplus.com/shows/{show_id}/

    Example request:
        - GET /shows/{show_id}/xhr/sectionId/{section_id}/offset/{offset}
            - /limit/{limit}/xs/0/
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
        section_id: int,
        offset: int = 0,
        limit: int = LIMIT,
    ) -> SectionModel:
        """Download and parse the section file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(show_id, section_id=section_id, offset=offset, limit=limit),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        show_id: str,
        *,
        section_id: int,
        offset: int = 0,
        limit: int = LIMIT,
    ) -> str:
        """Download the section file.

        An offset past the end of the section is answered with an empty list and
        the total the section holds, the same answer an empty section gives.

        Raises:
            ShowNotFoundError: If the show does not exist.
            SectionNotFoundError: If the section does not exist.
        """
        log_id = self.get_log_id(self.download, locals())
        endpoint = (
            f"shows/{show_id}/xhr/sectionId/{section_id}"
            f"/offset/{offset}/limit/{limit}/xs/0/"
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
        return self._validate_download(response, section_id)

    # TODO: Validate
    def _validate_download(self, response: str, section_id: int) -> str:
        if not json.loads(response)["success"]:
            raise SectionNotFoundError(section_id, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SectionModel:
        """Load a section file into its model."""
        return model_validate_json(extract_section(data), log_id or self.default_log_id)

# TODO: Validate
"""Contains the Show class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from trivial_minus.base_api_endpoint import BaseEndpoint
from trivial_minus.exceptions import ResourceNotFoundError, ShowNotFoundError
from trivial_minus.show.extract import extract_show
from trivial_minus.show.models import ShowModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Show(BaseEndpoint):
    """Manage the show file.

    The site serves no JSON for a show, so what is downloaded is the page and
    the seasons are read out of the selector the site fills its dropdown with.

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
        """Look the show up and return the model it is read into."""
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
        """Read a downloaded show page into its model."""
        return model_validate_json(extract_show(data), log_id or self.default_log_id)

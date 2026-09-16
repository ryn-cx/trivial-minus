# TODO: Validate
"""Contains the TrivialMinus class."""

from __future__ import annotations

from http import HTTPStatus
from logging import NullHandler, getLogger
from time import monotonic, sleep
from typing import Any

from get_around import GetAround

from trivial_minus.episodes import Episodes
from trivial_minus.exceptions import HTTPError, ResourceNotFoundError
from trivial_minus.movie import Movie
from trivial_minus.section import Section
from trivial_minus.show import Show

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_DOMAIN = "www.paramountplus.com"

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)


# TODO: Validate
class TrivialMinus:
    """Paramount+ API wrapper."""

    # TODO: Validate
    def __init__(
        self,
        get_around_client: GetAround | None = None,
        user_agent: str = DEFAULT_USER_AGENT,
        sleep_time: float = 0,
    ) -> None:
        """Initializes the TrivialMinus client.

        The client holds one attribute per endpoint, so `client.movie(id)` looks
        a movie up and `client.movie.download(id)` and `client.movie.load(data)`
        are the halves of it.
        """
        self.get_around_client = get_around_client or GetAround()
        self.user_agent = user_agent
        self.sleep_time = sleep_time

        self.show = Show(self)
        self.episodes = Episodes(self)
        self.movie = Movie(self)
        self.section = Section(self)

    # TODO: Validate
    def json_headers(self, referer: str) -> dict[str, str]:
        """Return the headers the site's own XHR requests are sent with."""
        return {
            "user-agent": self.user_agent,
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9",
            "referer": referer,
            "x-requested-with": "XMLHttpRequest",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
        }

    # TODO: Validate
    def page_headers(self, referer: str) -> dict[str, str]:
        """Return the headers a browser asks the site for a page with."""
        return {
            "user-agent": self.user_agent,
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "en-US,en;q=0.9",
            "referer": referer,
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "priority": "u=0, i",
        }

    # TODO: Validate
    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        headers: dict[str, str],
        log_id: str,
    ) -> str:
        """Downloads from the site and returns the body as it was served.

        Raises:
            ResourceNotFoundError: If the site answers that there is no such page.
            HTTPError: If the site answers with any other unexpected status code.
        """
        logger.debug("Downloading: %s", log_id)
        url = f"https://{API_DOMAIN}/{endpoint}"
        start = monotonic()
        response = self.get_around_client.get(
            url,
            params=params,
            headers=headers,
            follow_redirects=True,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise ResourceNotFoundError(response.status_code, response.text)
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, monotonic() - start)
        sleep(self.sleep_time)
        return response.text

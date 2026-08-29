# TODO: Validate
"""Contains the Movie class."""

from __future__ import annotations

import json
import re
from logging import NullHandler, getLogger
from typing import Any

from trivial_minus.base_api_endpoint import BaseEndpoint
from trivial_minus.exceptions import (
    ExtractionError,
    MovieNotFoundError,
    ResourceNotFoundError,
    WrongMovieError,
)
from trivial_minus.movie.models import MovieModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

LD_JSON_RE = re.compile(
    r'<script type="application/ld\+json">(?P<json>.*?)</script>',
    re.DOTALL,
)
"""The schema.org blocks a page carries, one of which describes the movie."""


# TODO: Validate
class Movie(BaseEndpoint):
    """Manage the movie file.

    The site serves no JSON for a movie, so what is downloaded is the page and
    what is kept is the schema.org block written into it for search engines.

    Source: https://www.paramountplus.com/movies/video/{movie_id}/

    Example request:
        - GET /movies/video/{movie_id}/
            - HTTP/2
        - Host: www.paramountplus.com
        - User-Agent: __REDACTED__
        - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        - Accept-Language: en-US,en;q=0.9
        - Referer: https://www.paramountplus.com/movies/
        - Sec-Fetch-Dest: document
        - Sec-Fetch-Mode: navigate
        - Sec-Fetch-Site: same-origin
        - Priority: u=0, i
    """

    # TODO: Validate
    def __call__(self, movie_id: str) -> MovieModel:
        """Look the movie up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(movie_id), log_id)

    # TODO: Validate
    def download(self, movie_id: str) -> str:
        """Download the movie page and return the movie block written into it.

        Raises:
            MovieNotFoundError: If the movie does not exist.
            ExtractionError: If the page carries no movie block.
            WrongMovieError: If the block is for a different movie.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            page = self._client.download(
                endpoint=f"movies/video/{movie_id}/",
                params={},
                headers=self._client.page_headers(
                    "https://www.paramountplus.com/movies/",
                ),
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(movie_id, err.status_code, err.response) from err
        return self._extract_movie(page, movie_id)

    # TODO: Validate
    @staticmethod
    def _extract_movie(page: str, movie_id: str) -> str:
        """Return the movie block from the page, as the text it was written as."""
        for match in LD_JSON_RE.finditer(page):
            block: dict[str, Any] = json.loads(match.group("json"))
            if block.get("@type") != "Movie":
                continue
            if movie_id not in block["mainEntityOfPage"]["@id"]:
                raise WrongMovieError(movie_id, block)
            return match.group("json")
        msg = "The downloaded page carries no movie"
        raise ExtractionError(msg, page)

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> MovieModel:
        """Read a downloaded movie file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

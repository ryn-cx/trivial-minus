"""Contains the Movie class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from trivial_minus.base_api_endpoint import BaseEndpoint
from trivial_minus.exceptions import MovieNotFoundError, ResourceNotFoundError
from trivial_minus.movie.models import MovieModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Movie(BaseEndpoint[MovieModel]):
    """Manage the movie file.

    Source: https://www.paramountplus.com/movies/video/{video_id}/

    Example request:
        - GET /movies/video/{video_id}/ HTTP/2
        - Host: www.paramountplus.com
        - User-Agent: __REDACTED__
        - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Sec-GPC: 1
        - Upgrade-Insecure-Requests: 1
        - Sec-Fetch-Dest: document
        - Sec-Fetch-Mode: navigate
        - Sec-Fetch-Site: none
        - Sec-Fetch-User: ?1
        - Connection: keep-alive
        - Cookie: __REDACTED__
        - Priority: u=0, i
        - TE: trailers
    """

    _response_model = MovieModel

    @override
    def download(self, movie_id: str) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        url = f"https://www.paramountplus.com/movies/video/{movie_id}/"
        try:
            return self._client.download_ld_json(
                url,
                referer="https://www.paramountplus.com/movies/",
                schema_type="Movie",
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(
                movie_id,
                err.status_code,
                err.response,
            ) from err

    @override
    def download_and_parse(self, movie_id: str) -> MovieModel:
        return self.parse(self.download(movie_id))

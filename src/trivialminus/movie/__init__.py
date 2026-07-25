# TODO: Validate
"""Contains the Movie class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from trivialminus.base_api_endpoint import BaseEndpoint
from trivialminus.constants import WEB_DOMAIN
from trivialminus.exceptions import MovieNotFoundError, ResourceNotFoundError
from trivialminus.movie.models import MovieModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Movie(BaseEndpoint[MovieModel]):
    """Manage the movie file.

    Movie detail pages have no `xhr` JSON route, but they embed a schema.org
    `Movie` object in a `<script type="application/ld+json">` tag, which is
    served anonymously. This endpoint fetches the page and extracts that block.

    Source: https://www.paramountplus.com/movies/video/ALVE01KT235XQDEK58R7H2012VNZMK/

    Example request:
        - GET /movies/video/ALVE01KT235XQDEK58R7H2012VNZMK/ HTTP/2
        - Host: www.paramountplus.com
        - User-Agent: __REDACTED__
        - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.paramountplus.com/movies/

    The returned object is the schema.org `Movie` (name, description,
    datePublished, image, contentRating, genre, publisher, ...).
    """

    _response_model = MovieModel

    @override
    def download(self, movie_id: str) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        url = f"https://{WEB_DOMAIN}/movies/video/{movie_id}/"
        try:
            return self._client.download_ld_json(
                url,
                referer=f"https://{WEB_DOMAIN}/movies/",
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

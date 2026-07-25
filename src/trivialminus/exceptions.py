"""Exceptions."""

from __future__ import annotations

from typing import Any


class TrivialMinusError(Exception):
    """Base exception for the trivialminus library."""

    response: str | dict[str, Any] | None = None


class HTTPError(TrivialMinusError):
    """Raised when an HTTP request fails with an unexpected status code."""

    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested resource does not exist."""


class ShowNotFoundError(ResourceNotFoundError):
    """Raised when the requested show does not exist."""

    def __init__(
        self,
        show: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the show and the originating response."""
        self.show = show
        super().__init__(status_code, response)


class SeasonNotFoundError(ResourceNotFoundError):
    """Raised when the requested season of an existing show does not exist."""

    def __init__(
        self,
        show: str,
        season: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the show, season, and the originating response."""
        self.show = show
        self.season = season
        super().__init__(status_code, response)


class MovieNotFoundError(ResourceNotFoundError):
    """Raised when the requested movie does not exist."""

    def __init__(
        self,
        movie_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the movie id and the originating response."""
        self.movie_id = movie_id
        super().__init__(status_code, response)


class ExtractionError(TrivialMinusError):
    """Raised when expected data cannot be found in a page's HTML."""

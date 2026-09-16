# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class TrivialMinusError(Exception):
    """Base exception for TrivialMinus."""

    response: str | dict[str, Any] | None = None


# TODO: Validate
class HTTPError(TrivialMinusError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class ResourceNotFoundError(HTTPError):
    """Raised when the site reports that the requested page does not exist."""


# TODO: Validate
class ShowNotFoundError(ResourceNotFoundError):
    """Raised when the requested show does not exist."""

    # TODO: Validate
    def __init__(
        self,
        show_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the show id and the originating response."""
        self.show_id = show_id
        super().__init__(status_code, response)


# TODO: Validate
class MovieNotFoundError(ResourceNotFoundError):
    """Raised when the requested movie does not exist."""

    # TODO: Validate
    def __init__(
        self,
        movie_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the movie id and the originating response."""
        self.movie_id = movie_id
        super().__init__(status_code, response)


# TODO: Validate
class ExtractionError(TrivialMinusError):
    """Raised when a page does not carry the data that was expected in it."""

    # TODO: Validate
    def __init__(self, message: str, response: str | None = None) -> None:
        """Initialize with the problem and the page it was read from."""
        self.response = response
        super().__init__(message)


# TODO: Validate
class WrongSeasonError(TrivialMinusError):
    """Raised when the downloaded episodes are for a different season."""

    # TODO: Validate
    def __init__(
        self,
        season_number: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the season that was asked for and the response."""
        self.season_number = season_number
        self.response = response
        super().__init__(f"The downloaded file is not for season {season_number}")


# TODO: Validate
class WrongMovieError(TrivialMinusError):
    """Raised when the downloaded page is for a different movie."""

    # TODO: Validate
    def __init__(
        self,
        movie_id: str,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the movie that was asked for and the response."""
        self.movie_id = movie_id
        self.response = response
        super().__init__(f"The downloaded file is not for movie {movie_id}")


# TODO: Validate
class SectionNotFoundError(TrivialMinusError):
    """Raised when the requested section does not exist."""

    # TODO: Validate
    def __init__(
        self,
        section_id: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the section id and the originating response."""
        self.section_id = section_id
        self.response = response
        super().__init__(f"There is no section {section_id}")


# TODO: Validate
class CollectionNotFoundError(TrivialMinusError):
    """Raised when the requested collection does not exist."""

    # TODO: Validate
    def __init__(self, message: str, response: str | None = None) -> None:
        """Initialize with the problem and the page it was read from."""
        self.response = response
        super().__init__(message)


# TODO: Validate
class EmptyCarouselError(TrivialMinusError):
    """Raised when a carousel holds nothing at the offset that was asked for."""

    # TODO: Validate
    def __init__(
        self,
        offset: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the offset that was asked for and the response."""
        self.offset = offset
        self.response = response
        super().__init__(f"The carousel holds nothing at offset {offset}")

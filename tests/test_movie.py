# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from trivial_minus.exceptions import MovieNotFoundError
from trivial_minus.movie.models import MovieModel

if TYPE_CHECKING:
    from trivial_minus import TrivialMinus

MOVIE_IDS = [
    # https://www.paramountplus.com/movies/video/ALVE01KT235XQDEK58R7H2012VNZMK/
    pytest.param("ALVE01KT235XQDEK58R7H2012VNZMK", id="paw patrol fire rescue"),
]


class MovieTest(RecordedEndpoint):
    MODEL = MovieModel


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_download(client: TrivialMinus, movie_id: str) -> None:
    MovieTest.download_test(movie_id, lambda: client.movie.download(movie_id))


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_parse(client: TrivialMinus, movie_id: str) -> None:
    data = client.movie.load(MovieTest.recorded_content(movie_id))
    assert movie_id in data.main_entity_of_page.field_id


# TODO: Validate
@pytest.mark.parametrize(
    "movie_id",
    [pytest.param("000000000000000000000000000000", id="movie that does not exist")],
)
def test_download_invalid(client: TrivialMinus, movie_id: str) -> None:
    MovieTest.error_test(
        movie_id,
        lambda: client.movie.download(movie_id),
        MovieNotFoundError,
    )

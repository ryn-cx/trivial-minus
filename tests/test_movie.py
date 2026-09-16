# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from trivial_minus.exceptions import MovieNotFoundError

if TYPE_CHECKING:
    from trivial_minus import TrivialMinus

MOVIE_IDS = [
    # https://www.paramountplus.com/movies/video/ALVE01KT235XQDEK58R7H2012VNZMK/
    pytest.param("ALVE01KT235XQDEK58R7H2012VNZMK", id="paw patrol fire rescue"),
]


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_download(client: TrivialMinus, movie_id: str) -> None:
    movie = client.movie(movie_id)
    assert movie_id in movie.main_entity_of_page.field_id


# TODO: Validate
def test_download_invalid(client: TrivialMinus) -> None:
    with pytest.raises(MovieNotFoundError):
        client.movie.download("000000000000000000000000000000")

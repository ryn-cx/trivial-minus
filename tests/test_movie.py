from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from tests.utils import assert_error, download_and_save, parsed_json
from trivial_minus.exceptions import MovieNotFoundError

if TYPE_CHECKING:
    from trivial_minus import TrivialMinus
    from trivial_minus.movie import Movie


class TestData(BaseModel):
    __test__ = False

    movie_id: str
    name: str
    movie_name: str


TEST_DATA = [
    TestData(
        movie_id="ALVE01KT235XQDEK58R7H2012VNZMK",
        name="paw-patrol-fire-rescue",
        movie_name="PAW Patrol: Fire Rescue",
    ),
]


@pytest.fixture(scope="session")
def client(client: TrivialMinus) -> Movie:
    return client.movie


@pytest.fixture(params=TEST_DATA, ids=lambda test_data: test_data.name)
def test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


def test_download(client: Movie, test_data: TestData) -> None:
    download_and_save(
        client,
        test_data.name,
        lambda: client.download(test_data.movie_id),
    )


def test_parse(client: Movie, test_data: TestData) -> None:
    movie = parsed_json(client, test_data.name)
    assert movie.name == test_data.movie_name


def test_download_invalid(client: Movie) -> None:
    assert_error(
        client,
        "000000000000000000000000000000",
        lambda: client.download("000000000000000000000000000000"),
        MovieNotFoundError,
    )

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from tests.utils import assert_error, download_and_save, parsed_json
from trivialminus.exceptions import SeasonNotFoundError, ShowNotFoundError

if TYPE_CHECKING:
    from trivialminus import TrivialMinus
    from trivialminus.episodes import Episodes


class TestData(BaseModel):
    __test__ = False

    show: str
    season: int
    name: str


TEST_DATA = [
    TestData(show="south-park", season=28, name="south-park-s28"),
]


@pytest.fixture(scope="session")
def client(client: TrivialMinus) -> Episodes:
    return client.episodes


@pytest.fixture(params=TEST_DATA, ids=lambda test_data: test_data.name)
def test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


def test_download(client: Episodes, test_data: TestData) -> None:
    download_and_save(
        client,
        test_data.name,
        lambda: client.download(test_data.show, season_number=test_data.season),
    )


def test_parse(client: Episodes, test_data: TestData) -> None:
    episodes = parsed_json(client, test_data.name)
    assert episodes.result.data
    assert all(
        episode.season_number == str(test_data.season)
        for episode in episodes.result.data
    )


def test_download_invalid_show(client: Episodes) -> None:
    assert_error(
        client,
        "invalid-show",
        lambda: client.download("invalid-show", season_number=1),
        ShowNotFoundError,
    )


def test_download_invalid_season(client: Episodes) -> None:
    assert_error(
        client,
        "invalid-season",
        lambda: client.download("south-park", season_number=999),
        SeasonNotFoundError,
    )

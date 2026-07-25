from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from trivialminus import TrivialMinus
    from trivialminus.search import Search


class TestData(BaseModel):
    __test__ = False

    term: str
    name: str
    content_id: str
    title: str


TEST_DATA = [
    TestData(
        term="south",
        name="south",
        content_id="61457085",
        title="South Park",
    ),
]


@pytest.fixture(scope="session")
def client(client: TrivialMinus) -> Search:
    return client.search


@pytest.fixture(params=TEST_DATA, ids=lambda test_data: test_data.name)
def test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


def test_download(client: Search, test_data: TestData) -> None:
    download_and_save(client, test_data.name, lambda: client.download(test_data.term))


def test_parse(client: Search, test_data: TestData) -> None:
    search = parsed_json(client, test_data.name)
    assert search.success

    shows = [r for r in search.results if r.content_id == test_data.content_id]
    assert len(shows) == 1
    show = shows[0]
    assert show.title == test_data.title
    assert show.series_title == test_data.title
    assert show.media_type == "shows"

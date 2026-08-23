# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from trivial_minus.episodes.models import EpisodesModel
from trivial_minus.exceptions import ShowNotFoundError

if TYPE_CHECKING:
    from trivial_minus import TrivialMinus

SEASONS = [
    # https://www.paramountplus.com/shows/south-park/
    pytest.param("south-park", 28, id="south park season 28"),
    pytest.param("south-park", 999, id="south park season that does not exist"),
]


class EpisodesTest(RecordedEndpoint):
    MODEL = EpisodesModel


# TODO: Validate
def recording_name(show_id: str, season_number: int) -> str:
    return f"{show_id}-s{season_number}"


# TODO: Validate
@pytest.mark.parametrize(("show_id", "season_number"), SEASONS)
def test_download(client: TrivialMinus, show_id: str, season_number: int) -> None:
    EpisodesTest.download_test(
        recording_name(show_id, season_number),
        lambda: client.episodes.download(show_id, season_number=season_number),
    )


# TODO: Validate
@pytest.mark.parametrize(("show_id", "season_number"), SEASONS)
def test_parse(client: TrivialMinus, show_id: str, season_number: int) -> None:
    recorded = EpisodesTest.recorded_content(recording_name(show_id, season_number))
    data = client.episodes.load(recorded)
    for episode in data.result.data:
        assert int(episode.season_number) == season_number


# TODO: Validate
def test_parse_unknown_season(client: TrivialMinus) -> None:
    # A season the show does not have is answered with an empty list rather than
    # an error, which is the same answer a season with nothing in it gives.
    data = client.episodes.load(EpisodesTest.recorded_content("south-park-s999"))
    assert data.result.data == []


# TODO: Validate
@pytest.mark.parametrize(
    "show_id",
    [pytest.param("invalid-show", id="show that does not exist")],
)
def test_download_invalid(client: TrivialMinus, show_id: str) -> None:
    EpisodesTest.error_test(
        show_id,
        lambda: client.episodes.download(show_id, season_number=1),
        ShowNotFoundError,
    )

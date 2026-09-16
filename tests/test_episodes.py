# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from trivial_minus.exceptions import ShowNotFoundError

if TYPE_CHECKING:
    from trivial_minus import TrivialMinus

# https://www.paramountplus.com/shows/south-park/
SEASONS = [pytest.param("south-park", 28, id="south park season 28")]


# TODO: Validate
@pytest.mark.parametrize(("show_id", "season_number"), SEASONS)
def test_download(client: TrivialMinus, show_id: str, season_number: int) -> None:
    episodes = client.episodes(show_id, season_number=season_number)
    assert episodes.data
    assert all(int(episode.season_number) == season_number for episode in episodes.data)


# TODO: Validate
def test_download_unknown_season(client: TrivialMinus) -> None:
    # A season the show does not have is answered with an empty list rather than
    # an error, which is the same answer a season with nothing in it gives.
    assert client.episodes("south-park", season_number=999).data == []


# TODO: Validate
def test_download_invalid(client: TrivialMinus) -> None:
    with pytest.raises(ShowNotFoundError):
        client.episodes.download("invalid-show", season_number=1)

# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from trivial_minus.exceptions import ShowNotFoundError

if TYPE_CHECKING:
    from trivial_minus import TrivialMinus

# https://www.paramountplus.com/shows/south-park/
SHOWS = [pytest.param("south-park", "South Park", 61457085, 28, id="south park")]


# TODO: Validate
@pytest.mark.parametrize(("show_id", "name", "cbs_show_id", "latest_season"), SHOWS)
def test_download(
    client: TrivialMinus,
    show_id: str,
    name: str,
    cbs_show_id: int,
    latest_season: int,
) -> None:
    show = client.show(show_id)
    assert show.seasons == list(range(1, latest_season + 1))
    assert show.show.key == show_id
    assert show.show.id == cbs_show_id
    assert show.show.name == name
    assert show.series.name == name
    assert all(
        recommendation.title and recommendation.url
        for recommendation in show.recommendations
    )
    assert all(section.id and section.title for section in show.sections)


# TODO: Validate
def test_download_invalid(client: TrivialMinus) -> None:
    with pytest.raises(ShowNotFoundError):
        client.show.download("invalid-show")

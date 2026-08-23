# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from trivial_minus.exceptions import ShowNotFoundError
from trivial_minus.show.extract import extract_show
from trivial_minus.show.models import ShowModel

if TYPE_CHECKING:
    from pathlib import Path

    from pydantic import BaseModel

    from tests.utils import Category
    from trivial_minus import TrivialMinus

SHOW_IDS = [
    # https://www.paramountplus.com/shows/south-park/
    pytest.param("south-park", id="south park"),
]


class ShowTest(RecordedEndpoint):
    MODEL = ShowModel

    # TODO: Validate
    @classmethod
    def recorded_path(cls, name: str | int, category: Category = None) -> Path:
        # A show is answered with a page rather than JSON, so the recording is
        # the page itself.
        return super().recorded_path(name, category).with_suffix(".html")

    # TODO: Validate
    @classmethod
    def load_models(cls, name: str | int, category: Category = None) -> list[BaseModel]:
        return [
            ShowModel.model_validate(extract_show(document))
            for document in cls.recorded_documents(name, category)
        ]


# TODO: Validate
@pytest.mark.parametrize("show_id", SHOW_IDS)
def test_download(client: TrivialMinus, show_id: str) -> None:
    ShowTest.download_test(show_id, lambda: client.show.download(show_id))


# TODO: Validate
@pytest.mark.parametrize(
    ("show_id", "latest_season"),
    [pytest.param("south-park", 28, id="south park")],
)
def test_parse(client: TrivialMinus, show_id: str, latest_season: int) -> None:
    data = client.show.load(ShowTest.recorded_content(show_id))
    assert data.seasons == list(range(1, latest_season + 1))


# TODO: Validate
@pytest.mark.parametrize(
    "show_id",
    [pytest.param("invalid-show", id="show that does not exist")],
)
def test_download_invalid(client: TrivialMinus, show_id: str) -> None:
    ShowTest.error_test(
        show_id,
        lambda: client.show.download(show_id),
        ShowNotFoundError,
    )

# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from trivialminus.exceptions import ShowNotFoundError
from trivialminus.show_html import ShowHTML

if TYPE_CHECKING:
    from trivialminus import TrivialMinus

# Anchors are out of order and Season 2 is duplicated to check sorting and dedup.
_SAMPLE_HTML = """
<a aria-label="Season 2" data-index="1" data-value="2"></a>
<a aria-label="Season 1" data-index="0" data-value="1" data-selected="true"></a>
<a aria-label="Season 2" data-index="1" data-value="2"></a>
<a aria-label="Season 3" data-index="2" data-value="3"></a>
"""


@pytest.fixture(scope="session")
def client(client: TrivialMinus) -> ShowHTML:
    return client.show_html


def test_download(client: ShowHTML) -> None:
    html = client.download("south-park")
    assert isinstance(html, str)
    assert "<html" in html.lower()


def test_download_invalid_show(client: ShowHTML) -> None:
    with pytest.raises(ShowNotFoundError):
        client.download("invalid-show")


def test_extract_season_numbers() -> None:
    assert ShowHTML.extract_season_numbers(_SAMPLE_HTML) == [1, 2, 3]


def test_extract_season_numbers_empty() -> None:
    assert ShowHTML.extract_season_numbers("<html></html>") == []

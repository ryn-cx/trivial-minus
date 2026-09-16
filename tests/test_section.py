# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from trivial_minus.exceptions import SectionNotFoundError, ShowNotFoundError

if TYPE_CHECKING:
    from trivial_minus import TrivialMinus

# https://www.paramountplus.com/shows/south-park/
SECTIONS = [pytest.param("south-park", 301229, id="south park new episode clips")]


# TODO: Validate
@pytest.mark.parametrize(("show_id", "section_id"), SECTIONS)
def test_download(client: TrivialMinus, show_id: str, section_id: int) -> None:
    section = client.section(show_id, section_id=section_id)
    assert section.title
    assert section.data
    assert section.total >= len(section.data)
    assert all(video.content_id and video.title for video in section.data)


# TODO: Validate
@pytest.mark.parametrize(("show_id", "section_id"), SECTIONS)
def test_download_past_the_end(
    client: TrivialMinus,
    show_id: str,
    section_id: int,
) -> None:
    # An offset past the end is answered with an empty list rather than an error.
    section = client.section(show_id, section_id=section_id, offset=999999)
    assert section.data == []
    assert section.total


# TODO: Validate
def test_sections_come_from_the_show_page(client: TrivialMinus) -> None:
    sections = client.show("south-park").sections
    assert sections
    section = client.section("south-park", section_id=sections[0].id)
    assert section.title == sections[0].title


# TODO: Validate
def test_download_unknown_section(client: TrivialMinus) -> None:
    with pytest.raises(SectionNotFoundError):
        client.section.download("south-park", section_id=1)


# TODO: Validate
def test_download_invalid(client: TrivialMinus) -> None:
    with pytest.raises(ShowNotFoundError):
        client.section.download("invalid-show", section_id=301229)

# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from trivial_minus.exceptions import EmptyCarouselError, HTTPError

if TYPE_CHECKING:
    from trivial_minus import TrivialMinus

# https://www.paramountplus.com/collections/true-crime/
COLLECTION_ID = "true-crime"


# TODO: Validate
@pytest.fixture
def token(client: TrivialMinus) -> str:
    return client.collection(COLLECTION_ID).carousels[0].token


# TODO: Validate
def test_download(client: TrivialMinus, token: str) -> None:
    carousel = client.carousel(COLLECTION_ID, token=token)
    assert carousel.title
    assert carousel.data
    assert carousel.total == len(carousel.data)
    assert all(entry.href for entry in carousel.data)


# TODO: Validate
def test_download_past_the_end(client: TrivialMinus, token: str) -> None:
    with pytest.raises(EmptyCarouselError):
        client.carousel.download(COLLECTION_ID, token=token, offset=999999)


# TODO: Validate
def test_download_invalid(client: TrivialMinus) -> None:
    with pytest.raises(HTTPError):
        client.carousel.download(COLLECTION_ID, token="not-a-token")  # noqa: S106

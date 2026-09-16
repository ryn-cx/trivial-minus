# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from trivial_minus.exceptions import CollectionNotFoundError

if TYPE_CHECKING:
    from trivial_minus import TrivialMinus

# https://www.paramountplus.com/collections/true-crime/
COLLECTIONS = [pytest.param("true-crime", id="true crime")]


# TODO: Validate
@pytest.mark.parametrize("collection_id", COLLECTIONS)
def test_download(client: TrivialMinus, collection_id: str) -> None:
    collection = client.collection(collection_id)
    assert collection.hub.hub_slug == collection_id
    assert collection.carousels
    assert all(carousel.token and carousel.title for carousel in collection.carousels)


# TODO: Validate
def test_download_invalid(client: TrivialMinus) -> None:
    # An unknown collection is redirected to a page that is not a collection.
    with pytest.raises(CollectionNotFoundError):
        client.collection.download("invalid-collection")

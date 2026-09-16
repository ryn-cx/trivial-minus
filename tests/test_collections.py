# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from trivial_minus import TrivialMinus

# https://www.paramountplus.com/collections/
ALL_COLLECTIONS = "All Collections A-Z"


# TODO: Validate
def test_download(client: TrivialMinus) -> None:
    collections = client.collections()
    assert collections.hub.hub_slug == "all-collections"
    assert collections.categories[0].slug == "all-collections"
    assert all(carousel.token and carousel.title for carousel in collections.carousels)


# TODO: Validate
def test_the_collections_are_in_a_carousel(client: TrivialMinus) -> None:
    carousels = client.collections().carousels
    a_to_z = next(
        carousel for carousel in carousels if carousel.title == ALL_COLLECTIONS
    )
    collections = client.carousel("all-collections", token=a_to_z.token)
    assert collections.title == ALL_COLLECTIONS
    assert all(collection.slug and collection.title for collection in collections.data)
    assert "true-crime" in [collection.slug for collection in collections.data]

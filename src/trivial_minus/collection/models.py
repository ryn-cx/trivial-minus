# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import CollectionModel as OptionalModel
from .strict_models import CollectionModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Carousel,
        CollectionModel,
        Hub,
    )
else:
    from .optional_models import (
        Carousel,
        CollectionModel,
        Hub,
    )

__all__ = [
    "Carousel",
    "CollectionModel",
    "Hub",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> CollectionModel:
    """Read a downloaded file into CollectionModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

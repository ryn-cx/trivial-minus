# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import CollectionsModel as OptionalModel
from .strict_models import CollectionsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Carousel,
        Category,
        CollectionsModel,
        Hub,
    )
else:
    from .optional_models import (
        Carousel,
        Category,
        CollectionsModel,
        Hub,
    )

__all__ = [
    "Carousel",
    "Category",
    "CollectionsModel",
    "Hub",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> CollectionsModel:
    """Read a downloaded file into CollectionsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import MovieModel as OptionalModel
from .strict_models import MovieModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        EligibleRegion,
        ExpectsAcceptanceOfItem,
        Logo,
        MainEntityOfPage,
        MovieModel,
        PotentialActionItem,
        Publisher,
        Seller,
        Target,
    )
else:
    from .optional_models import (
        EligibleRegion,
        ExpectsAcceptanceOfItem,
        Logo,
        MainEntityOfPage,
        MovieModel,
        PotentialActionItem,
        Publisher,
        Seller,
        Target,
    )

__all__ = [
    "EligibleRegion",
    "ExpectsAcceptanceOfItem",
    "Logo",
    "MainEntityOfPage",
    "MovieModel",
    "PotentialActionItem",
    "Publisher",
    "Seller",
    "Target",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> MovieModel:
    """Read a downloaded file into MovieModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

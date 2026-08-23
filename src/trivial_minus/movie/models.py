"""MovieModel, strict to a type checker, all-optional at runtime.

A type checker reads the strict model, so every field carries the type and
the requiredness the schema recorded. At runtime the all-optional copy is imported
instead, so a response that has drifted still parses and a field the data is
missing is None despite what its type hint says.
"""

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

# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SectionModel as OptionalModel
from .strict_models import SectionModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Datum,
        SectionModel,
    )
else:
    from .optional_models import (
        Datum,
        SectionModel,
    )

__all__ = [
    "Datum",
    "SectionModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SectionModel:
    """Read a downloaded file into SectionModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

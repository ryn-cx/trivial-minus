from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field

class Logo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    url: str

class Publisher(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_context: str = Field(..., alias='@context')
    field_type: str = Field(..., alias='@type')
    name: str
    url: str
    logo: Logo

class MainEntityOfPage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    field_id: str = Field(..., alias='@id')

class Target(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    url_template: str = Field(..., alias='urlTemplate')
    action_platform: str = Field(..., alias='actionPlatform')
    in_language: str = Field(..., alias='inLanguage')

class EligibleRegion(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    name: str

class Seller(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    name: str
    same_as: str = Field(..., alias='sameAs')

class ExpectsAcceptanceOfItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    category: str
    availability_starts: AwareDatetime = Field(..., alias='availabilityStarts')
    availability_ends: AwareDatetime = Field(..., alias='availabilityEnds')
    eligible_region: EligibleRegion = Field(..., alias='eligibleRegion')
    name: str
    price: float
    price_currency: str = Field(..., alias='priceCurrency')
    seller: Seller

class PotentialActionItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    target: Target
    expects_acceptance_of: list[ExpectsAcceptanceOfItem] = Field(..., alias='expectsAcceptanceOf')

class MovieModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_context: str = Field(..., alias='@context')
    field_type: str = Field(..., alias='@type')
    name: str
    description: str
    date_published: AwareDatetime = Field(..., alias='datePublished')
    image: str
    content_rating: str = Field(..., alias='contentRating')
    genre: str
    publisher: Publisher
    main_entity_of_page: MainEntityOfPage = Field(..., alias='mainEntityOfPage')
    potential_action: list[PotentialActionItem] = Field(..., alias='potentialAction')
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input

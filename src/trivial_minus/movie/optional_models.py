from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Logo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    url: str | None = None

class Publisher(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_context: str | None = Field(None, alias='@context')
    field_type: str | None = Field(None, alias='@type')
    name: str | None = None
    url: str | None = None
    logo: Logo | None = None

class MainEntityOfPage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    field_id: str | None = Field(None, alias='@id')

class Target(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    url_template: str | None = Field(None, alias='urlTemplate')
    action_platform: str | None = Field(None, alias='actionPlatform')
    in_language: str | None = Field(None, alias='inLanguage')

class EligibleRegion(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    name: str | None = None

class Seller(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    name: str | None = None
    same_as: str | None = Field(None, alias='sameAs')

class ExpectsAcceptanceOfItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    category: str | None = None
    availability_starts: AwareDatetime | None = Field(None, alias='availabilityStarts')
    availability_ends: AwareDatetime | None = Field(None, alias='availabilityEnds')
    eligible_region: EligibleRegion | None = Field(None, alias='eligibleRegion')
    name: str | None = None
    price: float | None = None
    price_currency: str | None = Field(None, alias='priceCurrency')
    seller: Seller | None = None

class PotentialActionItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    target: Target | None = None
    expects_acceptance_of: list[ExpectsAcceptanceOfItem] | None = Field(None, alias='expectsAcceptanceOf')

class MovieModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_context: str | None = Field(None, alias='@context')
    field_type: str | None = Field(None, alias='@type')
    name: str | None = None
    description: str | None = None
    date_published: AwareDatetime | None = Field(None, alias='datePublished')
    image: str | None = None
    content_rating: str | None = Field(None, alias='contentRating')
    genre: str | None = None
    publisher: Publisher | None = None
    main_entity_of_page: MainEntityOfPage | None = Field(None, alias='mainEntityOfPage')
    potential_action: list[PotentialActionItem] | None = Field(None, alias='potentialAction')
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

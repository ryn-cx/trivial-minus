from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Logo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')

class Publisher(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_context: str | Any = Field(None, alias='@context', union_mode='left_to_right')
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    logo: Logo | Any = Field(default=None, union_mode='left_to_right')

class MainEntityOfPage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    field_id: str | Any = Field(None, alias='@id', union_mode='left_to_right')

class Target(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    url_template: str | Any = Field(None, alias='urlTemplate', union_mode='left_to_right')
    action_platform: str | Any = Field(None, alias='actionPlatform', union_mode='left_to_right')
    in_language: str | Any = Field(None, alias='inLanguage', union_mode='left_to_right')

class EligibleRegion(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')

class Seller(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    same_as: str | Any = Field(None, alias='sameAs', union_mode='left_to_right')

class ExpectsAcceptanceOfItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    category: str | Any = Field(default=None, union_mode='left_to_right')
    availability_starts: AwareDatetime | Any = Field(None, alias='availabilityStarts', union_mode='left_to_right')
    availability_ends: AwareDatetime | Any = Field(None, alias='availabilityEnds', union_mode='left_to_right')
    eligible_region: EligibleRegion | Any = Field(None, alias='eligibleRegion', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    price: float | Any = Field(default=None, union_mode='left_to_right')
    price_currency: str | Any = Field(None, alias='priceCurrency', union_mode='left_to_right')
    seller: Seller | Any = Field(default=None, union_mode='left_to_right')

class PotentialActionItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    target: Target | Any = Field(default=None, union_mode='left_to_right')
    expects_acceptance_of: list[ExpectsAcceptanceOfItem] | Any = Field(None, alias='expectsAcceptanceOf', union_mode='left_to_right')

class MovieModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_context: str | Any = Field(None, alias='@context', union_mode='left_to_right')
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    date_published: AwareDatetime | Any = Field(None, alias='datePublished', union_mode='left_to_right')
    image: str | Any = Field(default=None, union_mode='left_to_right')
    content_rating: str | Any = Field(None, alias='contentRating', union_mode='left_to_right')
    genre: str | Any = Field(default=None, union_mode='left_to_right')
    publisher: Publisher | Any = Field(default=None, union_mode='left_to_right')
    main_entity_of_page: MainEntityOfPage | Any = Field(None, alias='mainEntityOfPage', union_mode='left_to_right')
    potential_action: list[PotentialActionItem] | Any = Field(None, alias='potentialAction', union_mode='left_to_right')
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

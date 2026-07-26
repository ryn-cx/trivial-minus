from pydantic import AwareDatetime, ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel

class Logo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    url: str

class Publisher(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_context: str = Field(..., alias='@context')
    field_type: str = Field(..., alias='@type')
    name: str
    url: str
    logo: Logo

class MainEntityOfPage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    field_id: str = Field(..., alias='@id')

class Target(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    url_template: str = Field(..., alias='urlTemplate')
    action_platform: str = Field(..., alias='actionPlatform')
    in_language: str = Field(..., alias='inLanguage')

class EligibleRegion(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    name: str

class Seller(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    name: str
    same_as: str = Field(..., alias='sameAs')

class ExpectsAcceptanceOfItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    category: str
    availability_starts: AwareDatetime = Field(..., alias='availabilityStarts')
    availability_ends: AwareDatetime = Field(..., alias='availabilityEnds')
    eligible_region: EligibleRegion = Field(..., alias='eligibleRegion')
    name: str
    price: float
    price_currency: str = Field(..., alias='priceCurrency')
    seller: Seller

class PotentialActionItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    target: Target
    expects_acceptance_of: list[ExpectsAcceptanceOfItem] = Field(..., alias='expectsAcceptanceOf')

class MovieModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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

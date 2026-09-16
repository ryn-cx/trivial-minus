from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from uuid import UUID
from pydantic import BaseModel, Field

class Hub(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    hub_slug: str = Field(..., alias='hubSlug')
    hub_page_type: str = Field(..., alias='hubPageType')
    page_type: str = Field(..., alias='pageType')

class Category(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    title: str
    locale: str
    slug: str
    global_menu_link: str
    link_type: str
    item_key: str = Field(..., alias='itemKey')

class Carousel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    token: str
    display_id: UUID = Field(..., alias='displayId')
    reco_id: UUID = Field(..., alias='recoId')
    carousel_id: UUID = Field(..., alias='carouselId')
    orientation: str
    title: str
    position: None
    model: str
    api_base_url: str = Field(..., alias='apiBaseUrl')
    slug: str
    channel_slug: UUID = Field(..., alias='channelSlug')
    is_content_highlight_enabled: bool = Field(..., alias='isContentHighlightEnabled')
    carousel_presentation_style: str = Field(..., alias='carouselPresentationStyle')
    has_browse_numeric_experiment: bool = Field(..., alias='hasBrowseNumericExperiment')
    dom_id: str = Field(..., alias='domId')

class CollectionsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hub: Hub
    categories: list[Category]
    carousels: list[Carousel]
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

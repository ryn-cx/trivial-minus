from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

class Hub(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | None = None
    hub_slug: str | None = Field(None, alias='hubSlug')
    hub_page_type: str | None = Field(None, alias='hubPageType')
    page_type: str | None = Field(None, alias='pageType')

class Category(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | None = None
    title: str | None = None
    locale: str | None = None
    slug: str | None = None
    global_menu_link: str | None = None
    link_type: str | None = None
    item_key: str | None = Field(None, alias='itemKey')

class Carousel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    token: str | None = None
    display_id: UUID | None = Field(None, alias='displayId')
    reco_id: UUID | None = Field(None, alias='recoId')
    carousel_id: UUID | None = Field(None, alias='carouselId')
    orientation: str | None = None
    title: str | None = None
    position: Any | None = None
    model: str | None = None
    api_base_url: str | None = Field(None, alias='apiBaseUrl')
    slug: str | None = None
    channel_slug: UUID | None = Field(None, alias='channelSlug')
    is_content_highlight_enabled: bool | None = Field(None, alias='isContentHighlightEnabled')
    carousel_presentation_style: str | None = Field(None, alias='carouselPresentationStyle')
    has_browse_numeric_experiment: bool | None = Field(None, alias='hasBrowseNumericExperiment')
    dom_id: str | None = Field(None, alias='domId')

class CollectionsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hub: Hub | None = None
    categories: list[Category] | None = None
    carousels: list[Carousel] | None = None
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

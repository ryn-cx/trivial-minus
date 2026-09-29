from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

class Hub(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | Any = Field(default=None, union_mode='left_to_right')
    hub_slug: str | Any = Field(None, alias='hubSlug', union_mode='left_to_right')
    hub_page_type: str | Any = Field(None, alias='hubPageType', union_mode='left_to_right')
    screen_name: str | Any = Field(None, alias='screenName', union_mode='left_to_right')

class Carousel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    token: str | Any = Field(default=None, union_mode='left_to_right')
    display_id: UUID | Any = Field(None, alias='displayId', union_mode='left_to_right')
    reco_id: UUID | Any = Field(None, alias='recoId', union_mode='left_to_right')
    carousel_id: UUID | str | Any = Field(None, alias='carouselId', union_mode='left_to_right')
    orientation: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    position: Any | None = None
    model: str | Any = Field(default=None, union_mode='left_to_right')
    api_base_url: str | Any = Field(None, alias='apiBaseUrl', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    channel_slug: UUID | str | Any = Field(None, alias='channelSlug', union_mode='left_to_right')
    is_content_highlight_enabled: bool | Any = Field(None, alias='isContentHighlightEnabled', union_mode='left_to_right')
    carousel_presentation_style: str | Any = Field(None, alias='carouselPresentationStyle', union_mode='left_to_right')
    has_browse_numeric_experiment: bool | Any = Field(None, alias='hasBrowseNumericExperiment', union_mode='left_to_right')
    dom_id: str | Any = Field(None, alias='domId', union_mode='left_to_right')

class CollectionModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hub: Hub | Any = Field(default=None, union_mode='left_to_right')
    carousels: list[Carousel] | Any = Field(default=None, union_mode='left_to_right')
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

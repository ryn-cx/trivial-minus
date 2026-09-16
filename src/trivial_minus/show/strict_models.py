from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field

class Show(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str
    id: int
    key: str
    tune_in_time: str
    available_for_profile_types_on_shows: str = Field(..., alias='availableForProfileTypesOnShows')
    category: str

class Target(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    url_template: str = Field(..., alias='urlTemplate')
    action_platform: str | list[str] = Field(..., alias='actionPlatform')

class PotentialActionItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    target: Target

class Broadcaster(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    legal_name: str = Field(..., alias='legalName')
    logo: str
    name: str
    url: str

class PublishedOn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    name: str
    broadcaster: Broadcaster

class PublicationItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    start_date: AwareDatetime | str = Field(..., alias='startDate', union_mode='left_to_right')
    published_on: PublishedOn | None = Field(None, alias='publishedOn')

class EpisodeItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    episode_number: str = Field(..., alias='episodeNumber')
    name: str
    description: str
    url: str
    publication: list[PublicationItem]

class ContainsSeason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    name: str
    number_of_episodes: str = Field(..., alias='numberOfEpisodes')
    episode: list[EpisodeItem]

class Series(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_context: str = Field(..., alias='@context')
    field_id: str = Field(..., alias='@id')
    field_type: str = Field(..., alias='@type')
    name: str
    url: str
    potential_action: list[PotentialActionItem] = Field(..., alias='potentialAction')
    contains_season: ContainsSeason = Field(..., alias='containsSeason')

class Section(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    title: str

class Recommendation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    url: str

class ShowModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    show: Show
    series: Series
    seasons: list[int]
    sections: list[Section]
    recommendations: list[Recommendation]
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

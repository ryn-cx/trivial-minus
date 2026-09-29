from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Show(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | Any = Field(default=None, union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    tune_in_time: str | Any = Field(default=None, union_mode='left_to_right')
    available_for_profile_types_on_shows: str | Any = Field(None, alias='availableForProfileTypesOnShows', union_mode='left_to_right')
    category: str | Any = Field(default=None, union_mode='left_to_right')

class Target(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    url_template: str | Any = Field(None, alias='urlTemplate', union_mode='left_to_right')
    action_platform: str | list[str] | Any = Field(None, alias='actionPlatform', union_mode='left_to_right')

class PotentialActionItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    target: Target | Any = Field(default=None, union_mode='left_to_right')

class Broadcaster(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    legal_name: str | Any = Field(None, alias='legalName', union_mode='left_to_right')
    logo: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')

class PublishedOn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    broadcaster: Broadcaster | Any = Field(default=None, union_mode='left_to_right')

class PublicationItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    start_date: AwareDatetime | str | Any = Field(None, alias='startDate', union_mode='left_to_right')
    published_on: PublishedOn | Any = Field(None, alias='publishedOn', union_mode='left_to_right')

class EpisodeItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    episode_number: str | Any = Field(None, alias='episodeNumber', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    publication: list[PublicationItem] | Any = Field(default=None, union_mode='left_to_right')

class ContainsSeason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    number_of_episodes: str | Any = Field(None, alias='numberOfEpisodes', union_mode='left_to_right')
    episode: list[EpisodeItem] | Any = Field(default=None, union_mode='left_to_right')

class Series(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_context: str | Any = Field(None, alias='@context', union_mode='left_to_right')
    field_id: str | Any = Field(None, alias='@id', union_mode='left_to_right')
    field_type: str | Any = Field(None, alias='@type', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    potential_action: list[PotentialActionItem] | Any = Field(None, alias='potentialAction', union_mode='left_to_right')
    contains_season: ContainsSeason | Any = Field(None, alias='containsSeason', union_mode='left_to_right')

class Section(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Recommendation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')

class ShowModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    show: Show | Any = Field(default=None, union_mode='left_to_right')
    series: Series | Any = Field(default=None, union_mode='left_to_right')
    seasons: list[int] | Any = Field(default=None, union_mode='left_to_right')
    sections: list[Section] | Any = Field(default=None, union_mode='left_to_right')
    recommendations: list[Recommendation] | Any = Field(default=None, union_mode='left_to_right')
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

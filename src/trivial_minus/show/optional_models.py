from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Show(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    id: int | None = None
    key: str | None = None
    tune_in_time: str | None = None
    available_for_profile_types_on_shows: str | None = Field(None, alias='availableForProfileTypesOnShows')
    category: str | None = None

class Target(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    url_template: str | None = Field(None, alias='urlTemplate')
    action_platform: str | list[str] | None = Field(None, alias='actionPlatform')

class PotentialActionItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    target: Target | None = None

class Broadcaster(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    legal_name: str | None = Field(None, alias='legalName')
    logo: str | None = None
    name: str | None = None
    url: str | None = None

class PublishedOn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    name: str | None = None
    broadcaster: Broadcaster | None = None

class PublicationItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    start_date: AwareDatetime | str | None = Field(None, alias='startDate', union_mode='left_to_right')
    published_on: PublishedOn | None = Field(None, alias='publishedOn')

class EpisodeItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    episode_number: str | None = Field(None, alias='episodeNumber')
    name: str | None = None
    description: str | None = None
    url: str | None = None
    publication: list[PublicationItem] | None = None

class ContainsSeason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    name: str | None = None
    number_of_episodes: str | None = Field(None, alias='numberOfEpisodes')
    episode: list[EpisodeItem] | None = None

class Series(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_context: str | None = Field(None, alias='@context')
    field_id: str | None = Field(None, alias='@id')
    field_type: str | None = Field(None, alias='@type')
    name: str | None = None
    url: str | None = None
    potential_action: list[PotentialActionItem] | None = Field(None, alias='potentialAction')
    contains_season: ContainsSeason | None = Field(None, alias='containsSeason')

class Section(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | None = None
    title: str | None = None

class Recommendation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    url: str | None = None

class ShowModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    show: Show | None = None
    series: Series | None = None
    seasons: list[int] | None = None
    sections: list[Section] | None = None
    recommendations: list[Recommendation] | None = None
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

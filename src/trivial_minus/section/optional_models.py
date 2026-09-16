from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    media_type: str | None = Field(None, alias='mediaType')
    type: str | None = None
    show_id: int | None = Field(None, alias='showId')
    content_id: str | None = Field(None, alias='contentId')
    season_number: str | None = Field(None, alias='seasonNumber')
    episode_number: str | None = Field(None, alias='episodeNumber')
    airdate: str | None = None
    airdate_iso: AwareDatetime | None = Field(None, alias='airdateISO')
    start_date_iso: AwareDatetime | None = Field(None, alias='startDateISO')
    start_date: str | None = Field(None, alias='startDate')
    air_date: int | None = Field(None, alias='airDate')
    subscription_level: str | None = Field(None, alias='subscriptionLevel')
    show_page_url: str | None = Field(None, alias='showPageUrl')
    video_properties: list[str] | None = Field(None, alias='videoProperties')
    brand: str | None = None
    label: str | None = None
    title: str | None = None
    alt: str | None = None
    series_title: str | None = Field(None, alias='seriesTitle')
    content_type: str | None = None
    genre: str | None = None
    primary_category_name: str | None = Field(None, alias='primaryCategoryName')
    show_seasonless: bool | None = Field(None, alias='showSeasonless')
    show_episodeless: bool | None = Field(None, alias='showEpisodeless')
    rating_icon: str | None = Field(None, alias='ratingIcon')
    is_user_subscriber: bool | None = Field(None, alias='isUserSubscriber')
    status: str | None = None
    vod: str | None = None
    position_num: int | None = Field(None, alias='positionNum')
    is_live: bool | None = None
    show_or_movie_title: str | None = Field(None, alias='showOrMovieTitle')
    video_preview_url: str | None = Field(None, alias='videoPreviewURL')
    locked: bool | None = None
    is_movie: bool | None = Field(None, alias='isMovie')
    content_locked: str | None = Field(None, alias='contentLocked')
    display_item_title: bool | None = Field(None, alias='displayItemTitle')
    href: str | None = None
    thumb: str | None = None
    is_seasonless: bool | None = Field(None, alias='isSeasonless')
    is_episodeless: bool | None = Field(None, alias='isEpisodeless')
    aa_link: str | None = Field(None, alias='aaLink')
    rating: str | None = None
    duration: str | None = None
    content_id_impression: str | None = Field(None, alias='contentIdImpression')
    position: int | None = None
    item_pem: Any | None = Field(None, alias='itemPEM')
    about: str | None = None
    description: str | None = None
    bundle_locked: bool | None = Field(None, alias='bundleLocked')
    lock_icon: Any | None = Field(None, alias='lockIcon')

class SectionModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: Any | None = None
    title: str | None = None
    orientation: str | None = None
    left_arrow: str | None = Field(None, alias='leftArrow')
    right_arrow: str | None = Field(None, alias='rightArrow')
    display_id: str | None = Field(None, alias='displayId')
    reco_id: str | None = Field(None, alias='recoId')
    data: list[Datum] | None = None
    carousel_id: str | None = Field(None, alias='carouselId')
    model: str | None = None
    rank_model: str | None = None
    pvr_model: str | None = None
    data_ci: str | None = Field(None, alias='dataCi')
    carousel_presentation_style: str | None = Field(None, alias='carouselPresentationStyle')
    is_content_highlight_enabled: bool | None = Field(None, alias='isContentHighlightEnabled')
    total: int | None = None
    include_profile_dropdown: bool | None = Field(None, alias='includeProfileDropdown')
    live_sports_data: bool | None = Field(None, alias='liveSportsData')
    display_scores_toggle: bool | None = Field(None, alias='displayScoresToggle')
    carousel_pem: Any | None = Field(None, alias='carouselPEM')
    red_dot: bool | None = Field(None, alias='redDot')
    display_show_title: bool | None = Field(None, alias='displayShowTitle')
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

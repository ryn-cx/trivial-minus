from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    show_id: int | Any = Field(None, alias='showId', union_mode='left_to_right')
    content_id: str | Any = Field(None, alias='contentId', union_mode='left_to_right')
    season_number: str | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    episode_number: str | Any = Field(None, alias='episodeNumber', union_mode='left_to_right')
    airdate: str | Any = Field(default=None, union_mode='left_to_right')
    airdate_iso: AwareDatetime | Any = Field(None, alias='airdateISO', union_mode='left_to_right')
    start_date_iso: AwareDatetime | Any = Field(None, alias='startDateISO', union_mode='left_to_right')
    start_date: str | Any = Field(None, alias='startDate', union_mode='left_to_right')
    air_date: int | Any = Field(None, alias='airDate', union_mode='left_to_right')
    subscription_level: str | Any = Field(None, alias='subscriptionLevel', union_mode='left_to_right')
    show_page_url: str | Any = Field(None, alias='showPageUrl', union_mode='left_to_right')
    video_properties: list[str] | Any = Field(None, alias='videoProperties', union_mode='left_to_right')
    brand: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    alt: str | Any = Field(default=None, union_mode='left_to_right')
    series_title: str | Any = Field(None, alias='seriesTitle', union_mode='left_to_right')
    content_type: str | Any = Field(default=None, union_mode='left_to_right')
    genre: str | Any = Field(default=None, union_mode='left_to_right')
    primary_category_name: str | Any = Field(None, alias='primaryCategoryName', union_mode='left_to_right')
    show_seasonless: bool | Any = Field(None, alias='showSeasonless', union_mode='left_to_right')
    show_episodeless: bool | Any = Field(None, alias='showEpisodeless', union_mode='left_to_right')
    rating_icon: str | Any = Field(None, alias='ratingIcon', union_mode='left_to_right')
    is_user_subscriber: bool | Any = Field(None, alias='isUserSubscriber', union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    vod: str | Any = Field(default=None, union_mode='left_to_right')
    position_num: int | Any = Field(None, alias='positionNum', union_mode='left_to_right')
    is_live: bool | Any = Field(default=None, union_mode='left_to_right')
    show_or_movie_title: str | Any = Field(None, alias='showOrMovieTitle', union_mode='left_to_right')
    video_preview_url: str | Any = Field(None, alias='videoPreviewURL', union_mode='left_to_right')
    locked: bool | Any = Field(default=None, union_mode='left_to_right')
    is_movie: bool | Any = Field(None, alias='isMovie', union_mode='left_to_right')
    content_locked: str | Any = Field(None, alias='contentLocked', union_mode='left_to_right')
    display_item_title: bool | Any = Field(None, alias='displayItemTitle', union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    thumb: str | Any = Field(default=None, union_mode='left_to_right')
    is_seasonless: bool | Any = Field(None, alias='isSeasonless', union_mode='left_to_right')
    is_episodeless: bool | Any = Field(None, alias='isEpisodeless', union_mode='left_to_right')
    aa_link: str | Any = Field(None, alias='aaLink', union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    duration: str | Any = Field(default=None, union_mode='left_to_right')
    content_id_impression: str | Any = Field(None, alias='contentIdImpression', union_mode='left_to_right')
    position: int | Any = Field(default=None, union_mode='left_to_right')
    item_pem: Any | None = Field(None, alias='itemPEM')
    about: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    bundle_locked: bool | Any = Field(None, alias='bundleLocked', union_mode='left_to_right')
    lock_icon: str | Any = Field(None, alias='lockIcon', union_mode='left_to_right')
    upsell_url: str | Any = Field(None, alias='upsellUrl', union_mode='left_to_right')

class SectionModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: Any | None = None
    title: str | Any = Field(default=None, union_mode='left_to_right')
    orientation: str | Any = Field(default=None, union_mode='left_to_right')
    left_arrow: str | Any = Field(None, alias='leftArrow', union_mode='left_to_right')
    right_arrow: str | Any = Field(None, alias='rightArrow', union_mode='left_to_right')
    display_id: str | Any = Field(None, alias='displayId', union_mode='left_to_right')
    reco_id: str | Any = Field(None, alias='recoId', union_mode='left_to_right')
    data: list[Datum] | Any = Field(default=None, union_mode='left_to_right')
    carousel_id: str | Any = Field(None, alias='carouselId', union_mode='left_to_right')
    model: str | Any = Field(default=None, union_mode='left_to_right')
    rank_model: str | Any = Field(default=None, union_mode='left_to_right')
    pvr_model: str | Any = Field(default=None, union_mode='left_to_right')
    data_ci: str | Any = Field(None, alias='dataCi', union_mode='left_to_right')
    carousel_presentation_style: str | Any = Field(None, alias='carouselPresentationStyle', union_mode='left_to_right')
    is_content_highlight_enabled: bool | Any = Field(None, alias='isContentHighlightEnabled', union_mode='left_to_right')
    total: int | Any = Field(default=None, union_mode='left_to_right')
    include_profile_dropdown: bool | Any = Field(None, alias='includeProfileDropdown', union_mode='left_to_right')
    live_sports_data: bool | Any = Field(None, alias='liveSportsData', union_mode='left_to_right')
    display_scores_toggle: bool | Any = Field(None, alias='displayScoresToggle', union_mode='left_to_right')
    carousel_pem: Any | None = Field(None, alias='carouselPEM')
    red_dot: bool | Any = Field(None, alias='redDot', union_mode='left_to_right')
    display_show_title: bool | Any = Field(None, alias='displayShowTitle', union_mode='left_to_right')
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

from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    media_type: str = Field(..., alias='mediaType')
    type: str
    show_id: int = Field(..., alias='showId')
    content_id: str = Field(..., alias='contentId')
    season_number: str = Field(..., alias='seasonNumber')
    episode_number: str = Field(..., alias='episodeNumber')
    airdate: str
    airdate_iso: AwareDatetime = Field(..., alias='airdateISO')
    start_date_iso: AwareDatetime = Field(..., alias='startDateISO')
    start_date: str = Field(..., alias='startDate')
    air_date: int = Field(..., alias='airDate')
    subscription_level: str = Field(..., alias='subscriptionLevel')
    show_page_url: str = Field(..., alias='showPageUrl')
    video_properties: list[str] = Field(..., alias='videoProperties')
    brand: str
    label: str
    title: str
    alt: str
    series_title: str = Field(..., alias='seriesTitle')
    content_type: str
    genre: str
    primary_category_name: str = Field(..., alias='primaryCategoryName')
    show_seasonless: bool = Field(..., alias='showSeasonless')
    show_episodeless: bool = Field(..., alias='showEpisodeless')
    rating_icon: str = Field(..., alias='ratingIcon')
    is_user_subscriber: bool = Field(..., alias='isUserSubscriber')
    status: str
    vod: str
    position_num: int = Field(..., alias='positionNum')
    is_live: bool
    show_or_movie_title: str = Field(..., alias='showOrMovieTitle')
    video_preview_url: str = Field(..., alias='videoPreviewURL')
    locked: bool
    is_movie: bool = Field(..., alias='isMovie')
    content_locked: str = Field(..., alias='contentLocked')
    display_item_title: bool = Field(..., alias='displayItemTitle')
    href: str
    thumb: str
    is_seasonless: bool = Field(..., alias='isSeasonless')
    is_episodeless: bool = Field(..., alias='isEpisodeless')
    aa_link: str = Field(..., alias='aaLink')
    rating: str
    duration: str
    content_id_impression: str = Field(..., alias='contentIdImpression')
    position: int
    item_pem: None = Field(..., alias='itemPEM')
    about: str
    description: str
    bundle_locked: bool = Field(..., alias='bundleLocked')
    lock_icon: None = Field(..., alias='lockIcon')

class SectionModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: None
    title: str
    orientation: str
    left_arrow: str = Field(..., alias='leftArrow')
    right_arrow: str = Field(..., alias='rightArrow')
    display_id: str = Field(..., alias='displayId')
    reco_id: str = Field(..., alias='recoId')
    data: list[Datum]
    carousel_id: str = Field(..., alias='carouselId')
    model: str
    rank_model: str
    pvr_model: str
    data_ci: str = Field(..., alias='dataCi')
    carousel_presentation_style: str = Field(..., alias='carouselPresentationStyle')
    is_content_highlight_enabled: bool = Field(..., alias='isContentHighlightEnabled')
    total: int
    include_profile_dropdown: bool = Field(..., alias='includeProfileDropdown')
    live_sports_data: bool = Field(..., alias='liveSportsData')
    display_scores_toggle: bool = Field(..., alias='displayScoresToggle')
    carousel_pem: None = Field(..., alias='carouselPEM')
    red_dot: bool = Field(..., alias='redDot')
    display_show_title: bool = Field(..., alias='displayShowTitle')
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

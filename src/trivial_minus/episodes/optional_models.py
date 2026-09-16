from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Subrating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    description: str | None = None

class RegionalRatings(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    region: str | None = None
    rating: str | None = None
    disclaimer: Any | None = None
    secondary_descriptors: str | None = Field(None, alias='secondaryDescriptors')
    subratings: list[Subrating] | None = None
    consumer_advice: Any | None = Field(None, alias='consumerAdvice')
    rating_icon: Any | None = Field(None, alias='ratingIcon')

class Thumb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    large: str | None = None
    small: str | None = None
    field_640x360: str | None = Field(None, alias='640x360')
    field_640x480: str | None = Field(None, alias='640x480')
    field_1400x2100: str | None = Field(None, alias='1400x2100')
    poster: Any | None = None

class EsturLs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    amazon: str | None = None
    i_tunes: str | None = Field(None, alias='iTunes')

class RegionalRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    region: str | None = None
    rating: str | None = None
    disclaimer: Any | None = None
    secondary_descriptors: str | None = Field(None, alias='secondaryDescriptors')
    subratings: list[Subrating] | None = None
    consumer_advice: Any | None = Field(None, alias='consumerAdvice')
    rating_icon: Any | None = Field(None, alias='ratingIcon')

class MetaData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    airdate_iso: AwareDatetime | None = None
    airdate_tv: bool | None = None
    asset_type: str | None = Field(None, alias='assetType')
    brand: str | None = None
    media_type: Any | None = Field(None, alias='mediaType')
    channel_name: Any | None = Field(None, alias='channelName')
    content_id: str | None = Field(None, alias='contentId')
    content_url: str | None = Field(None, alias='contentUrl')
    end_credits_chapter_time: Any | None = Field(None, alias='endCreditsChapterTime')
    episode_number: str | None = Field(None, alias='episodeNumber')
    estur_ls: EsturLs | None = Field(None, alias='ESTURLs')
    exclude_oztam: Any | None = Field(None, alias='excludeOztam')
    full_episode: bool | None = Field(None, alias='fullEpisode')
    is_service_allowed: bool | None = Field(None, alias='isServiceAllowed')
    oztam_media_id: Any | None = Field(None, alias='oztamMediaId')
    pid: Any | None = None
    daistream_key: Any | None = Field(None, alias='daistreamKey')
    preview_image_url: Any | None = Field(None, alias='previewImageURL')
    rating: str | None = None
    regional_ratings: list[RegionalRating] | None = Field(None, alias='regionalRatings')
    season_number: str | None = Field(None, alias='seasonNumber')
    series_title: str | None = Field(None, alias='seriesTitle')
    show_page_url: str | None = Field(None, alias='showPageURL')
    subscription_level: str | None = Field(None, alias='subscriptionLevel')
    thumbnail: Any | None = None
    thumbnail_sheet: Any | None = Field(None, alias='thumbnailSheet')
    tv_rating_flag: bool | None = Field(None, alias='tvRatingFlag')
    video_length: int | None = Field(None, alias='videoLength')
    video_page_url: str | None = Field(None, alias='videoPageURL')
    video_title: str | None = Field(None, alias='videoTitle')
    label: str | None = None
    video_properties: list[str] | None = Field(None, alias='videoProperties')
    playback_events: Any | None = Field(None, alias='playbackEvents')
    browser_version: str | None = Field(None, alias='browserVersion')
    current_listing_title: Any | None = Field(None, alias='currentListingTitle')

class ThumbnailSetItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: int | None = None
    width: int | None = None
    asset_type: str | None = Field(None, alias='assetType')
    url: str | None = None

class RegionalRating1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    region: str | None = None
    rating: str | None = None
    disclaimer: Any | None = None
    secondary_descriptors: str | None = Field(None, alias='secondaryDescriptors')
    subratings: list[Subrating] | None = None
    consumer_advice: Any | None = Field(None, alias='consumerAdvice')
    rating_icon: Any | None = Field(None, alias='ratingIcon')

class ApiMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    genre: str | None = None
    status: str | None = None
    show_page_url: str | None = Field(None, alias='showPageUrl')
    air_date: int | None = Field(None, alias='airDate')
    description: str | None = None
    short_description: str | None = Field(None, alias='shortDescription')
    label: str | None = None
    full_episode: bool | None = Field(None, alias='fullEpisode')
    content_id: str | None = Field(None, alias='contentId')
    title: str | None = None
    episode_num: str | None = Field(None, alias='episodeNum')
    season_num: str | None = Field(None, alias='seasonNum')
    brand: str | None = None
    series_title: str | None = Field(None, alias='seriesTitle')
    field_air_date: str | None = Field(None, alias='_airDate')
    duration: int | None = None
    rating: str | None = None
    expiration_date: int | None = Field(None, alias='expirationDate')
    field_expiration_date: str | None = Field(None, alias='_expirationDate')
    field_air_date_iso: AwareDatetime | None = Field(None, alias='_airDateISO')
    subscription_level: str | None = Field(None, alias='subscriptionLevel')
    media_available_date: AwareDatetime | None = Field(None, alias='mediaAvailableDate')
    media_available_date_epoch: int | None = Field(None, alias='mediaAvailableDateEpoch')
    is_live: bool | None = Field(None, alias='isLive')
    is_protected: bool | None = Field(None, alias='isProtected')
    thumbnail_set: list[ThumbnailSetItem] | None = Field(None, alias='thumbnailSet')
    download_country_set: list[Any] | None = Field(None, alias='downloadCountrySet')
    regional_ratings: list[RegionalRating1] | None = Field(None, alias='regionalRatings')
    video_properties: list[str] | None = Field(None, alias='videoProperties')
    available_for_profile_types: list[str] | None = Field(None, alias='availableForProfileTypes')
    copyright: str | None = None
    add_ons: list[Any] | None = Field(None, alias='addOns')
    brand_slug: str | None = Field(None, alias='brandSlug')
    original_release_year: int | None = Field(None, alias='originalReleaseYear')
    is_content_accessible_in_can: bool | None = Field(None, alias='isContentAccessibleInCAN')
    thumbnail_sheet_set: list[Any] | None = Field(None, alias='thumbnailSheetSet')
    is_product_placement: bool | None = Field(None, alias='isProductPlacement')
    video_title: str | None = Field(None, alias='videoTitle')

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    title: str | None = None
    series_title: str | None = None
    label: str | None = None
    content_id: str | None = None
    airdate: str | None = None
    airdate_ts: int | None = None
    airdate_iso: AwareDatetime | None = None
    expiredate_raw: str | None = None
    season_number: str | None = None
    episode_number: str | None = None
    duration: str | None = None
    duration_raw: int | None = None
    rating: str | None = None
    regional_ratings: RegionalRatings | None = Field(None, alias='regionalRatings')
    description: str | None = None
    short_description: str | None = Field(None, alias='shortDescription')
    thumb: Thumb | None = None
    url: str | None = None
    app_url: str | None = None
    amazon_est_url: str | None = None
    itunes_est_url: str | None = None
    streaming_url: str | None = None
    live_streaming_url: str | None = None
    tms_program_id: str | None = None
    show_id: Any | None = None
    asset_type: str | None = None
    status: str | None = None
    expiry_date: str | None = None
    is_paid_content: bool | None = None
    ios_available_status: str | None = None
    ios_available_date: str | None = None
    android_available_status: str | None = None
    android_available_date: str | None = None
    tracking_media_id: Any | None = None
    signature: Any | None = None
    media_type: Any | None = None
    vtag: Any | None = None
    is_live: bool | None = None
    med_time: int | None = Field(None, alias='medTime')
    genre: str | None = None
    meta_data: MetaData | None = Field(None, alias='metaData')
    brand: str | None = None
    video_properties: list[str] | None = Field(None, alias='videoProperties')
    available_for_profile_types: list[str] | None = Field(None, alias='availableForProfileTypes')
    primary_category_name: str | None = Field(None, alias='primaryCategoryName')
    playback_events: Any | None = Field(None, alias='playbackEvents')
    cast: Any | None = None
    show_assets: Any | None = Field(None, alias='showAssets')
    movie_assets: Any | None = Field(None, alias='movieAssets')
    channel_name: Any | None = Field(None, alias='channelName')
    is_content_accessible_in_can: bool | None = Field(None, alias='isContentAccessibleInCAN')
    api_metadata: ApiMetadata | None = Field(None, alias='apiMetadata')
    media_content_type: str | None = None
    mpd_url: Any | None = None
    license_url: Any | None = None
    closed_captions: Any | None = None
    position_num: int | None = Field(None, alias='positionNum')
    is_protected: bool | None = None
    drm: bool | None = None
    raw_url: str | None = None
    episode_title: str | None = None
    video_preview_url: str | None = Field(None, alias='videoPreviewURL')
    feature: AwareDatetime | None = None
    pubdate_iso: Any | None = None
    content_locked: str | None = Field(None, alias='contentLocked')
    play_icon: str | None = Field(None, alias='playIcon')
    thumb_url: str | None = Field(None, alias='thumbUrl')
    season_title: str | None = Field(None, alias='seasonTitle')
    season_abbr: str | None = Field(None, alias='seasonAbbr')
    episode_abbr: str | None = Field(None, alias='episodeAbbr')
    episode_number_title: str | None = Field(None, alias='episodeNumberTitle')
    label_subscribe: str | None = Field(None, alias='labelSubscribe')
    rating_text: str | None = Field(None, alias='ratingText')
    rating_icon: Any | None = Field(None, alias='ratingIcon')
    is_user_subscriber: bool | None = Field(None, alias='isUserSubscriber')
    aa_link: str | None = Field(None, alias='aaLink')
    data_tracking: str | None = Field(None, alias='dataTracking')
    display_title: str | None = Field(None, alias='displayTitle')
    display_description: str | None = Field(None, alias='displayDescription')
    lock_level: str | None = Field(None, alias='lockLevel')

class EpisodesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    data: list[Datum] | None = None
    total: int | None = None
    display_seasons: bool | None = None
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

from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Subrating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class RegionalRatings(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    region: str | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    disclaimer: Any | None = None
    secondary_descriptors: str | Any = Field(None, alias='secondaryDescriptors', union_mode='left_to_right')
    subratings: list[Subrating] | Any = Field(default=None, union_mode='left_to_right')
    consumer_advice: Any | None = Field(None, alias='consumerAdvice')
    rating_icon: Any | None = Field(None, alias='ratingIcon')

class Thumb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    large: str | Any = Field(default=None, union_mode='left_to_right')
    small: str | Any = Field(default=None, union_mode='left_to_right')
    field_640x360: str | Any = Field(None, alias='640x360', union_mode='left_to_right')
    field_640x480: str | Any = Field(None, alias='640x480', union_mode='left_to_right')
    field_1400x2100: str | Any = Field(None, alias='1400x2100', union_mode='left_to_right')
    poster: Any | None = None

class EsturLs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    amazon: str | Any = Field(default=None, union_mode='left_to_right')
    i_tunes: str | Any = Field(None, alias='iTunes', union_mode='left_to_right')

class RegionalRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    region: str | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    disclaimer: Any | None = None
    secondary_descriptors: str | Any = Field(None, alias='secondaryDescriptors', union_mode='left_to_right')
    subratings: list[Subrating] | Any = Field(default=None, union_mode='left_to_right')
    consumer_advice: Any | None = Field(None, alias='consumerAdvice')
    rating_icon: Any | None = Field(None, alias='ratingIcon')

class MetaData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    airdate_iso: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    airdate_tv: bool | Any = Field(default=None, union_mode='left_to_right')
    asset_type: str | Any = Field(None, alias='assetType', union_mode='left_to_right')
    brand: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: Any | None = Field(None, alias='mediaType')
    channel_name: Any | None = Field(None, alias='channelName')
    content_id: str | Any = Field(None, alias='contentId', union_mode='left_to_right')
    content_url: str | Any = Field(None, alias='contentUrl', union_mode='left_to_right')
    end_credits_chapter_time: Any | None = Field(None, alias='endCreditsChapterTime')
    episode_number: str | Any = Field(None, alias='episodeNumber', union_mode='left_to_right')
    estur_ls: EsturLs | Any = Field(None, alias='ESTURLs', union_mode='left_to_right')
    exclude_oztam: Any | None = Field(None, alias='excludeOztam')
    full_episode: bool | Any = Field(None, alias='fullEpisode', union_mode='left_to_right')
    is_service_allowed: bool | Any = Field(None, alias='isServiceAllowed', union_mode='left_to_right')
    oztam_media_id: Any | None = Field(None, alias='oztamMediaId')
    pid: str | Any = Field(default=None, union_mode='left_to_right')
    daistream_key: Any | None = Field(None, alias='daistreamKey')
    preview_image_url: Any | None = Field(None, alias='previewImageURL')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    regional_ratings: list[RegionalRating] | Any = Field(None, alias='regionalRatings', union_mode='left_to_right')
    season_number: str | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    series_title: str | Any = Field(None, alias='seriesTitle', union_mode='left_to_right')
    show_page_url: str | Any = Field(None, alias='showPageURL', union_mode='left_to_right')
    subscription_level: str | Any = Field(None, alias='subscriptionLevel', union_mode='left_to_right')
    thumbnail: Any | None = None
    thumbnail_sheet: Any | None = Field(None, alias='thumbnailSheet')
    tv_rating_flag: bool | Any = Field(None, alias='tvRatingFlag', union_mode='left_to_right')
    video_length: int | Any = Field(None, alias='videoLength', union_mode='left_to_right')
    video_page_url: str | Any = Field(None, alias='videoPageURL', union_mode='left_to_right')
    video_title: str | Any = Field(None, alias='videoTitle', union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    video_properties: list[str] | Any = Field(None, alias='videoProperties', union_mode='left_to_right')
    playback_events: Any | None = Field(None, alias='playbackEvents')
    browser_version: str | Any = Field(None, alias='browserVersion', union_mode='left_to_right')
    current_listing_title: Any | None = Field(None, alias='currentListingTitle')

class ThumbnailSetItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: int | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    asset_type: str | Any = Field(None, alias='assetType', union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')

class RegionalRating1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    region: str | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    disclaimer: Any | None = None
    secondary_descriptors: str | Any = Field(None, alias='secondaryDescriptors', union_mode='left_to_right')
    subratings: list[Subrating] | Any = Field(default=None, union_mode='left_to_right')
    consumer_advice: Any | None = Field(None, alias='consumerAdvice')
    rating_icon: Any | None = Field(None, alias='ratingIcon')

class ApiMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    genre: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    show_page_url: str | Any = Field(None, alias='showPageUrl', union_mode='left_to_right')
    air_date: int | Any = Field(None, alias='airDate', union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    short_description: str | Any = Field(None, alias='shortDescription', union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    full_episode: bool | Any = Field(None, alias='fullEpisode', union_mode='left_to_right')
    content_id: str | Any = Field(None, alias='contentId', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    episode_num: str | Any = Field(None, alias='episodeNum', union_mode='left_to_right')
    season_num: str | Any = Field(None, alias='seasonNum', union_mode='left_to_right')
    brand: str | Any = Field(default=None, union_mode='left_to_right')
    series_title: str | Any = Field(None, alias='seriesTitle', union_mode='left_to_right')
    field_air_date: str | Any = Field(None, alias='_airDate', union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    expiration_date: int | Any = Field(None, alias='expirationDate', union_mode='left_to_right')
    field_expiration_date: str | Any = Field(None, alias='_expirationDate', union_mode='left_to_right')
    field_air_date_iso: AwareDatetime | Any = Field(None, alias='_airDateISO', union_mode='left_to_right')
    subscription_level: str | Any = Field(None, alias='subscriptionLevel', union_mode='left_to_right')
    media_available_date: AwareDatetime | Any = Field(None, alias='mediaAvailableDate', union_mode='left_to_right')
    media_available_date_epoch: int | Any = Field(None, alias='mediaAvailableDateEpoch', union_mode='left_to_right')
    is_live: bool | Any = Field(None, alias='isLive', union_mode='left_to_right')
    is_protected: bool | Any = Field(None, alias='isProtected', union_mode='left_to_right')
    thumbnail_set: list[ThumbnailSetItem] | Any = Field(None, alias='thumbnailSet', union_mode='left_to_right')
    download_country_set: list[Any] | Any = Field(None, alias='downloadCountrySet', union_mode='left_to_right')
    regional_ratings: list[RegionalRating1] | Any = Field(None, alias='regionalRatings', union_mode='left_to_right')
    video_properties: list[str] | Any = Field(None, alias='videoProperties', union_mode='left_to_right')
    available_for_profile_types: list[str] | Any = Field(None, alias='availableForProfileTypes', union_mode='left_to_right')
    copyright: str | Any = Field(default=None, union_mode='left_to_right')
    add_ons: list[str] | Any = Field(None, alias='addOns', union_mode='left_to_right')
    original_release_year: int | Any = Field(None, alias='originalReleaseYear', union_mode='left_to_right')
    is_content_accessible_in_can: bool | Any = Field(None, alias='isContentAccessibleInCAN', union_mode='left_to_right')
    thumbnail_sheet_set: list[Any] | Any = Field(None, alias='thumbnailSheetSet', union_mode='left_to_right')
    is_product_placement: bool | Any = Field(None, alias='isProductPlacement', union_mode='left_to_right')
    video_title: str | Any = Field(None, alias='videoTitle', union_mode='left_to_right')
    pid: str | Any = Field(default=None, union_mode='left_to_right')
    streaming_url: str | Any = Field(None, alias='streamingUrl', union_mode='left_to_right')
    brand_slug: str | Any = Field(None, alias='brandSlug', union_mode='left_to_right')

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    series_title: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    default_title: str | Any = Field(None, alias='defaultTitle', union_mode='left_to_right')
    content_id: str | Any = Field(default=None, union_mode='left_to_right')
    airdate: str | Any = Field(default=None, union_mode='left_to_right')
    airdate_ts: int | Any = Field(default=None, union_mode='left_to_right')
    airdate_iso: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    expiredate_raw: str | Any = Field(default=None, union_mode='left_to_right')
    season_number: str | Any = Field(default=None, union_mode='left_to_right')
    episode_number: str | Any = Field(default=None, union_mode='left_to_right')
    duration: str | Any = Field(default=None, union_mode='left_to_right')
    duration_raw: int | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    regional_ratings: RegionalRatings | Any = Field(None, alias='regionalRatings', union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    short_description: str | Any = Field(None, alias='shortDescription', union_mode='left_to_right')
    thumb: Thumb | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    app_url: str | Any = Field(default=None, union_mode='left_to_right')
    amazon_est_url: str | Any = Field(default=None, union_mode='left_to_right')
    itunes_est_url: str | Any = Field(default=None, union_mode='left_to_right')
    streaming_url: str | Any = Field(default=None, union_mode='left_to_right')
    live_streaming_url: str | Any = Field(default=None, union_mode='left_to_right')
    tms_program_id: str | Any = Field(default=None, union_mode='left_to_right')
    show_id: Any | None = None
    asset_type: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    expiry_date: str | Any = Field(default=None, union_mode='left_to_right')
    is_paid_content: bool | Any = Field(default=None, union_mode='left_to_right')
    ios_available_status: str | Any = Field(default=None, union_mode='left_to_right')
    ios_available_date: str | Any = Field(default=None, union_mode='left_to_right')
    android_available_status: str | Any = Field(default=None, union_mode='left_to_right')
    android_available_date: str | Any = Field(default=None, union_mode='left_to_right')
    tracking_media_id: Any | None = None
    signature: Any | None = None
    media_type: Any | None = None
    vtag: Any | None = None
    is_live: bool | Any = Field(default=None, union_mode='left_to_right')
    med_time: int | Any = Field(None, alias='medTime', union_mode='left_to_right')
    genre: str | Any = Field(default=None, union_mode='left_to_right')
    meta_data: MetaData | Any = Field(None, alias='metaData', union_mode='left_to_right')
    brand: str | Any = Field(default=None, union_mode='left_to_right')
    video_properties: list[str] | Any = Field(None, alias='videoProperties', union_mode='left_to_right')
    available_for_profile_types: list[str] | Any = Field(None, alias='availableForProfileTypes', union_mode='left_to_right')
    primary_category_name: str | Any = Field(None, alias='primaryCategoryName', union_mode='left_to_right')
    playback_events: Any | None = Field(None, alias='playbackEvents')
    cast: Any | None = None
    show_assets: Any | None = Field(None, alias='showAssets')
    movie_assets: Any | None = Field(None, alias='movieAssets')
    channel_name: Any | None = Field(None, alias='channelName')
    is_content_accessible_in_can: bool | Any = Field(None, alias='isContentAccessibleInCAN', union_mode='left_to_right')
    api_metadata: ApiMetadata | Any = Field(None, alias='apiMetadata', union_mode='left_to_right')
    media_content_type: str | Any = Field(default=None, union_mode='left_to_right')
    mpd_url: Any | None = None
    license_url: Any | None = None
    closed_captions: Any | None = None
    position_num: int | Any = Field(None, alias='positionNum', union_mode='left_to_right')
    is_protected: bool | Any = Field(default=None, union_mode='left_to_right')
    drm: bool | Any = Field(default=None, union_mode='left_to_right')
    raw_url: str | Any = Field(default=None, union_mode='left_to_right')
    episode_title: str | Any = Field(default=None, union_mode='left_to_right')
    video_preview_url: str | Any = Field(None, alias='videoPreviewURL', union_mode='left_to_right')
    feature: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    pubdate_iso: Any | None = None
    content_locked: str | Any = Field(None, alias='contentLocked', union_mode='left_to_right')
    play_icon: str | Any = Field(None, alias='playIcon', union_mode='left_to_right')
    thumb_url: str | Any = Field(None, alias='thumbUrl', union_mode='left_to_right')
    season_title: str | Any = Field(None, alias='seasonTitle', union_mode='left_to_right')
    season_abbr: str | Any = Field(None, alias='seasonAbbr', union_mode='left_to_right')
    episode_abbr: str | Any = Field(None, alias='episodeAbbr', union_mode='left_to_right')
    episode_number_title: str | Any = Field(None, alias='episodeNumberTitle', union_mode='left_to_right')
    label_subscribe: str | Any = Field(None, alias='labelSubscribe', union_mode='left_to_right')
    rating_text: str | Any = Field(None, alias='ratingText', union_mode='left_to_right')
    rating_icon: Any | None = Field(None, alias='ratingIcon')
    is_user_subscriber: bool | Any = Field(None, alias='isUserSubscriber', union_mode='left_to_right')
    aa_link: str | Any = Field(None, alias='aaLink', union_mode='left_to_right')
    data_tracking: str | Any = Field(None, alias='dataTracking', union_mode='left_to_right')
    display_title: str | Any = Field(None, alias='displayTitle', union_mode='left_to_right')
    display_description: str | Any = Field(None, alias='displayDescription', union_mode='left_to_right')
    lock_level: str | Any = Field(None, alias='lockLevel', union_mode='left_to_right')

class EpisodesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    data: list[Datum] | Any = Field(default=None, union_mode='left_to_right')
    total: int | Any = Field(default=None, union_mode='left_to_right')
    display_seasons: bool | Any = Field(default=None, union_mode='left_to_right')
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

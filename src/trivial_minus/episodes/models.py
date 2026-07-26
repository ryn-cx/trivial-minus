from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field
from typing import Any

class Subrating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    code: str
    description: str

class RegionalRatings(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    region: str
    rating: str
    disclaimer: None
    secondary_descriptors: str | None = Field(..., alias='secondaryDescriptors')
    subratings: list[Subrating]
    consumer_advice: None = Field(..., alias='consumerAdvice')
    rating_icon: None = Field(..., alias='ratingIcon')

class Thumb(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    large: str
    small: str
    field_640x360: str = Field(..., alias='640x360')
    field_640x480: str = Field(..., alias='640x480')
    field_1400x2100: str = Field(..., alias='1400x2100')
    poster: None

class EsturLs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    amazon: str
    i_tunes: str = Field(..., alias='iTunes')

class RegionalRating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    region: str
    rating: str
    disclaimer: None
    secondary_descriptors: str | None = Field(..., alias='secondaryDescriptors')
    subratings: list[Subrating]
    consumer_advice: None = Field(..., alias='consumerAdvice')
    rating_icon: None = Field(..., alias='ratingIcon')

class MetaData(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    airdate_iso: AwareDatetime
    airdate_tv: bool
    asset_type: str = Field(..., alias='assetType')
    brand: str
    media_type: None = Field(..., alias='mediaType')
    channel_name: None = Field(..., alias='channelName')
    content_id: str = Field(..., alias='contentId')
    content_url: str = Field(..., alias='contentUrl')
    end_credits_chapter_time: None = Field(..., alias='endCreditsChapterTime')
    episode_number: str = Field(..., alias='episodeNumber')
    estur_ls: EsturLs = Field(..., alias='ESTURLs')
    exclude_oztam: None = Field(..., alias='excludeOztam')
    full_episode: bool = Field(..., alias='fullEpisode')
    is_service_allowed: bool = Field(..., alias='isServiceAllowed')
    oztam_media_id: None = Field(..., alias='oztamMediaId')
    pid: None
    daistream_key: None = Field(..., alias='daistreamKey')
    preview_image_url: None = Field(..., alias='previewImageURL')
    rating: str
    regional_ratings: list[RegionalRating] = Field(..., alias='regionalRatings')
    season_number: str = Field(..., alias='seasonNumber')
    series_title: str = Field(..., alias='seriesTitle')
    show_page_url: str = Field(..., alias='showPageURL')
    subscription_level: str = Field(..., alias='subscriptionLevel')
    thumbnail: None
    thumbnail_sheet: None = Field(..., alias='thumbnailSheet')
    tv_rating_flag: bool = Field(..., alias='tvRatingFlag')
    video_length: int = Field(..., alias='videoLength')
    video_page_url: str = Field(..., alias='videoPageURL')
    video_title: str = Field(..., alias='videoTitle')
    label: str
    video_properties: list[str] = Field(..., alias='videoProperties')
    playback_events: None = Field(..., alias='playbackEvents')
    browser_version: str = Field(..., alias='browserVersion')
    current_listing_title: None = Field(..., alias='currentListingTitle')

class ThumbnailSetItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    height: int
    width: int
    asset_type: str = Field(..., alias='assetType')
    url: str

class RegionalRating1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    region: str
    rating: str
    disclaimer: None
    secondary_descriptors: str | None = Field(..., alias='secondaryDescriptors')
    subratings: list[Subrating]
    consumer_advice: None = Field(..., alias='consumerAdvice')
    rating_icon: None = Field(..., alias='ratingIcon')

class ApiMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    genre: str
    status: str
    show_page_url: str = Field(..., alias='showPageUrl')
    air_date: int = Field(..., alias='airDate')
    description: str
    short_description: str = Field(..., alias='shortDescription')
    label: str
    full_episode: bool = Field(..., alias='fullEpisode')
    content_id: str = Field(..., alias='contentId')
    title: str
    episode_num: str = Field(..., alias='episodeNum')
    season_num: str = Field(..., alias='seasonNum')
    brand: str
    series_title: str = Field(..., alias='seriesTitle')
    field_air_date: str = Field(..., alias='_airDate')
    duration: int
    rating: str
    expiration_date: int = Field(..., alias='expirationDate')
    field_expiration_date: str = Field(..., alias='_expirationDate')
    field_air_date_iso: AwareDatetime = Field(..., alias='_airDateISO')
    subscription_level: str = Field(..., alias='subscriptionLevel')
    media_available_date: AwareDatetime = Field(..., alias='mediaAvailableDate')
    media_available_date_epoch: int = Field(..., alias='mediaAvailableDateEpoch')
    is_live: bool = Field(..., alias='isLive')
    is_protected: bool = Field(..., alias='isProtected')
    thumbnail_set: list[ThumbnailSetItem] = Field(..., alias='thumbnailSet')
    download_country_set: list[None] = Field(..., alias='downloadCountrySet')
    regional_ratings: list[RegionalRating1] = Field(..., alias='regionalRatings')
    video_properties: list[str] = Field(..., alias='videoProperties')
    available_for_profile_types: list[str] = Field(..., alias='availableForProfileTypes')
    copyright: str
    add_ons: list[None] = Field(..., alias='addOns')
    brand_slug: str = Field(..., alias='brandSlug')
    original_release_year: int = Field(..., alias='originalReleaseYear')
    is_content_accessible_in_can: bool = Field(..., alias='isContentAccessibleInCAN')
    thumbnail_sheet_set: list[None] = Field(..., alias='thumbnailSheetSet')
    is_product_placement: bool = Field(..., alias='isProductPlacement')
    video_title: str = Field(..., alias='videoTitle')

class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    title: str
    series_title: str
    label: str
    content_id: str
    airdate: str
    airdate_ts: int
    airdate_iso: AwareDatetime
    expiredate_raw: str
    season_number: str
    episode_number: str
    duration: str
    duration_raw: int
    rating: str
    regional_ratings: RegionalRatings = Field(..., alias='regionalRatings')
    description: str
    short_description: str = Field(..., alias='shortDescription')
    thumb: Thumb
    url: str
    app_url: str
    amazon_est_url: str
    itunes_est_url: str
    streaming_url: str
    live_streaming_url: str
    tms_program_id: str
    show_id: None
    asset_type: str
    status: str
    expiry_date: str
    is_paid_content: bool
    ios_available_status: str
    ios_available_date: str
    android_available_status: str
    android_available_date: str
    tracking_media_id: None
    signature: None
    media_type: None
    vtag: None
    is_live: bool
    med_time: int = Field(..., alias='medTime')
    genre: str
    meta_data: MetaData = Field(..., alias='metaData')
    brand: str
    video_properties: list[str] = Field(..., alias='videoProperties')
    available_for_profile_types: list[str] = Field(..., alias='availableForProfileTypes')
    primary_category_name: str = Field(..., alias='primaryCategoryName')
    playback_events: None = Field(..., alias='playbackEvents')
    cast: None
    show_assets: None = Field(..., alias='showAssets')
    movie_assets: None = Field(..., alias='movieAssets')
    channel_name: None = Field(..., alias='channelName')
    is_content_accessible_in_can: bool = Field(..., alias='isContentAccessibleInCAN')
    api_metadata: ApiMetadata = Field(..., alias='apiMetadata')
    media_content_type: str
    mpd_url: None
    license_url: None
    closed_captions: None
    position_num: int = Field(..., alias='positionNum')
    is_protected: bool
    drm: bool
    raw_url: str
    episode_title: str
    video_preview_url: str = Field(..., alias='videoPreviewURL')
    feature: AwareDatetime
    pubdate_iso: None
    content_locked: str = Field(..., alias='contentLocked')
    play_icon: str = Field(..., alias='playIcon')
    thumb_url: str = Field(..., alias='thumbUrl')
    season_title: str = Field(..., alias='seasonTitle')
    season_abbr: str = Field(..., alias='seasonAbbr')
    episode_abbr: str = Field(..., alias='episodeAbbr')
    episode_number_title: str = Field(..., alias='episodeNumberTitle')
    label_subscribe: str = Field(..., alias='labelSubscribe')
    rating_text: str = Field(..., alias='ratingText')
    rating_icon: None = Field(..., alias='ratingIcon')
    is_user_subscriber: bool = Field(..., alias='isUserSubscriber')
    aa_link: str = Field(..., alias='aaLink')
    data_tracking: str = Field(..., alias='dataTracking')
    display_title: str = Field(..., alias='displayTitle')
    display_description: str = Field(..., alias='displayDescription')
    lock_level: str = Field(..., alias='lockLevel')

class Result(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    data: list[Datum]
    total: int

class EpisodesModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    result: Result
    success: bool

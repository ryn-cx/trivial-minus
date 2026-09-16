from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import time
from typing import Any
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, Field, NaiveDatetime

class AvailableVideoSeason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    season_num: str = Field(..., alias='seasonNum')
    total_count: int = Field(..., alias='totalCount')
    premium_count: int = Field(..., alias='premiumCount')
    clips_count: int = Field(..., alias='clipsCount')
    delay_count: int = Field(..., alias='delayCount')
    season_premiere_date: None = Field(..., alias='seasonPremiereDate')
    season_premiere_date_epoch: None = Field(..., alias='seasonPremiereDateEpoch')
    season_finale_date: None = Field(..., alias='seasonFinaleDate')
    season_finale_date_epoch: None = Field(..., alias='seasonFinaleDateEpoch')

class ShowAssets(BaseModel):
    model_config = ConfigDict(defer_build=True)
    filepath_apple_airplay: str
    filepath_mobile_endcard: str
    filepath_show_page_header: str
    filepath_title_logo_regular: str
    filepath_video_endcard_show_image: str
    filepath_title_logo_left: str
    filepath_title_logo_center: str
    filepath_apple_centered_background: str
    filepath_show_hero_landscape: str | None = None
    filepath_ott_hd_show_image_overhang: str
    filepath_apple_content_logo_polychromatic: str
    filepath_show_browse_poster: str
    filepath_show_hero_regular: str
    filepath_show_hero_compact: str
    filepath_show_hero_portrait: str | None = None
    filepath_apple_cover_artwork_horizontal: str
    filepath_title_logo_compact: str
    filepath_apple_content_logo_monochromatic: str
    filepath_apple_centered_background_small: str
    filepath_apple_top_shelf: str
    filepath_show_poster: str | None = None
    filepath_partner_brand_logo: str | None = None
    filepath_brand_hero: str | None = None

class ThumbnailSetItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    height: int
    width: int
    asset_type: str = Field(..., alias='assetType')
    url: str

class DownloadCountrySetItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: str
    downloadable: bool

class RegionalRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    region: str
    rating: str
    disclaimer: None
    secondary_descriptors: None = Field(..., alias='secondaryDescriptors')
    subratings: None
    consumer_advice: None = Field(..., alias='consumerAdvice')
    rating_icon: None = Field(..., alias='ratingIcon')

class PlaybackEvents(BaseModel):
    model_config = ConfigDict(defer_build=True)
    end_credit_chapter_time_ms: int = Field(..., alias='endCreditChapterTimeMs')
    preview_start_time_ms: None = Field(..., alias='previewStartTimeMs')
    preview_end_time_ms: None = Field(..., alias='previewEndTimeMs')
    open_credit_end_time_ms: None = Field(..., alias='openCreditEndTimeMs')
    open_credit_start_time: None = Field(..., alias='openCreditStartTime')

class ThumbnailSheetSetItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    height: int
    width: int
    asset_type: str = Field(..., alias='assetType')
    url: str

class MovieContent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    genre: str
    status: str
    field_first_ingest_date: str = Field(..., alias='_firstIngestDate')
    expired: bool
    show_page_url: str = Field(..., alias='showPageUrl')
    cbs_show_id: int = Field(..., alias='cbsShowId')
    primary_category: str = Field(..., alias='primaryCategory')
    primary_category_name: str = Field(..., alias='primaryCategoryName')
    edit_date: int = Field(..., alias='editDate')
    field_edit_date: str = Field(..., alias='_editDate')
    field_last_modified_date: str = Field(..., alias='_lastModifiedDate')
    ingest_date: int = Field(..., alias='ingestDate')
    air_date: int = Field(..., alias='airDate')
    description: str
    short_description: str = Field(..., alias='shortDescription')
    pub_date: int = Field(..., alias='pubDate')
    label: str
    url: str
    asset_type: str = Field(..., alias='assetType')
    first_ingest_date: int = Field(..., alias='firstIngestDate')
    category: str
    top_level_category: str = Field(..., alias='topLevelCategory')
    full_episode: bool = Field(..., alias='fullEpisode')
    exclusive: bool
    content_id: str = Field(..., alias='contentId')
    title: str
    field_ingest_date: str = Field(..., alias='_ingestDate')
    episode_num: str = Field(..., alias='episodeNum')
    field_pub_date: str = Field(..., alias='_pubDate')
    season_num: str = Field(..., alias='seasonNum')
    brand: str
    child_content_id: str = Field(..., alias='childContentId')
    sizzle_id: str = Field(..., alias='sizzleId')
    series_title: str = Field(..., alias='seriesTitle')
    field_air_date: str = Field(..., alias='_airDate')
    duration: int
    last_modified_date: int = Field(..., alias='lastModifiedDate')
    rating: str
    device_type: str = Field(..., alias='deviceType')
    thumbnail: str
    amazon_esturl: str = Field(..., alias='amazonESTURL')
    itunes_esturl: str = Field(..., alias='itunesESTURL')
    expiration_date: int = Field(..., alias='expirationDate')
    field_expiration_date: str = Field(..., alias='_expirationDate')
    field_pub_date_iso: AwareDatetime = Field(..., alias='_pubDateISO')
    field_air_date_iso: AwareDatetime = Field(..., alias='_airDateISO')
    subscription_level: str = Field(..., alias='subscriptionLevel')
    media_available_date: AwareDatetime = Field(..., alias='mediaAvailableDate')
    media_available_date_epoch: int = Field(..., alias='mediaAvailableDateEpoch')
    is_live: bool = Field(..., alias='isLive')
    cms_account_id: str = Field(..., alias='cmsAccountId')
    apple_watch_list_show_key: str = Field(..., alias='appleWatchListShowKey')
    is_protected: bool = Field(..., alias='isProtected')
    media_type: str = Field(..., alias='mediaType')
    exclude_nielsen_tracking: bool = Field(..., alias='excludeNielsenTracking')
    end_credits_chapter_time: time = Field(..., alias='endCreditsChapterTime')
    thumbnail_set: list[ThumbnailSetItem] = Field(..., alias='thumbnailSet')
    download_country_set: list[DownloadCountrySetItem] = Field(..., alias='downloadCountrySet')
    regional_ratings: list[RegionalRating] = Field(..., alias='regionalRatings')
    premium_features: list[str] = Field(..., alias='premiumFeatures')
    video_properties: list[str] = Field(..., alias='videoProperties')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    external_id: str = Field(..., alias='externalId')
    available_for_profile_types: list[str] = Field(..., alias='availableForProfileTypes')
    playback_events: PlaybackEvents = Field(..., alias='playbackEvents')
    embeddable: str
    copyright: str
    add_ons: list[None] = Field(..., alias='addOns')
    regional_audio_exclude_languages: list[None] = Field(..., alias='regionalAudioExcludeLanguages')
    regional_text_exclude_languages: list[None] = Field(..., alias='regionalTextExcludeLanguages')
    original_release_year: int = Field(..., alias='originalReleaseYear')
    tmsseries_id: str = Field(..., alias='tmsseriesID')
    tmsprogram_id: str = Field(..., alias='tmsprogramID')
    is_content_accessible_in_can: bool = Field(..., alias='isContentAccessibleInCAN')
    thumbnail_sheet_set: list[ThumbnailSheetSetItem] = Field(..., alias='thumbnailSheetSet')
    v_tag: str = Field(..., alias='vTag')
    is_product_placement: bool = Field(..., alias='isProductPlacement')

class PlaybackEvents1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    end_credit_chapter_time_ms: None = Field(..., alias='endCreditChapterTimeMs')
    preview_start_time_ms: None = Field(..., alias='previewStartTimeMs')
    preview_end_time_ms: None = Field(..., alias='previewEndTimeMs')
    open_credit_end_time_ms: None = Field(..., alias='openCreditEndTimeMs')
    open_credit_start_time: None = Field(..., alias='openCreditStartTime')

class TrailerContent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    genre: str
    status: str
    field_first_ingest_date: str = Field(..., alias='_firstIngestDate')
    expired: bool
    show_page_url: str = Field(..., alias='showPageUrl')
    cbs_show_id: int = Field(..., alias='cbsShowId')
    primary_category: str = Field(..., alias='primaryCategory')
    primary_category_name: str = Field(..., alias='primaryCategoryName')
    edit_date: int = Field(..., alias='editDate')
    field_edit_date: str = Field(..., alias='_editDate')
    field_last_modified_date: str = Field(..., alias='_lastModifiedDate')
    ingest_date: int = Field(..., alias='ingestDate')
    air_date: int = Field(..., alias='airDate')
    description: str
    short_description: str = Field(..., alias='shortDescription')
    pub_date: int = Field(..., alias='pubDate')
    label: str
    video_page_url: str = Field(..., alias='videoPageUrl')
    url: str
    asset_type: str = Field(..., alias='assetType')
    first_ingest_date: int = Field(..., alias='firstIngestDate')
    category: str
    top_level_category: str = Field(..., alias='topLevelCategory')
    full_episode: bool = Field(..., alias='fullEpisode')
    exclusive: bool
    content_id: str = Field(..., alias='contentId')
    title: str
    field_ingest_date: str = Field(..., alias='_ingestDate')
    episode_num: str = Field(..., alias='episodeNum')
    field_pub_date: str = Field(..., alias='_pubDate')
    season_num: str = Field(..., alias='seasonNum')
    brand: str
    child_content_id: str = Field(..., alias='childContentId')
    sizzle_id: str = Field(..., alias='sizzleId')
    pid: UUID | str = Field(union_mode='left_to_right')
    series_title: str = Field(..., alias='seriesTitle')
    field_air_date: str = Field(..., alias='_airDate')
    duration: int
    last_modified_date: int = Field(..., alias='lastModifiedDate')
    rating: str
    device_type: str = Field(..., alias='deviceType')
    thumbnail: str
    amazon_esturl: str = Field(..., alias='amazonESTURL')
    itunes_esturl: str = Field(..., alias='itunesESTURL')
    streaming_url: str = Field(..., alias='streamingUrl')
    expiration_date: int = Field(..., alias='expirationDate')
    field_expiration_date: str = Field(..., alias='_expirationDate')
    field_pub_date_iso: AwareDatetime = Field(..., alias='_pubDateISO')
    field_air_date_iso: AwareDatetime = Field(..., alias='_airDateISO')
    player_loc_url: str = Field(..., alias='playerLocUrl')
    subscription_level: str = Field(..., alias='subscriptionLevel')
    media_available_date: AwareDatetime = Field(..., alias='mediaAvailableDate')
    media_available_date_epoch: int = Field(..., alias='mediaAvailableDateEpoch')
    closed_caption_url: str = Field(..., alias='closedCaptionUrl')
    is_live: bool = Field(..., alias='isLive')
    cms_account_id: str = Field(..., alias='cmsAccountId')
    apple_watch_list_show_key: str = Field(..., alias='appleWatchListShowKey')
    is_protected: bool = Field(..., alias='isProtected')
    media_type: str = Field(..., alias='mediaType')
    exclude_nielsen_tracking: bool = Field(..., alias='excludeNielsenTracking')
    end_credits_chapter_time: str = Field(..., alias='endCreditsChapterTime')
    thumbnail_set: list[ThumbnailSetItem] = Field(..., alias='thumbnailSet')
    download_country_set: list[None] = Field(..., alias='downloadCountrySet')
    regional_ratings: list[RegionalRating] = Field(..., alias='regionalRatings')
    premium_features: list[str] = Field(..., alias='premiumFeatures')
    video_properties: list[str] = Field(..., alias='videoProperties')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    external_id: str = Field(..., alias='externalId')
    available_for_profile_types: list[str] = Field(..., alias='availableForProfileTypes')
    playback_events: PlaybackEvents1 = Field(..., alias='playbackEvents')
    embeddable: str
    copyright: str
    add_ons: list[None] = Field(..., alias='addOns')
    regional_audio_exclude_languages: list[None] = Field(..., alias='regionalAudioExcludeLanguages')
    regional_text_exclude_languages: list[None] = Field(..., alias='regionalTextExcludeLanguages')
    original_release_year: int = Field(..., alias='originalReleaseYear')
    tmsseries_id: str = Field(..., alias='tmsseriesID')
    tmsprogram_id: str = Field(..., alias='tmsprogramID')
    is_content_accessible_in_can: bool = Field(..., alias='isContentAccessibleInCAN')
    thumbnail_sheet_set: list[ThumbnailSheetSetItem] = Field(..., alias='thumbnailSheetSet')
    v_tag: str = Field(..., alias='vTag')
    is_product_placement: bool = Field(..., alias='isProductPlacement')

class MovieAssets(BaseModel):
    model_config = ConfigDict(defer_build=True)
    filepath_movie_keep_watching: str
    filepath_movie_poster: str
    filepath_title_logo_regular: str
    filepath_movie_logo: str
    filepath_movie_hero_regular: str
    filepath_movie_hero: str
    filepath_title_logo_left: str
    filepath_partner_movie_poster: str
    filepath_movie_hero_compact: str
    filepath_title_logo_center: str
    filepath_title_logo_compact: str

class Content(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hub_id: int | None = Field(None, alias='hubId')
    title: str | None = None
    hub_slug: str | None = Field(None, alias='hubSlug')
    type: str | None = None
    hub_items: None = Field(None, alias='hubItems')
    page_type: str | None = Field(None, alias='pageType')
    region: str | None = None
    locale: str | None = None
    user_state: list[str] | None = Field(None, alias='userState')
    live_on_date: int | None = Field(None, alias='liveOnDate')
    variant_key: None = Field(None, alias='variantKey')
    show_id: int | None = Field(None, alias='showId')
    about: str | None = None
    show_title: str | None = Field(None, alias='showTitle')
    content_type: str | None = Field(None, alias='contentType')
    show_path: str | None = Field(None, alias='showPath')
    tune_in_time: str | None = Field(None, alias='tuneInTime')
    premium_features: list[None] | None = Field(None, alias='premiumFeatures')
    category: str | None = None
    available_video_seasons: list[AvailableVideoSeason] | None = Field(None, alias='availableVideoSeasons')
    show_assets: ShowAssets | None = Field(None, alias='showAssets')
    callbacks: dict[str, Any] | None = None
    rating: str | list[str] | None = None
    is_content_accessible_in_cms: bool | None = Field(None, alias='isContentAccessibleInCMS')
    required_add_ons: list[None] | None = Field(None, alias='requiredAddOns')
    is_after_hours: bool | None = Field(None, alias='isAfterHours')
    is_kids_content: bool | None = Field(None, alias='isKidsContent')
    cast_names: list[str] | None = Field(None, alias='castNames')
    sub_video_starting_point_cta: str | None = Field(None, alias='subVideoStartingPointCTA')
    genre: str | None = None
    unified_genre: list[str] | None = Field(None, alias='unifiedGenre')
    video_preview_url: str | None = Field(None, alias='videoPreviewURL')
    id: int | None = None
    content_id: str | None = Field(None, alias='contentId')
    trailer_content_id: str | None = Field(None, alias='trailerContentId')
    movie_content: MovieContent | None = Field(None, alias='movieContent')
    trailer_content: TrailerContent | None = Field(None, alias='trailerContent')
    movie_assets: MovieAssets | None = Field(None, alias='movieAssets')
    is_movie_available: bool | None = Field(None, alias='isMovieAvailable')
    first_available_date: AwareDatetime | None = Field(None, alias='firstAvailableDate')
    league_id: int | None = Field(None, alias='leagueId')
    brand_slug: str | None = Field(None, alias='brandSlug')
    show_premiere_date_str: NaiveDatetime | None = Field(None, alias='showPremiereDateStr')

class ItemPem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    pvr_model: str = Field(..., alias='pvrModel')
    draw_id: UUID = Field(..., alias='drawId')
    arm_id: UUID | None = Field(None, alias='armId')
    p: str | None = None
    mab_id: str | None = Field(None, alias='mabId')

class WatchListCtaContent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_id: int | str
    content_type: str
    title: str
    series_title: str
    genre: str

class Subrating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: str
    description: str

class RegionalRating2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    region: str
    rating: str
    disclaimer: None
    secondary_descriptors: str | None = Field(..., alias='secondaryDescriptors')
    subratings: list[Subrating] | None
    consumer_advice: None = Field(..., alias='consumerAdvice')
    rating_icon: None = Field(..., alias='ratingIcon')

class PlaybackEvents2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    end_credit_chapter_time_ms: int = Field(..., alias='endCreditChapterTimeMs')
    preview_start_time_ms: None = Field(..., alias='previewStartTimeMs')
    preview_end_time_ms: None = Field(..., alias='previewEndTimeMs')
    open_credit_end_time_ms: None = Field(..., alias='openCreditEndTimeMs')
    open_credit_start_time: None = Field(..., alias='openCreditStartTime')

class MovieContent1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    genre: str
    status: str
    field_first_ingest_date: str = Field(..., alias='_firstIngestDate')
    expired: bool
    show_page_url: str = Field(..., alias='showPageUrl')
    cbs_show_id: int = Field(..., alias='cbsShowId')
    primary_category: str = Field(..., alias='primaryCategory')
    primary_category_name: str = Field(..., alias='primaryCategoryName')
    edit_date: int = Field(..., alias='editDate')
    field_edit_date: str = Field(..., alias='_editDate')
    field_last_modified_date: str = Field(..., alias='_lastModifiedDate')
    ingest_date: int = Field(..., alias='ingestDate')
    air_date: int = Field(..., alias='airDate')
    description: str
    short_description: str = Field(..., alias='shortDescription')
    pub_date: int = Field(..., alias='pubDate')
    label: str
    url: str
    asset_type: str = Field(..., alias='assetType')
    first_ingest_date: int = Field(..., alias='firstIngestDate')
    category: str
    top_level_category: str = Field(..., alias='topLevelCategory')
    full_episode: bool = Field(..., alias='fullEpisode')
    exclusive: bool
    content_id: str = Field(..., alias='contentId')
    title: str
    field_ingest_date: str = Field(..., alias='_ingestDate')
    episode_num: str = Field(..., alias='episodeNum')
    field_pub_date: str = Field(..., alias='_pubDate')
    season_num: str = Field(..., alias='seasonNum')
    brand: str
    child_content_id: str = Field(..., alias='childContentId')
    sizzle_id: str = Field(..., alias='sizzleId')
    series_title: str = Field(..., alias='seriesTitle')
    field_air_date: str = Field(..., alias='_airDate')
    duration: int
    last_modified_date: int = Field(..., alias='lastModifiedDate')
    rating: str
    device_type: str = Field(..., alias='deviceType')
    thumbnail: str
    amazon_esturl: str = Field(..., alias='amazonESTURL')
    itunes_esturl: str = Field(..., alias='itunesESTURL')
    expiration_date: int = Field(..., alias='expirationDate')
    field_expiration_date: str = Field(..., alias='_expirationDate')
    field_pub_date_iso: AwareDatetime = Field(..., alias='_pubDateISO')
    field_air_date_iso: AwareDatetime = Field(..., alias='_airDateISO')
    subscription_level: str = Field(..., alias='subscriptionLevel')
    media_available_date: AwareDatetime = Field(..., alias='mediaAvailableDate')
    media_available_date_epoch: int = Field(..., alias='mediaAvailableDateEpoch')
    is_live: bool = Field(..., alias='isLive')
    cms_account_id: str = Field(..., alias='cmsAccountId')
    apple_watch_list_show_key: str = Field(..., alias='appleWatchListShowKey')
    is_protected: bool = Field(..., alias='isProtected')
    media_type: str = Field(..., alias='mediaType')
    exclude_nielsen_tracking: bool = Field(..., alias='excludeNielsenTracking')
    end_credits_chapter_time: time = Field(..., alias='endCreditsChapterTime')
    thumbnail_set: list[ThumbnailSetItem] = Field(..., alias='thumbnailSet')
    download_country_set: list[DownloadCountrySetItem] = Field(..., alias='downloadCountrySet')
    regional_ratings: list[RegionalRating2] = Field(..., alias='regionalRatings')
    premium_features: list[str] = Field(..., alias='premiumFeatures')
    video_properties: list[str] = Field(..., alias='videoProperties')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    external_id: str | None = Field(None, alias='externalId')
    available_for_profile_types: list[str] = Field(..., alias='availableForProfileTypes')
    playback_events: PlaybackEvents2 = Field(..., alias='playbackEvents')
    embeddable: str
    copyright: str
    add_ons: list[str] = Field(..., alias='addOns')
    regional_audio_exclude_languages: list[None] = Field(..., alias='regionalAudioExcludeLanguages')
    regional_text_exclude_languages: list[None] = Field(..., alias='regionalTextExcludeLanguages')
    original_release_year: int = Field(..., alias='originalReleaseYear')
    tmsseries_id: str = Field(..., alias='tmsseriesID')
    tmsprogram_id: str = Field(..., alias='tmsprogramID')
    is_content_accessible_in_can: bool = Field(..., alias='isContentAccessibleInCAN')
    thumbnail_sheet_set: list[ThumbnailSheetSetItem] = Field(..., alias='thumbnailSheetSet')
    v_tag: str = Field(..., alias='vTag')
    is_product_placement: bool = Field(..., alias='isProductPlacement')
    brand_slug: str = Field(..., alias='brandSlug')
    is_movie_available: bool = Field(..., alias='isMovieAvailable')

class RegionalRating3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    region: str
    rating: str
    disclaimer: None
    secondary_descriptors: str | None = Field(..., alias='secondaryDescriptors')
    subratings: list[Subrating] | None
    consumer_advice: None = Field(..., alias='consumerAdvice')
    rating_icon: None = Field(..., alias='ratingIcon')

class PlaybackEvents3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    end_credit_chapter_time_ms: None = Field(..., alias='endCreditChapterTimeMs')
    preview_start_time_ms: None = Field(..., alias='previewStartTimeMs')
    preview_end_time_ms: None = Field(..., alias='previewEndTimeMs')
    open_credit_end_time_ms: None = Field(..., alias='openCreditEndTimeMs')
    open_credit_start_time: None = Field(..., alias='openCreditStartTime')

class TrailerContent1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    genre: str
    status: str
    field_first_ingest_date: str = Field(..., alias='_firstIngestDate')
    expired: bool
    show_page_url: str = Field(..., alias='showPageUrl')
    cbs_show_id: int = Field(..., alias='cbsShowId')
    primary_category: str = Field(..., alias='primaryCategory')
    primary_category_name: str = Field(..., alias='primaryCategoryName')
    edit_date: int = Field(..., alias='editDate')
    field_edit_date: str = Field(..., alias='_editDate')
    field_last_modified_date: str = Field(..., alias='_lastModifiedDate')
    ingest_date: int = Field(..., alias='ingestDate')
    air_date: int = Field(..., alias='airDate')
    description: str
    short_description: str = Field(..., alias='shortDescription')
    pub_date: int = Field(..., alias='pubDate')
    label: str
    video_page_url: str = Field(..., alias='videoPageUrl')
    url: str
    asset_type: str = Field(..., alias='assetType')
    first_ingest_date: int = Field(..., alias='firstIngestDate')
    category: str
    top_level_category: str = Field(..., alias='topLevelCategory')
    full_episode: bool = Field(..., alias='fullEpisode')
    exclusive: bool
    content_id: str = Field(..., alias='contentId')
    title: str
    field_ingest_date: str = Field(..., alias='_ingestDate')
    episode_num: str = Field(..., alias='episodeNum')
    field_pub_date: str = Field(..., alias='_pubDate')
    season_num: str = Field(..., alias='seasonNum')
    brand: str
    child_content_id: str = Field(..., alias='childContentId')
    sizzle_id: str = Field(..., alias='sizzleId')
    pid: UUID | str = Field(union_mode='left_to_right')
    series_title: str = Field(..., alias='seriesTitle')
    field_air_date: str = Field(..., alias='_airDate')
    duration: int
    last_modified_date: int = Field(..., alias='lastModifiedDate')
    rating: str
    device_type: str = Field(..., alias='deviceType')
    thumbnail: str
    amazon_esturl: str = Field(..., alias='amazonESTURL')
    itunes_esturl: str = Field(..., alias='itunesESTURL')
    streaming_url: str = Field(..., alias='streamingUrl')
    expiration_date: int | None = Field(None, alias='expirationDate')
    field_expiration_date: str | None = Field(None, alias='_expirationDate')
    field_pub_date_iso: AwareDatetime = Field(..., alias='_pubDateISO')
    field_air_date_iso: AwareDatetime = Field(..., alias='_airDateISO')
    player_loc_url: str = Field(..., alias='playerLocUrl')
    subscription_level: str = Field(..., alias='subscriptionLevel')
    media_available_date: AwareDatetime = Field(..., alias='mediaAvailableDate')
    media_available_date_epoch: int = Field(..., alias='mediaAvailableDateEpoch')
    closed_caption_url: str = Field(..., alias='closedCaptionUrl')
    is_live: bool = Field(..., alias='isLive')
    cms_account_id: str = Field(..., alias='cmsAccountId')
    apple_watch_list_show_key: str = Field(..., alias='appleWatchListShowKey')
    is_protected: bool = Field(..., alias='isProtected')
    media_type: str = Field(..., alias='mediaType')
    exclude_nielsen_tracking: bool = Field(..., alias='excludeNielsenTracking')
    end_credits_chapter_time: str = Field(..., alias='endCreditsChapterTime')
    thumbnail_set: list[ThumbnailSetItem] = Field(..., alias='thumbnailSet')
    download_country_set: list[DownloadCountrySetItem] = Field(..., alias='downloadCountrySet')
    regional_ratings: list[RegionalRating3] = Field(..., alias='regionalRatings')
    premium_features: list[str] = Field(..., alias='premiumFeatures')
    video_properties: list[str] = Field(..., alias='videoProperties')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    external_id: str | None = Field(None, alias='externalId')
    available_for_profile_types: list[str] = Field(..., alias='availableForProfileTypes')
    playback_events: PlaybackEvents3 = Field(..., alias='playbackEvents')
    embeddable: str
    copyright: str
    add_ons: list[str] = Field(..., alias='addOns')
    regional_audio_exclude_languages: list[None] = Field(..., alias='regionalAudioExcludeLanguages')
    regional_text_exclude_languages: list[None] = Field(..., alias='regionalTextExcludeLanguages')
    original_release_year: int = Field(..., alias='originalReleaseYear')
    tmsseries_id: str = Field(..., alias='tmsseriesID')
    tmsprogram_id: str = Field(..., alias='tmsprogramID')
    is_content_accessible_in_can: bool = Field(..., alias='isContentAccessibleInCAN')
    thumbnail_sheet_set: list[ThumbnailSheetSetItem] = Field(..., alias='thumbnailSheetSet')
    v_tag: str = Field(..., alias='vTag')
    is_product_placement: bool = Field(..., alias='isProductPlacement')
    brand_slug: str | None = Field(None, alias='brandSlug')

class AvailableVideoSeason1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    season_num: str = Field(..., alias='seasonNum')
    total_count: int = Field(..., alias='totalCount')
    premium_count: int = Field(..., alias='premiumCount')
    clips_count: int = Field(..., alias='clipsCount')
    delay_count: int = Field(..., alias='delayCount')
    season_premiere_date: str | None = Field(..., alias='seasonPremiereDate')
    season_premiere_date_epoch: int | None = Field(..., alias='seasonPremiereDateEpoch')
    season_finale_date: None = Field(..., alias='seasonFinaleDate')
    season_finale_date_epoch: None = Field(..., alias='seasonFinaleDateEpoch')

class Button(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str
    season: int | None = None
    episode: int | None = None
    url: str
    play: bool

class RegionalRating4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    region: str
    rating: str
    disclaimer: None
    secondary_descriptors: None = Field(..., alias='secondaryDescriptors')
    subratings: None
    consumer_advice: None = Field(..., alias='consumerAdvice')
    rating_icon: None = Field(..., alias='ratingIcon')

class ContentCanVideo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    genre: str
    status: str
    field_first_ingest_date: str = Field(..., alias='_firstIngestDate')
    expired: bool
    show_page_url: str = Field(..., alias='showPageUrl')
    cbs_show_id: int = Field(..., alias='cbsShowId')
    primary_category: str = Field(..., alias='primaryCategory')
    primary_category_name: str = Field(..., alias='primaryCategoryName')
    edit_date: int = Field(..., alias='editDate')
    field_edit_date: str = Field(..., alias='_editDate')
    field_last_modified_date: str = Field(..., alias='_lastModifiedDate')
    ingest_date: int = Field(..., alias='ingestDate')
    air_date: int = Field(..., alias='airDate')
    description: str
    short_description: str = Field(..., alias='shortDescription')
    pub_date: int = Field(..., alias='pubDate')
    label: str
    url: str
    asset_type: str = Field(..., alias='assetType')
    first_ingest_date: int = Field(..., alias='firstIngestDate')
    category: str
    top_level_category: str = Field(..., alias='topLevelCategory')
    full_episode: bool = Field(..., alias='fullEpisode')
    exclusive: bool
    content_id: UUID = Field(..., alias='contentId')
    title: str
    field_ingest_date: str = Field(..., alias='_ingestDate')
    episode_num: str = Field(..., alias='episodeNum')
    field_pub_date: str = Field(..., alias='_pubDate')
    season_num: str = Field(..., alias='seasonNum')
    brand: str
    child_content_id: str = Field(..., alias='childContentId')
    sizzle_id: str = Field(..., alias='sizzleId')
    series_title: str = Field(..., alias='seriesTitle')
    field_air_date: str = Field(..., alias='_airDate')
    duration: int
    last_modified_date: int = Field(..., alias='lastModifiedDate')
    rating: str
    device_type: str = Field(..., alias='deviceType')
    thumbnail: str
    amazon_esturl: str = Field(..., alias='amazonESTURL')
    itunes_esturl: str = Field(..., alias='itunesESTURL')
    expiration_date: int = Field(..., alias='expirationDate')
    field_expiration_date: str = Field(..., alias='_expirationDate')
    field_pub_date_iso: AwareDatetime = Field(..., alias='_pubDateISO')
    field_air_date_iso: AwareDatetime = Field(..., alias='_airDateISO')
    subscription_level: str = Field(..., alias='subscriptionLevel')
    media_available_date: AwareDatetime = Field(..., alias='mediaAvailableDate')
    media_available_date_epoch: int = Field(..., alias='mediaAvailableDateEpoch')
    is_live: bool = Field(..., alias='isLive')
    cms_account_id: str = Field(..., alias='cmsAccountId')
    apple_watch_list_show_key: str = Field(..., alias='appleWatchListShowKey')
    is_protected: bool = Field(..., alias='isProtected')
    media_type: str = Field(..., alias='mediaType')
    exclude_nielsen_tracking: bool = Field(..., alias='excludeNielsenTracking')
    end_credits_chapter_time: str = Field(..., alias='endCreditsChapterTime')
    thumbnail_set: list[ThumbnailSetItem] = Field(..., alias='thumbnailSet')
    download_country_set: list[None] = Field(..., alias='downloadCountrySet')
    regional_ratings: list[RegionalRating4] = Field(..., alias='regionalRatings')
    premium_features: list[str] = Field(..., alias='premiumFeatures')
    video_properties: list[str] = Field(..., alias='videoProperties')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    daistream_key: str = Field(..., alias='daistreamKey')
    playback_events: PlaybackEvents3 = Field(..., alias='playbackEvents')
    embeddable: str
    copyright: str
    add_ons: list[None] = Field(..., alias='addOns')
    regional_audio_exclude_languages: list[None] = Field(..., alias='regionalAudioExcludeLanguages')
    regional_text_exclude_languages: list[None] = Field(..., alias='regionalTextExcludeLanguages')
    original_release_year: int = Field(..., alias='originalReleaseYear')
    tmsseries_id: str = Field(..., alias='tmsseriesID')
    tmsprogram_id: str = Field(..., alias='tmsprogramID')
    is_content_accessible_in_can: bool = Field(..., alias='isContentAccessibleInCAN')
    thumbnail_sheet_set: list[None] = Field(..., alias='thumbnailSheetSet')
    v_tag: str = Field(..., alias='vTag')
    is_product_placement: bool = Field(..., alias='isProductPlacement')

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str | None = None
    description: str | None = None
    slug: str | None = None
    brand_id: str | None = Field(None, alias='brandId')
    brand_slug: str | None = Field(None, alias='brandSlug')
    page_type: str | None = Field(None, alias='pageType')
    show_path: str | None = Field(None, alias='showPath')
    movie_page_url: str | None = Field(None, alias='moviePageUrl')
    content_type: str | None = Field(None, alias='contentType')
    href: str
    thumb: str | None = None
    brand_logo: str | None = Field(None, alias='brandLogo')
    top_ten_badge: None = Field(None, alias='topTenBadge')
    action_text: str | None = Field(None, alias='actionText')
    po_copy: str | None = Field(None, alias='poCopy')
    filepath_logo_regular_image: str | None = Field(None, alias='filepathLogoRegularImage')
    logo_image: str | None = Field(None, alias='logoImage')
    background_image: str | None = Field(None, alias='backgroundImage')
    background_mobile_image: str | None = Field(None, alias='backgroundMobileImage')
    filepath_logo_compact_image: str | None = Field(None, alias='filepathLogoCompactImage')
    filepath_background_hero_image: str | None = Field(None, alias='filepathBackgroundHeroImage')
    filepath_mobile_web_image: str | None = Field(None, alias='filepathMobileWebImage')
    filepath_promo_tile_poster_image: str | None = Field(None, alias='filepathPromoTilePosterImage')
    filepath_promo_tile_landscape_image: str | None = Field(None, alias='filepathPromoTileLandscapeImage')
    content_id_impression: int | str | None = Field(None, alias='contentIdImpression')
    position: int | None = None
    rank_model: None = Field(None, alias='rankModel')
    cms_id: int | str | None = Field(None, alias='cmsId')
    content: Content | None = None
    id: int | str | None = None
    content_id: int | str | None = Field(None, alias='contentId')
    alt: str | None = None
    tune_in_time: str | None = Field(None, alias='tuneInTime')
    category: str | None = None
    is_listing_live: bool | None = Field(None, alias='isListingLive')
    show: None = Field(None)
    pvr_model: str | None = Field(None, alias='pvrModel')
    item_pem: ItemPem | None = Field(None, alias='itemPEM')
    bundle_locked: bool | None = Field(None, alias='bundleLocked')
    badge_label: bool | str | None = Field(None, alias='badgeLabel')
    aa_link: str = Field(..., alias='aaLink')
    impression: str | None = None
    promo_tile: bool | None = Field(None, alias='promoTile')
    promo_icon: str | None = Field(None, alias='promoIcon')
    cta_line1: str | None = Field(None, alias='ctaLine1')
    cta_line2: str | None = Field(None, alias='ctaLine2')
    cta_text: str | None = Field(None, alias='ctaText')
    deep_link_url: str | None = Field(None, alias='deepLinkUrl')
    hub_id: int | None = Field(None, alias='hubId')
    content_locked: int | str | None = Field(None, alias='contentLocked')
    is_user_subscriber: bool | None = Field(None, alias='isUserSubscriber')
    is_user_registered: bool | None = Field(None, alias='isUserRegistered')
    brand: str | None = None
    data_tracking: str | None = Field(None, alias='dataTracking')
    is_movie: bool | None = Field(None, alias='isMovie')
    label: str | None = None
    genre: str | None = None
    show_series_id: int | str | None = Field(None, alias='showSeriesId')
    series_id: int | str | None = Field(None, alias='seriesId')
    content_id_1: UUID | str | None = Field(None, alias='content_id', union_mode='left_to_right')
    orientation: str | None = None
    movie_id: int | str | None = Field(None, alias='movieId')
    upsell_url: str | None = Field(None, alias='upsellUrl')
    lock_icon: str | None = Field(None, alias='lockIcon')
    show_movie_id: str | None = Field(None, alias='showMovieId')
    action_url: str | None = Field(None, alias='actionUrl')
    series_title: str | None = Field(None, alias='seriesTitle')
    episode_title: str | None = Field(None, alias='episodeTitle')
    episode_id: str | None = Field(None, alias='episodeId')
    season_number: str | None = Field(None, alias='seasonNumber')
    rating: str | None = None
    rating_icon: str | None = Field(None, alias='ratingIcon')
    is_hub_carousel: bool | None = Field(None, alias='isHubCarousel')
    video_id: str | None = Field(None, alias='videoId')
    available_date: str | None = Field(None, alias='availableDate')
    show_countdown_timer: bool | None = Field(None, alias='showCountdownTimer')
    start_timestamp: int | str | None = Field(None, alias='startTimestamp')
    end_timestamp: str | None = Field(None, alias='endTimestamp')
    stream_start_timestamp: int | str | None = Field(None, alias='streamStartTimestamp')
    stream_end_timestamp: str | None = Field(None, alias='streamEndTimestamp')
    thumbnail: str | None = None
    sizzle_content_id: str | None = Field(None, alias='sizzleContentId')
    video_preview_url: str | None = Field(None, alias='videoPreviewURL')
    video_preview_id: str | None = Field(None, alias='videoPreviewId')
    show_or_movie: str | None = Field(None, alias='showOrMovie')
    notify_on: bool | None = Field(None, alias='notifyOn')
    allow_my_list_controls: bool | None = Field(None, alias='allowMyListControls')
    watch_list_cta_content: WatchListCtaContent | None = Field(None, alias='watchListCtaContent')
    cast_names: str | None = Field(None, alias='castNames')
    display_item_title: bool | None = Field(None, alias='displayItemTitle')
    is_user_kid_profile: str | None = Field(None, alias='isUserKidProfile')
    is_content_accessible_in_cms: bool | None = Field(None, alias='isContentAccessibleInCMS')
    show_title: str | None = Field(None, alias='showTitle')
    about: str | None = None
    movie_content: MovieContent1 | None = Field(None, alias='movieContent')
    trailer_content: TrailerContent1 | None = Field(None, alias='trailerContent')
    show_series_title: str | None = Field(None, alias='showSeriesTitle')
    title_slug: str | None = Field(None, alias='titleSlug')
    brand_name: str | None = Field(None, alias='brandName')
    num_seasons: int | str | None = Field(None, alias='numSeasons')
    carousel_content_type: str | None = Field(None, alias='carouselContentType')
    poster: str | None = None
    content_notification_add_action_url: str | None = Field(None, alias='contentNotificationAddActionUrl')
    content_notification_remove_action_url: str | None = Field(None, alias='contentNotificationRemoveActionUrl')
    content_my_list_add_action_url: str | None = Field(None, alias='contentMyListAddActionUrl')
    content_my_list_remove_action_url: str | None = Field(None, alias='contentMyListRemoveActionUrl')
    has_content_highlight: bool | None = Field(None, alias='hasContentHighlight')
    show_id: int | None = Field(None, alias='showId')
    carousel_type: str | None = Field(None, alias='carouselType')
    video_content_id: str | None = Field(None, alias='videoContentId')
    time_stamp: str | None = Field(None, alias='timeStamp')
    is_seasonless: bool | None = Field(None, alias='isSeasonless')
    is_episodeless: bool | None = Field(None, alias='isEpisodeless')
    season_counts: str | None = Field(None, alias='seasonCounts')
    premiere_date: str | None = Field(None, alias='premiereDate')
    available_video_seasons: list[AvailableVideoSeason1] | None = Field(None, alias='availableVideoSeasons')
    button: Button | None = None
    logo: str | None = None
    title_text: str | None = Field(None, alias='titleText')
    movie_duration: str | None = Field(None, alias='movieDuration')
    movie_rating: str | None = Field(None, alias='movieRating')
    url: str | None = None
    is_live: bool | None = Field(None, alias='isLive')
    channel_slug: str | None = Field(None, alias='channelSlug')
    stream_start_time_formatted: AwareDatetime | None = Field(None, alias='streamStartTimeFormatted')
    elapsed_time: AwareDatetime | str | None = Field(None, alias='elapsedTime', union_mode='left_to_right')
    content_can_video: ContentCanVideo | None = Field(None, alias='contentCANVideo')
    status: str | None = None
    show_id_1: int | None = Field(None, alias='show_id')
    duration: str | None = None
    schedule_badge: bool | None = Field(None, alias='scheduleBadge')
    schedule_badge_text: str | None = Field(None, alias='scheduleBadgeText')
    is_multi_channel: bool | None = Field(None, alias='isMultiChannel')
    live_badge_text: str | None = Field(None, alias='liveBadgeText')
    live_tv_channel: str | None = Field(None, alias='liveTvChannel')
    station_code: str | None = Field(None, alias='stationCode')
    stream_type: str | None = Field(None, alias='streamType')
    on_now_title: str | None = Field(None, alias='onNowTitle')
    channel_logo: str | None = Field(None, alias='channelLogo')
    multi_channel_name: str | None = Field(None, alias='multiChannelName')
    locked: bool | None = None
    local_live_tv: bool | None = Field(None, alias='localLiveTV')
    is_upcoming: bool | None = Field(None, alias='isUpcoming')
    progress: int | float | None = None
    progress_text: str | None = Field(None, alias='progressText')
    channel_name: str | None = Field(None, alias='channelName')
    filepath1x1_default_image: str | None = Field(None, alias='filepath1x1DefaultImage')
    filepath1x1_focus_state_image: str | None = Field(None, alias='filepath1x1FocusStateImage')
    movie_title: str | None = Field(None, alias='movieTitle')

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    origin_id: int = Field(..., alias='originId')
    slug: str
    channel_name: str = Field(..., alias='channelName')
    description: None
    timezone: str
    file_path_logo: str = Field(..., alias='filePathLogo')
    file_path_logo_selected: str = Field(..., alias='filePathLogoSelected')
    file_path_small_logo: str = Field(..., alias='filePathSmallLogo')
    file_path_small_logo_selected: str = Field(..., alias='filePathSmallLogoSelected')
    prg_svc_id: int = Field(..., alias='prgSvcId')
    ptv_id: None = Field(..., alias='ptvId')
    city: None
    state: None
    postal_code: None = Field(..., alias='postalCode')
    dma: None
    display_order: int = Field(..., alias='displayOrder')
    filepath_fallback_image: None = Field(..., alias='filepathFallbackImage')
    provider_type: str = Field(..., alias='providerType')
    cbs_packages: list[str] = Field(..., alias='cbsPackages')
    video_content_id: UUID = Field(..., alias='videoContentId')
    stream_type: str = Field(..., alias='streamType')
    display_metadata: bool = Field(..., alias='displayMetadata')
    promo_content_type: None = Field(..., alias='promoContentType')
    promo_content_id: None = Field(..., alias='promoContentId')
    promo_title: None = Field(..., alias='promoTitle')
    filepath_promo_thumbnail: None = Field(..., alias='filepathPromoThumbnail')
    channel_category_slugs: list[str] = Field(..., alias='channelCategorySlugs')
    filepath_live_end_card_image: None = Field(..., alias='filepathLiveEndCardImage')
    channel_types: list[str] = Field(..., alias='channelTypes')
    display_style: str = Field(..., alias='displayStyle')
    sort_theme: str = Field(..., alias='sortTheme')
    current_listing: None = Field(..., alias='currentListing')
    upcoming_listing: list[None] = Field(..., alias='upcomingListing')
    brand: None
    total_number_of_current_listings: int = Field(..., alias='totalNumberOfCurrentListings')
    total_number_of_upcoming_listings: int = Field(..., alias='totalNumberOfUpcomingListings')
    entitlement_codes: None = Field(..., alias='entitlementCodes')
    display_count_down_timer: bool = Field(..., alias='displayCountDownTimer')
    required_add_ons: list[None] = Field(..., alias='requiredAddOns')
    enable_dashdrm: bool = Field(..., alias='enableDASHDRM')
    kids_mode: bool = Field(..., alias='kidsMode')
    local: bool
    is_content_accessible_in_cms: bool = Field(..., alias='isContentAccessibleInCMS')

class CarouselModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str | None
    title: str
    orientation: str
    left_arrow: str = Field(..., alias='leftArrow')
    right_arrow: str = Field(..., alias='rightArrow')
    display_id: UUID | str = Field(..., alias='displayId', union_mode='left_to_right')
    reco_id: UUID | str = Field(..., alias='recoId', union_mode='left_to_right')
    data: list[Datum] | Data
    carousel_id: UUID | str = Field(..., alias='carouselId', union_mode='left_to_right')
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

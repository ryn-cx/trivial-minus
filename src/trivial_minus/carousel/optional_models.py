from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from datetime import time
from typing import Any
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class AvailableVideoSeason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    season_num: str | None = Field(None, alias='seasonNum')
    total_count: int | None = Field(None, alias='totalCount')
    premium_count: int | None = Field(None, alias='premiumCount')
    clips_count: int | None = Field(None, alias='clipsCount')
    delay_count: int | None = Field(None, alias='delayCount')
    season_premiere_date: Any | None = Field(None, alias='seasonPremiereDate')
    season_premiere_date_epoch: Any | None = Field(None, alias='seasonPremiereDateEpoch')
    season_finale_date: Any | None = Field(None, alias='seasonFinaleDate')
    season_finale_date_epoch: Any | None = Field(None, alias='seasonFinaleDateEpoch')

class ShowAssets(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    filepath_show_poster: str | None = None
    filepath_apple_airplay: str | None = None
    filepath_mobile_endcard: str | None = None
    filepath_show_page_header: str | None = None
    filepath_title_logo_regular: str | None = None
    filepath_video_endcard_show_image: str | None = None
    filepath_title_logo_left: str | None = None
    filepath_apple_centered_background: str | None = None
    filepath_show_hero_landscape: str | None = None
    filepath_title_logo_center: str | None = None
    filepath_ott_hd_show_image_overhang: str | None = None
    filepath_apple_content_logo_polychromatic: str | None = None
    filepath_show_browse_poster: str | None = None
    filepath_show_hero_regular: str | None = None
    filepath_show_hero_compact: str | None = None
    filepath_show_hero_portrait: str | None = None
    filepath_apple_cover_artwork_horizontal: str | None = None
    filepath_apple_centered_background_small: str | None = None
    filepath_apple_content_logo_monochromatic: str | None = None
    filepath_title_logo_compact: str | None = None
    filepath_apple_top_shelf: str | None = None
    filepath_partner_brand_logo: str | None = None
    filepath_brand_hero: str | None = None

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hub_id: int | None = Field(None, alias='hubId')
    title: str | None = None
    hub_slug: str | None = Field(None, alias='hubSlug')
    type: str | None = None
    hub_items: Any | None = Field(None, alias='hubItems')
    page_type: str | None = Field(None, alias='pageType')
    region: str | None = None
    locale: str | None = None
    user_state: Any | list[str] | None = Field(None, alias='userState')
    live_on_date: int | None = Field(None, alias='liveOnDate')
    variant_key: Any | None = Field(None, alias='variantKey')
    show_id: int | None = Field(None, alias='showId')
    league_id: int | None = Field(None, alias='leagueId')
    about: str | None = None
    show_title: str | None = Field(None, alias='showTitle')
    content_type: str | None = Field(None, alias='contentType')
    show_path: str | None = Field(None, alias='showPath')
    tune_in_time: str | None = Field(None, alias='tuneInTime')
    premium_features: list[Any] | None = Field(None, alias='premiumFeatures')
    brand_slug: str | None = Field(None, alias='brandSlug')
    category: str | None = None
    available_video_seasons: list[AvailableVideoSeason] | None = Field(None, alias='availableVideoSeasons')
    show_assets: ShowAssets | None = Field(None, alias='showAssets')
    callbacks: dict[str, Any] | None = None
    rating: str | None = None
    first_available_date: AwareDatetime | None = Field(None, alias='firstAvailableDate')
    is_content_accessible_in_cms: bool | None = Field(None, alias='isContentAccessibleInCMS')
    required_add_ons: list[Any] | None = Field(None, alias='requiredAddOns')
    is_after_hours: bool | None = Field(None, alias='isAfterHours')
    is_kids_content: bool | None = Field(None, alias='isKidsContent')
    cast_names: list[str] | None = Field(None, alias='castNames')
    sub_video_starting_point_cta: str | None = Field(None, alias='subVideoStartingPointCTA')
    genre: str | None = None
    unified_genre: list[str] | None = Field(None, alias='unifiedGenre')
    video_preview_url: str | None = Field(None, alias='videoPreviewURL')
    show_premiere_date_str: AwareDatetime | None = Field(None, alias='showPremiereDateStr')

class ItemPem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    pvr_model: str | None = Field(None, alias='pvrModel')
    draw_id: UUID | None = Field(None, alias='drawId')
    p: str | None = None
    arm_id: UUID | None = Field(None, alias='armId')
    mab_id: str | None = Field(None, alias='mabId')

class ThumbnailSetItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: int | None = None
    width: int | None = None
    asset_type: str | None = Field(None, alias='assetType')
    url: str | None = None

class DownloadCountrySetItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    downloadable: bool | None = None

class Subrating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    description: str | None = None

class RegionalRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    region: str | None = None
    rating: str | None = None
    disclaimer: Any | None = None
    secondary_descriptors: str | None = Field(None, alias='secondaryDescriptors')
    subratings: Any | list[Subrating] | None = None
    consumer_advice: Any | None = Field(None, alias='consumerAdvice')
    rating_icon: Any | None = Field(None, alias='ratingIcon')

class PlaybackEvents(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    end_credit_chapter_time_ms: int | None = Field(None, alias='endCreditChapterTimeMs')
    preview_start_time_ms: Any | None = Field(None, alias='previewStartTimeMs')
    preview_end_time_ms: Any | None = Field(None, alias='previewEndTimeMs')
    open_credit_end_time_ms: Any | None = Field(None, alias='openCreditEndTimeMs')
    open_credit_start_time: Any | None = Field(None, alias='openCreditStartTime')

class ThumbnailSheetSetItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: int | None = None
    width: int | None = None
    asset_type: str | None = Field(None, alias='assetType')
    url: str | None = None

class MovieContent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    genre: str | None = None
    status: str | None = None
    field_first_ingest_date: str | None = Field(None, alias='_firstIngestDate')
    expired: bool | None = None
    show_page_url: str | None = Field(None, alias='showPageUrl')
    cbs_show_id: int | None = Field(None, alias='cbsShowId')
    primary_category: str | None = Field(None, alias='primaryCategory')
    primary_category_name: str | None = Field(None, alias='primaryCategoryName')
    edit_date: int | None = Field(None, alias='editDate')
    field_edit_date: str | None = Field(None, alias='_editDate')
    field_last_modified_date: str | None = Field(None, alias='_lastModifiedDate')
    ingest_date: int | None = Field(None, alias='ingestDate')
    air_date: int | None = Field(None, alias='airDate')
    description: str | None = None
    short_description: str | None = Field(None, alias='shortDescription')
    pub_date: int | None = Field(None, alias='pubDate')
    label: str | None = None
    url: str | None = None
    asset_type: str | None = Field(None, alias='assetType')
    first_ingest_date: int | None = Field(None, alias='firstIngestDate')
    category: str | None = None
    top_level_category: str | None = Field(None, alias='topLevelCategory')
    full_episode: bool | None = Field(None, alias='fullEpisode')
    exclusive: bool | None = None
    content_id: str | None = Field(None, alias='contentId')
    title: str | None = None
    field_ingest_date: str | None = Field(None, alias='_ingestDate')
    episode_num: str | None = Field(None, alias='episodeNum')
    field_pub_date: str | None = Field(None, alias='_pubDate')
    season_num: str | None = Field(None, alias='seasonNum')
    brand: str | None = None
    child_content_id: str | None = Field(None, alias='childContentId')
    sizzle_id: str | None = Field(None, alias='sizzleId')
    series_title: str | None = Field(None, alias='seriesTitle')
    field_air_date: str | None = Field(None, alias='_airDate')
    duration: int | None = None
    last_modified_date: int | None = Field(None, alias='lastModifiedDate')
    rating: str | None = None
    device_type: str | None = Field(None, alias='deviceType')
    thumbnail: str | None = None
    amazon_esturl: str | None = Field(None, alias='amazonESTURL')
    itunes_esturl: str | None = Field(None, alias='itunesESTURL')
    expiration_date: int | None = Field(None, alias='expirationDate')
    field_expiration_date: str | None = Field(None, alias='_expirationDate')
    field_pub_date_iso: AwareDatetime | None = Field(None, alias='_pubDateISO')
    field_air_date_iso: AwareDatetime | None = Field(None, alias='_airDateISO')
    subscription_level: str | None = Field(None, alias='subscriptionLevel')
    media_available_date: AwareDatetime | None = Field(None, alias='mediaAvailableDate')
    media_available_date_epoch: int | None = Field(None, alias='mediaAvailableDateEpoch')
    is_live: bool | None = Field(None, alias='isLive')
    cms_account_id: str | None = Field(None, alias='cmsAccountId')
    apple_watch_list_show_key: str | None = Field(None, alias='appleWatchListShowKey')
    is_protected: bool | None = Field(None, alias='isProtected')
    media_type: str | None = Field(None, alias='mediaType')
    exclude_nielsen_tracking: bool | None = Field(None, alias='excludeNielsenTracking')
    end_credits_chapter_time: time | None = Field(None, alias='endCreditsChapterTime')
    thumbnail_set: list[ThumbnailSetItem] | None = Field(None, alias='thumbnailSet')
    download_country_set: list[DownloadCountrySetItem] | None = Field(None, alias='downloadCountrySet')
    regional_ratings: list[RegionalRating] | None = Field(None, alias='regionalRatings')
    premium_features: list[str] | None = Field(None, alias='premiumFeatures')
    video_properties: list[str] | None = Field(None, alias='videoProperties')
    aspect_ratio: str | None = Field(None, alias='aspectRatio')
    external_id: str | None = Field(None, alias='externalId')
    available_for_profile_types: list[str] | None = Field(None, alias='availableForProfileTypes')
    playback_events: PlaybackEvents | None = Field(None, alias='playbackEvents')
    embeddable: str | None = None
    copyright: str | None = None
    add_ons: list[str] | None = Field(None, alias='addOns')
    regional_audio_exclude_languages: list[Any] | None = Field(None, alias='regionalAudioExcludeLanguages')
    regional_text_exclude_languages: list[Any] | None = Field(None, alias='regionalTextExcludeLanguages')
    original_release_year: int | None = Field(None, alias='originalReleaseYear')
    tmsseries_id: str | None = Field(None, alias='tmsseriesID')
    tmsprogram_id: str | None = Field(None, alias='tmsprogramID')
    is_content_accessible_in_can: bool | None = Field(None, alias='isContentAccessibleInCAN')
    thumbnail_sheet_set: list[ThumbnailSheetSetItem] | None = Field(None, alias='thumbnailSheetSet')
    v_tag: str | None = Field(None, alias='vTag')
    is_product_placement: bool | None = Field(None, alias='isProductPlacement')
    brand_slug: str | None = Field(None, alias='brandSlug')
    is_movie_available: bool | None = Field(None, alias='isMovieAvailable')

class RegionalRating1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    region: str | None = None
    rating: str | None = None
    disclaimer: Any | None = None
    secondary_descriptors: str | None = Field(None, alias='secondaryDescriptors')
    subratings: Any | list[Subrating] | None = None
    consumer_advice: Any | None = Field(None, alias='consumerAdvice')
    rating_icon: Any | None = Field(None, alias='ratingIcon')

class PlaybackEvents1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    end_credit_chapter_time_ms: Any | None = Field(None, alias='endCreditChapterTimeMs')
    preview_start_time_ms: Any | None = Field(None, alias='previewStartTimeMs')
    preview_end_time_ms: Any | None = Field(None, alias='previewEndTimeMs')
    open_credit_end_time_ms: Any | None = Field(None, alias='openCreditEndTimeMs')
    open_credit_start_time: Any | None = Field(None, alias='openCreditStartTime')

class TrailerContent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    genre: str | None = None
    status: str | None = None
    field_first_ingest_date: str | None = Field(None, alias='_firstIngestDate')
    expired: bool | None = None
    show_page_url: str | None = Field(None, alias='showPageUrl')
    cbs_show_id: int | None = Field(None, alias='cbsShowId')
    primary_category: str | None = Field(None, alias='primaryCategory')
    primary_category_name: str | None = Field(None, alias='primaryCategoryName')
    edit_date: int | None = Field(None, alias='editDate')
    field_edit_date: str | None = Field(None, alias='_editDate')
    field_last_modified_date: str | None = Field(None, alias='_lastModifiedDate')
    ingest_date: int | None = Field(None, alias='ingestDate')
    air_date: int | None = Field(None, alias='airDate')
    description: str | None = None
    short_description: str | None = Field(None, alias='shortDescription')
    pub_date: int | None = Field(None, alias='pubDate')
    label: str | None = None
    video_page_url: str | None = Field(None, alias='videoPageUrl')
    url: str | None = None
    asset_type: str | None = Field(None, alias='assetType')
    first_ingest_date: int | None = Field(None, alias='firstIngestDate')
    category: str | None = None
    top_level_category: str | None = Field(None, alias='topLevelCategory')
    full_episode: bool | None = Field(None, alias='fullEpisode')
    exclusive: bool | None = None
    content_id: str | None = Field(None, alias='contentId')
    title: str | None = None
    field_ingest_date: str | None = Field(None, alias='_ingestDate')
    episode_num: str | None = Field(None, alias='episodeNum')
    field_pub_date: str | None = Field(None, alias='_pubDate')
    season_num: str | None = Field(None, alias='seasonNum')
    brand: str | None = None
    child_content_id: str | None = Field(None, alias='childContentId')
    sizzle_id: str | None = Field(None, alias='sizzleId')
    pid: UUID | str | None = Field(default=None, union_mode='left_to_right')
    series_title: str | None = Field(None, alias='seriesTitle')
    field_air_date: str | None = Field(None, alias='_airDate')
    duration: int | None = None
    last_modified_date: int | None = Field(None, alias='lastModifiedDate')
    rating: str | None = None
    device_type: str | None = Field(None, alias='deviceType')
    thumbnail: str | None = None
    amazon_esturl: str | None = Field(None, alias='amazonESTURL')
    itunes_esturl: str | None = Field(None, alias='itunesESTURL')
    streaming_url: str | None = Field(None, alias='streamingUrl')
    expiration_date: int | None = Field(None, alias='expirationDate')
    field_expiration_date: str | None = Field(None, alias='_expirationDate')
    field_pub_date_iso: AwareDatetime | None = Field(None, alias='_pubDateISO')
    field_air_date_iso: AwareDatetime | None = Field(None, alias='_airDateISO')
    player_loc_url: str | None = Field(None, alias='playerLocUrl')
    subscription_level: str | None = Field(None, alias='subscriptionLevel')
    media_available_date: AwareDatetime | None = Field(None, alias='mediaAvailableDate')
    media_available_date_epoch: int | None = Field(None, alias='mediaAvailableDateEpoch')
    closed_caption_url: str | None = Field(None, alias='closedCaptionUrl')
    is_live: bool | None = Field(None, alias='isLive')
    cms_account_id: str | None = Field(None, alias='cmsAccountId')
    apple_watch_list_show_key: str | None = Field(None, alias='appleWatchListShowKey')
    is_protected: bool | None = Field(None, alias='isProtected')
    media_type: str | None = Field(None, alias='mediaType')
    exclude_nielsen_tracking: bool | None = Field(None, alias='excludeNielsenTracking')
    end_credits_chapter_time: str | None = Field(None, alias='endCreditsChapterTime')
    thumbnail_set: list[ThumbnailSetItem] | None = Field(None, alias='thumbnailSet')
    download_country_set: list[DownloadCountrySetItem] | None = Field(None, alias='downloadCountrySet')
    regional_ratings: list[RegionalRating1] | None = Field(None, alias='regionalRatings')
    premium_features: list[str] | None = Field(None, alias='premiumFeatures')
    video_properties: list[str] | None = Field(None, alias='videoProperties')
    aspect_ratio: str | None = Field(None, alias='aspectRatio')
    external_id: str | None = Field(None, alias='externalId')
    available_for_profile_types: list[str] | None = Field(None, alias='availableForProfileTypes')
    playback_events: PlaybackEvents1 | None = Field(None, alias='playbackEvents')
    embeddable: str | None = None
    copyright: str | None = None
    add_ons: list[str] | None = Field(None, alias='addOns')
    regional_audio_exclude_languages: list[Any] | None = Field(None, alias='regionalAudioExcludeLanguages')
    regional_text_exclude_languages: list[Any] | None = Field(None, alias='regionalTextExcludeLanguages')
    original_release_year: int | None = Field(None, alias='originalReleaseYear')
    tmsseries_id: str | None = Field(None, alias='tmsseriesID')
    tmsprogram_id: str | None = Field(None, alias='tmsprogramID')
    is_content_accessible_in_can: bool | None = Field(None, alias='isContentAccessibleInCAN')
    thumbnail_sheet_set: list[ThumbnailSheetSetItem] | None = Field(None, alias='thumbnailSheetSet')
    v_tag: str | None = Field(None, alias='vTag')
    is_product_placement: bool | None = Field(None, alias='isProductPlacement')
    brand_slug: str | None = Field(None, alias='brandSlug')

class AvailableVideoSeason1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    season_num: str | None = Field(None, alias='seasonNum')
    total_count: int | None = Field(None, alias='totalCount')
    premium_count: int | None = Field(None, alias='premiumCount')
    clips_count: int | None = Field(None, alias='clipsCount')
    delay_count: int | None = Field(None, alias='delayCount')
    season_premiere_date: str | None = Field(None, alias='seasonPremiereDate')
    season_premiere_date_epoch: int | None = Field(None, alias='seasonPremiereDateEpoch')
    season_finale_date: Any | None = Field(None, alias='seasonFinaleDate')
    season_finale_date_epoch: Any | None = Field(None, alias='seasonFinaleDateEpoch')

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None
    season: int | None = None
    episode: int | None = None
    url: str | None = None
    play: bool | None = None

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None
    slug: str | None = None
    brand_id: str | None = Field(None, alias='brandId')
    brand_slug: str | None = Field(None, alias='brandSlug')
    page_type: str | None = Field(None, alias='pageType')
    show_path: str | None = Field(None, alias='showPath')
    movie_page_url: str | None = Field(None, alias='moviePageUrl')
    content_type: str | None = Field(None, alias='contentType')
    href: str | None = None
    thumb: str | None = None
    brand_logo: str | None = Field(None, alias='brandLogo')
    top_ten_badge: Any | None = Field(None, alias='topTenBadge')
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
    rank_model: Any | None = Field(None, alias='rankModel')
    cms_id: int | str | None = Field(None, alias='cmsId')
    content: Content | None = None
    id: int | str | None = None
    content_id: int | str | None = Field(None, alias='contentId')
    alt: str | None = None
    tune_in_time: str | None = Field(None, alias='tuneInTime')
    category: str | None = None
    is_listing_live: bool | None = Field(None, alias='isListingLive')
    show: Any | None = None
    pvr_model: str | None = Field(None, alias='pvrModel')
    item_pem: Any | ItemPem | None = Field(None, alias='itemPEM')
    bundle_locked: bool | None = Field(None, alias='bundleLocked')
    badge_label: bool | str | None = Field(None, alias='badgeLabel')
    aa_link: str | None = Field(None, alias='aaLink')
    impression: str | None = None
    display_item_title: bool | None = Field(None, alias='displayItemTitle')
    is_user_subscriber: bool | None = Field(None, alias='isUserSubscriber')
    is_user_kid_profile: str | None = Field(None, alias='isUserKidProfile')
    is_content_accessible_in_cms: bool | None = Field(None, alias='isContentAccessibleInCMS')
    show_or_movie: str | None = Field(None, alias='showOrMovie')
    show_title: str | None = Field(None, alias='showTitle')
    about: str | None = None
    movie_content: Any | MovieContent | None = Field(None, alias='movieContent')
    trailer_content: Any | TrailerContent | None = Field(None, alias='trailerContent')
    video_preview_url: str | None = Field(None, alias='videoPreviewURL')
    data_tracking: str | None = Field(None, alias='dataTracking')
    show_series_title: str | None = Field(None, alias='showSeriesTitle')
    title_slug: str | None = Field(None, alias='titleSlug')
    brand: str | None = None
    brand_name: str | None = Field(None, alias='brandName')
    genre: str | None = None
    num_seasons: int | str | None = Field(None, alias='numSeasons')
    carousel_content_type: str | None = Field(None, alias='carouselContentType')
    cast_names: str | None = Field(None, alias='castNames')
    poster: str | None = None
    movie_id: int | str | None = Field(None, alias='movieId')
    content_notification_add_action_url: str | None = Field(None, alias='contentNotificationAddActionUrl')
    content_notification_remove_action_url: str | None = Field(None, alias='contentNotificationRemoveActionUrl')
    content_my_list_add_action_url: str | None = Field(None, alias='contentMyListAddActionUrl')
    content_my_list_remove_action_url: str | None = Field(None, alias='contentMyListRemoveActionUrl')
    allow_my_list_controls: bool | None = Field(None, alias='allowMyListControls')
    has_content_highlight: bool | None = Field(None, alias='hasContentHighlight')
    show_id: int | None = Field(None, alias='showId')
    carousel_type: str | None = Field(None, alias='carouselType')
    video_content_id: str | None = Field(None, alias='videoContentId')
    time_stamp: str | None = Field(None, alias='timeStamp')
    is_seasonless: bool | None = Field(None, alias='isSeasonless')
    is_episodeless: bool | None = Field(None, alias='isEpisodeless')
    rating: str | None = None
    rating_icon: str | None = Field(None, alias='ratingIcon')
    season_counts: str | None = Field(None, alias='seasonCounts')
    premiere_date: str | None = Field(None, alias='premiereDate')
    available_video_seasons: Any | list[AvailableVideoSeason1] | None = Field(None, alias='availableVideoSeasons')
    button: Button | None = None
    logo: str | None = None
    title_text: str | None = Field(None, alias='titleText')
    content_id_1: str | None = Field(None, alias='content_id')
    is_movie: bool | None = Field(None, alias='isMovie')
    movie_duration: str | None = Field(None, alias='movieDuration')
    movie_rating: str | None = Field(None, alias='movieRating')
    upsell_url: str | None = Field(None, alias='upsellUrl')
    lock_icon: str | None = Field(None, alias='lockIcon')
    orientation: str | None = None
    promo_tile: bool | None = Field(None, alias='promoTile')
    promo_icon: str | None = Field(None, alias='promoIcon')
    cta_line1: str | None = Field(None, alias='ctaLine1')
    cta_line2: str | None = Field(None, alias='ctaLine2')
    deep_link_url: str | None = Field(None, alias='deepLinkUrl')
    hub_id: int | None = Field(None, alias='hubId')
    content_locked: int | str | None = Field(None, alias='contentLocked')
    show_series_id: int | str | None = Field(None, alias='showSeriesId')
    filepath1x1_default_image: str | None = Field(None, alias='filepath1x1DefaultImage')
    filepath1x1_focus_state_image: str | None = Field(None, alias='filepath1x1FocusStateImage')
    movie_title: str | None = Field(None, alias='movieTitle')

class CarouselModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    title: str | None = None
    orientation: str | None = None
    left_arrow: str | None = Field(None, alias='leftArrow')
    right_arrow: str | None = Field(None, alias='rightArrow')
    display_id: UUID | str | None = Field(None, alias='displayId', union_mode='left_to_right')
    reco_id: UUID | str | None = Field(None, alias='recoId', union_mode='left_to_right')
    data: list[Datum] | None = None
    carousel_id: UUID | str | None = Field(None, alias='carouselId', union_mode='left_to_right')
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

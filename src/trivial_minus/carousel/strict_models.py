from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import time
from typing import Any
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, Field

class Content(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hub_id: int = Field(..., alias='hubId')
    title: str
    hub_slug: str = Field(..., alias='hubSlug')
    type: str
    hub_items: None = Field(..., alias='hubItems')
    page_type: str = Field(..., alias='pageType')
    region: str
    locale: str
    user_state: list[str] | None = Field(..., alias='userState')
    live_on_date: int = Field(..., alias='liveOnDate')
    variant_key: None = Field(..., alias='variantKey')

class ItemPem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    pvr_model: str = Field(..., alias='pvrModel')
    draw_id: UUID = Field(..., alias='drawId')
    p: str | None = None
    arm_id: UUID | None = Field(None, alias='armId')
    mab_id: str | None = Field(None, alias='mabId')

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

class Subrating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: str
    description: str

class RegionalRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    region: str
    rating: str
    disclaimer: None
    secondary_descriptors: str | None = Field(..., alias='secondaryDescriptors')
    subratings: list[Subrating] | None
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
    external_id: str | None = Field(None, alias='externalId')
    available_for_profile_types: list[str] = Field(..., alias='availableForProfileTypes')
    playback_events: PlaybackEvents = Field(..., alias='playbackEvents')
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

class RegionalRating1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    region: str
    rating: str
    disclaimer: None
    secondary_descriptors: str | None = Field(..., alias='secondaryDescriptors')
    subratings: list[Subrating] | None
    consumer_advice: None = Field(..., alias='consumerAdvice')
    rating_icon: None = Field(..., alias='ratingIcon')

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
    regional_ratings: list[RegionalRating1] = Field(..., alias='regionalRatings')
    premium_features: list[str] = Field(..., alias='premiumFeatures')
    video_properties: list[str] = Field(..., alias='videoProperties')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    external_id: str | None = Field(None, alias='externalId')
    available_for_profile_types: list[str] = Field(..., alias='availableForProfileTypes')
    playback_events: PlaybackEvents1 = Field(..., alias='playbackEvents')
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

class AvailableVideoSeason(BaseModel):
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
    season: int
    episode: int
    url: str
    play: bool

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str | None = None
    slug: str | None = None
    brand_id: str | None = Field(None, alias='brandId')
    brand_slug: str | None = Field(None, alias='brandSlug')
    page_type: str | None = Field(None, alias='pageType')
    show_path: str | None = Field(None, alias='showPath')
    movie_page_url: str | None = Field(None, alias='moviePageUrl')
    content_type: str = Field(..., alias='contentType')
    href: str
    thumb: str
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
    item_pem: ItemPem | None = Field(..., alias='itemPEM')
    bundle_locked: bool | None = Field(None, alias='bundleLocked')
    badge_label: bool | str | None = Field(None, alias='badgeLabel')
    aa_link: str = Field(..., alias='aaLink')
    impression: str | None = None
    display_item_title: bool | None = Field(None, alias='displayItemTitle')
    is_user_subscriber: bool | None = Field(None, alias='isUserSubscriber')
    is_user_kid_profile: str | None = Field(None, alias='isUserKidProfile')
    is_content_accessible_in_cms: bool | None = Field(None, alias='isContentAccessibleInCMS')
    show_or_movie: str | None = Field(None, alias='showOrMovie')
    show_title: str | None = Field(None, alias='showTitle')
    about: str | None = None
    movie_content: MovieContent | None = Field(None, alias='movieContent')
    trailer_content: TrailerContent | None = Field(None, alias='trailerContent')
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
    available_video_seasons: list[AvailableVideoSeason] | None = Field(None, alias='availableVideoSeasons')
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
    content_locked: str | None = Field(None, alias='contentLocked')

class CarouselModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    title: str
    orientation: str
    left_arrow: str = Field(..., alias='leftArrow')
    right_arrow: str = Field(..., alias='rightArrow')
    display_id: UUID | str = Field(..., alias='displayId', union_mode='left_to_right')
    reco_id: UUID | str = Field(..., alias='recoId', union_mode='left_to_right')
    data: list[Datum]
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

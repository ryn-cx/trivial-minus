# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import CarouselModel as OptionalModel
from .strict_models import CarouselModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        AvailableVideoSeason,
        AvailableVideoSeason1,
        Button,
        CarouselModel,
        Content,
        ContentCanVideo,
        Data,
        Datum,
        DownloadCountrySetItem,
        ItemPem,
        MovieAssets,
        MovieContent,
        MovieContent1,
        PlaybackEvents,
        PlaybackEvents1,
        PlaybackEvents2,
        PlaybackEvents3,
        RegionalRating,
        RegionalRating2,
        RegionalRating3,
        RegionalRating4,
        ShowAssets,
        Subrating,
        ThumbnailSetItem,
        ThumbnailSheetSetItem,
        TrailerContent,
        TrailerContent1,
        WatchListCtaContent,
    )
else:
    from .optional_models import (
        AvailableVideoSeason,
        AvailableVideoSeason1,
        Button,
        CarouselModel,
        Content,
        ContentCanVideo,
        Data,
        Datum,
        DownloadCountrySetItem,
        ItemPem,
        MovieAssets,
        MovieContent,
        MovieContent1,
        PlaybackEvents,
        PlaybackEvents1,
        PlaybackEvents2,
        PlaybackEvents3,
        RegionalRating,
        RegionalRating2,
        RegionalRating3,
        RegionalRating4,
        ShowAssets,
        Subrating,
        ThumbnailSetItem,
        ThumbnailSheetSetItem,
        TrailerContent,
        TrailerContent1,
        WatchListCtaContent,
    )

__all__ = [
    "AvailableVideoSeason",
    "AvailableVideoSeason1",
    "Button",
    "CarouselModel",
    "Content",
    "ContentCanVideo",
    "Data",
    "Datum",
    "DownloadCountrySetItem",
    "ItemPem",
    "MovieAssets",
    "MovieContent",
    "MovieContent1",
    "PlaybackEvents",
    "PlaybackEvents1",
    "PlaybackEvents2",
    "PlaybackEvents3",
    "RegionalRating",
    "RegionalRating2",
    "RegionalRating3",
    "RegionalRating4",
    "ShowAssets",
    "Subrating",
    "ThumbnailSetItem",
    "ThumbnailSheetSetItem",
    "TrailerContent",
    "TrailerContent1",
    "WatchListCtaContent",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> CarouselModel:
    """Read a downloaded file into CarouselModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

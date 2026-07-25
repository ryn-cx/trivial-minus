# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

import re
from collections.abc import Mapping
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, cast, override

from trivialminus.base_api_endpoint import BaseEndpoint
from trivialminus.constants import (
    DEFAULT_DMA,
    DEFAULT_LATITUDE,
    DEFAULT_LONGITUDE,
    DEFAULT_STATION_ID,
    DEFAULT_TIME_ZONE,
    WEB_DOMAIN,
)
from trivialminus.search.models import SearchModel

if TYPE_CHECKING:
    from good_ass_pydantic_integrator.constants import INPUT_TYPE

logger = getLogger(__name__)
logger.addHandler(NullHandler())

_SECTION_RE = re.compile(
    r'<div class="[^"]*search__results--display[^"]*"'
    r'[^>]*?data-title="(?P<title>[^"]*)"',
    re.DOTALL,
)
_ANCHOR_RE = re.compile(r"<a\b(?P<body>.*?)</a>", re.DOTALL)
_IMG_SRC_RE = re.compile(r'<img[^>]*\bsrc="([^"]*)"')
_BADGE_RE = re.compile(r'badge-copy">([^<]*)<')

_MEDIA_TYPE_INDEX = 2
_POSITION_INDEX = 3


def _attr(text: str, name: str) -> str | None:
    match = re.search(rf'\b{name}="([^"]*)"', text)
    return match.group(1) if match else None


def _parse_results(html: str) -> list[dict[str, Any]]:
    """Parse the lookup HTML fragment into a list of structured result dicts.

    Sections are delimited by `search__results--display` divs; each `<a>`
    within a section that carries a `data-impression` is one result. The
    impression string is `content_id|title|media_type|position|||content_id`.
    """
    sections = [(m.start(), m.group("title")) for m in _SECTION_RE.finditer(html)]
    results: list[dict[str, Any]] = []
    for index, (start, section_title) in enumerate(sections):
        end = sections[index + 1][0] if index + 1 < len(sections) else len(html)
        for match in _ANCHOR_RE.finditer(html[start:end]):
            anchor = match.group("body")
            impression = _attr(anchor, "data-impression")
            if not impression:
                continue
            parts = impression.split("|")
            position = parts[_POSITION_INDEX] if len(parts) > _POSITION_INDEX else ""
            image = _IMG_SRC_RE.search(anchor)
            badges = _BADGE_RE.findall(anchor)
            results.append(
                {
                    "section": section_title,
                    "title": _attr(anchor, "aria-label"),
                    "series_title": _attr(anchor, "title"),
                    "url": _attr(anchor, "href"),
                    "content_id": parts[0] or None,
                    "media_type": (
                        parts[_MEDIA_TYPE_INDEX]
                        if len(parts) > _MEDIA_TYPE_INDEX
                        else None
                    ),
                    "position": int(position) if position.isdigit() else None,
                    "thumbnail": image.group(1) if image else None,
                    "badge": badges[0].strip() if badges else None,
                    "is_event": "is-event" in (_attr(anchor, "class") or ""),
                },
            )
    return results


class Search(BaseEndpoint[SearchModel]):
    """Manage the search file.

    Wraps the `search/lookup` route. Served anonymously (the example request
    was captured from a subscriber session, but the subscriber cookies are not
    required). The raw response is `{"success": bool, "html": str}` where
    `html` is the rendered results fragment; :meth:`transform_input` parses
    that fragment into a structured `results` list before validation, so the
    model exposes typed per-result fields (title, url, content_id, media_type,
    position, thumbnail, badge, ...). The raw HTML is still preserved on the
    model's `raw_input`.

    Source: https://www.paramountplus.com/search/

    Example request:
        - GET /search/lookup/?
            - term=Cherryn&
            - dma=807&
            - stationId=16533&
            - latitude=37.99&
            - longitude=-121.71&
            - timeZone=America%2FLos_Angeles
            - HTTP/2
        - Host: www.paramountplus.com
        - User-Agent: __REDACTED__
        - Accept: application/json, text/javascript, */*; q=0.01
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.paramountplus.com/search/
        - X-Requested-With: XMLHttpRequest
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - Cookie: __REDACTED__
    """

    _response_model = SearchModel

    @classmethod
    @override
    def transform_input(cls, data: INPUT_TYPE) -> INPUT_TYPE:
        """Replace the raw `html` blob with a parsed `results` list."""
        if not isinstance(data, Mapping) or "html" not in data:
            return data
        mapping = cast("Mapping[str, Any]", data)
        return {
            "success": mapping.get("success"),
            "results": _parse_results(str(mapping["html"])),
        }

    @override
    def download(
        self,
        term: str,
        *,
        dma: str = DEFAULT_DMA,
        station_id: str = DEFAULT_STATION_ID,
        latitude: str = DEFAULT_LATITUDE,
        longitude: str = DEFAULT_LONGITUDE,
        time_zone: str = DEFAULT_TIME_ZONE,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        return self._client.download_json(
            f"https://{WEB_DOMAIN}/search/lookup/",
            referer=f"https://{WEB_DOMAIN}/search/",
            params={
                "term": term,
                "dma": dma,
                "stationId": station_id,
                "latitude": latitude,
                "longitude": longitude,
                "timeZone": time_zone,
            },
            log_id=log_id,
        )

    @override
    def download_and_parse(
        self,
        term: str,
        *,
        dma: str = DEFAULT_DMA,
        station_id: str = DEFAULT_STATION_ID,
        latitude: str = DEFAULT_LATITUDE,
        longitude: str = DEFAULT_LONGITUDE,
        time_zone: str = DEFAULT_TIME_ZONE,
    ) -> SearchModel:
        return self.parse(
            self.download(
                term,
                dma=dma,
                station_id=station_id,
                latitude=latitude,
                longitude=longitude,
                time_zone=time_zone,
            ),
        )

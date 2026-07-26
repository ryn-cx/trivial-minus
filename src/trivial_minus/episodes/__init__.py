"""Contains the Episodes class."""

from __future__ import annotations

from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any, override

from trivial_minus.base_api_endpoint import BaseEndpoint
from trivial_minus.episodes.models import EpisodesModel
from trivial_minus.exceptions import (
    ResourceNotFoundError,
    SeasonNotFoundError,
    ShowNotFoundError,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Episodes(BaseEndpoint[EpisodesModel]):
    """Manage the episodes file.

    Source: https://www.paramountplus.com/shows/{show_id}/

    Example request:
        - GET /shows/{show_id}/xhr/episodes/page/0/size/18/xs/0/season/{seaon_id/ HTTP/2
        - Host: www.paramountplus.com
        - User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0
        - Accept: application/json, text/javascript, */*; q=0.01
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.paramountplus.com/shows/south-park/
        - newrelic: eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MzYzNDgiLCJhcCI6IjExMDMyMTY1MTgiLCJpZCI6IjcyNWEwYjA3YmJmNTQ1M2QiLCJ0ciI6IjFkN2U1NWE3MjJjNTYwODExNDY2Yjk4Nzk4YzUxMTFiIiwidGkiOjE3ODUwMDk3MjA2MTYsInRrIjoiMjMyMTYwNiJ9fQ==
        - traceparent: 00-1d7e55a722c560811466b98798c5111b-725a0b07bbf5453d-01
        - tracestate: 2321606@nr=0-1-2936348-1103216518-725a0b07bbf5453d----1785009720616
        - X-Requested-With: XMLHttpRequest
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - Connection: keep-alive
        - Cookie: pplus_timezone=America%2FLos_Angeles; CBS_ST=SUBSCRIBER; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Jul+25+2026+13%3A01%3A23+GMT-0700+(Pacific+Daylight+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=null&hosts=&genVendors=V20%3A0%2CV16%3A0%2CV21%3A0%2C&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1%2C5%3A1&AwaitingReconsent=false&geolocation=%3B&consentId=84b6daf5828b8921b86ef6835c4343829feba8e2b1328f9ffd402682edf340d8&isAnonUser=0; OptanonAlertBoxClosed=2026-07-23T00:53:01.765Z; CBS_COM=MDE1MkY4NEMxNUFFODZDMzEwRjFGOTdENjAyRjkzQkU2NjExMTg2RUM0Mjc2NTQ0NjU2MTIwOTA0QzI5Njk4QjoxODE2MzA0MDMyNDg3Ojg0M2I5OGRkY2Q3NTZmMzY2N2E0ZDVlNGZlNTg3YTgwOjMuMDoxOTA1NDY0Mw; CBS_PID=a878b9ff-8a3a-4a9b-a090-543578fd0499; CBS_U=ge:null|gr:6; CBS_ATTB=sl:g|ts:2026-07-25T20:01:58.130Z; abtest_api_overrides=%7B%7D; CBS_RR=US; pin_switch=0; ab.storage.sessionId.8cb8412e-2475-416f-b1df-c03199764b1f=%7B%22g%22%3A%22ab3486dd-e39d-eb80-05b0-66ae644cd61f%22%2C%22e%22%3A1785011483232%2C%22c%22%3A1785009514694%2C%22l%22%3A1785009683232%7D; ab.storage.deviceId.8cb8412e-2475-416f-b1df-c03199764b1f=%7B%22g%22%3A%2241390609-825b-9889-3e26-c819000cde69%22%2C%22c%22%3A1757223740541%2C%22l%22%3A1785009514694%7D; ab.storage.userId.8cb8412e-2475-416f-b1df-c03199764b1f=%7B%22g%22%3A%2219054643%22%2C%22c%22%3A1757223740541%2C%22l%22%3A1785009514694%7D; parentalControlPin=1; CBS_ADV_VAL=d; CBS_ADV_SUBSES_VAL=3; CBS_CP=0; WcoSMza=dfde122cb51e49faa70d6db0b9a8c9f7.f6a3b490b6d7d1191b5532fd80ef7038bc11a620fed567b409bd47f248e95e1ee425269ca086be1ceeb7d492a71663ea39a4f90e70ceaa9558cd1cd1d7d19abc0f85b504d0886538d59bf07a8eb81f85fe89c63c7482d3a9dd7b901b0d39ad5f4fa416d30a4dbbb19d03f2ae6856dca6a28565a2bacf90a306bda90908608cfb2941cd73585cd19ae40ab731470166405bffdcece41ae221d67aca6e51a9fb026272dc6ce9666cd63ba15936e679a1ef859c9264a34e72a00ff373c3018b7b37937ea3dddd95f3fff9ec24aa27814667329be2f2d5e58939178bb11a01da83dfcf.0xd0aa87d60aa770b0829e11c408b7629f58d858e9e4f14f7f193fb0de23aa776d; ovvuid=283b8d7d-2dda-3b06-3bbd-85319fc6f3a4; dmaInfo=807
        - Priority: u=0
    """

    _response_model = EpisodesModel

    @override
    def download(
        self,
        show_id: str,
        *,
        season_number: int,
        page: int = 0,
        size: int = 18,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        referer = f"https://www.paramountplus.com/shows/{show_id}/"
        url = (
            f"https://www.paramountplus.com/shows/{show_id}/xhr/episodes"
            f"/page/{page}/size/{size}/xs/0/season/{season_number}/"
        )
        try:
            response = self._client.download_json(url, referer=referer, log_id=log_id)
        except ResourceNotFoundError as err:
            raise ShowNotFoundError(
                show_id,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, show_id, season_number)

    def _validate_download(
        self,
        response: dict[str, Any],
        show: str,
        season: int,
    ) -> dict[str, Any]:
        if not response["result"]["data"]:
            raise SeasonNotFoundError(show, season, HTTPStatus.OK, response)
        return response

    @override
    def download_and_parse(
        self,
        show: str,
        *,
        season: int,
        page: int = 0,
        size: int = 18,
    ) -> EpisodesModel:
        return self.parse(self.download(show, season_number=season, page=page, size=size))

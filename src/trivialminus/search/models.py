from pydantic import Field
from uuid import UUID
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict

class Result(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    section: str
    title: str
    series_title: str
    url: str
    content_id: UUID | str = Field(union_mode='left_to_right')
    media_type: str
    position: int
    thumbnail: str
    badge: str | None
    is_event: bool

class SearchModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    success: bool
    results: list[Result]

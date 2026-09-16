from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from trivial_minus import TrivialMinus
from trivial_minus.section import extract_section

MODEL_NAME = "SectionModel"


# TODO: Validate
class SectionId(RecordingId[TrivialMinus]):
    show_id: str
    section_id: int

    # TODO: Validate
    def recording_name(self) -> str:
        return f"{self.show_id}-{self.section_id}"

    # TODO: Validate
    def download(self, client: TrivialMinus) -> str:
        return client.section.download(self.show_id, section_id=self.section_id)


SECTIONS = load_ids(GENERATOR_PATHS, MODEL_NAME, SectionId)


# TODO: Validate
def generate_section(client: TrivialMinus) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SECTIONS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, SectionId, extract_section)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_section(TrivialMinus(build_client_automatically()))

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
from trivial_minus.show import extract_show

MODEL_NAME = "ShowModel"


# TODO: Validate
class ShowId(RecordingId[TrivialMinus]):
    show_id: str

    # TODO: Validate
    def download(self, client: TrivialMinus) -> str:
        return client.show.download(self.show_id)


SHOW_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, ShowId)


# TODO: Validate
def generate_show(client: TrivialMinus) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SHOW_IDS, client, ".html")
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ShowId, extract_show)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_show(TrivialMinus(build_client_automatically()))

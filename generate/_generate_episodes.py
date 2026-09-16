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
from trivial_minus.episodes import extract_episodes

MODEL_NAME = "EpisodesModel"


# TODO: Validate
class EpisodesId(RecordingId[TrivialMinus]):
    show_id: str
    season_number: int

    # TODO: Validate
    def recording_name(self) -> str:
        return f"{self.show_id}-s{self.season_number}"

    # TODO: Validate
    def download(self, client: TrivialMinus) -> str:
        return client.episodes.download(self.show_id, season_number=self.season_number)


SEASONS = load_ids(GENERATOR_PATHS, MODEL_NAME, EpisodesId)


# TODO: Validate
def generate_episodes(client: TrivialMinus) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SEASONS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, EpisodesId, extract_episodes)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_episodes(TrivialMinus(build_client_automatically()))

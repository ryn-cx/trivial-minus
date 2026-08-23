# TODO: Validate
"""Rebuilds EpisodesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, TRIVIAL_MINUS_PATH
from generate.utils import download_if_missing
from trivial_minus import TrivialMinus

SEASONS = [("south-park", 28), ("south-park", 999)]
"""The show and season number each recorded episode list is for."""


# TODO: Validate
def generate_episodes(client: TrivialMinus) -> None:
    """Rebuild EpisodesModel."""
    for show_id, season_number in SEASONS:
        download_if_missing(
            FILES_PATH,
            "EpisodesModel",
            f"{show_id}-s{season_number}",
            lambda show_id=show_id, season_number=season_number: (
                client.episodes.download(show_id, season_number=season_number)
            ),
        )
    generate_model(FILES_PATH, TRIVIAL_MINUS_PATH, "EpisodesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_episodes(TrivialMinus(build_client_automatically()))

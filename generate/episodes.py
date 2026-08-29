# TODO: Validate
"""Rebuilds EpisodesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, TRIVIAL_MINUS_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from trivial_minus import TrivialMinus

SEASONS = load_ids("EpisodesModel")
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
    rebuild_model(
        FILES_PATH,
        TRIVIAL_MINUS_PATH,
        "EpisodesModel",
        name_of=lambda season: f"{season[0]}-s{season[1]}",
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_episodes(TrivialMinus(build_client_automatically()))

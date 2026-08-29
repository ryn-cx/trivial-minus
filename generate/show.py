# TODO: Validate
"""Rebuilds ShowModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, TRIVIAL_MINUS_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from trivial_minus import TrivialMinus
from trivial_minus.show.extract import extract_show

SHOW_IDS = load_ids("ShowModel")


# TODO: Validate
def generate_show(client: TrivialMinus) -> None:
    """Rebuild ShowModel."""
    for show_id in SHOW_IDS:
        download_if_missing(
            FILES_PATH,
            "ShowModel",
            show_id,
            lambda show_id=show_id: client.show.download(show_id),
            ".html",
        )
    # A show is answered with a page rather than JSON, so the recordings are run
    # through the same extractor the endpoint's `load` uses.
    rebuild_model(FILES_PATH, TRIVIAL_MINUS_PATH, "ShowModel", extract_show)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_show(TrivialMinus(build_client_automatically()))

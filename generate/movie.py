# TODO: Validate
"""Rebuilds MovieModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, TRIVIAL_MINUS_PATH
from generate.utils import download_if_missing
from trivial_minus import TrivialMinus

MOVIE_IDS = ["ALVE01KT235XQDEK58R7H2012VNZMK"]


# TODO: Validate
def generate_movie(client: TrivialMinus) -> None:
    """Rebuild MovieModel."""
    for movie_id in MOVIE_IDS:
        download_if_missing(
            FILES_PATH,
            "MovieModel",
            movie_id,
            lambda movie_id=movie_id: client.movie.download(movie_id),
        )
    generate_model(FILES_PATH, TRIVIAL_MINUS_PATH, "MovieModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movie(TrivialMinus(build_client_automatically()))

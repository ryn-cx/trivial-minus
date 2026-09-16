from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_named_missing,
    load_named_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from trivial_minus import TrivialMinus
from trivial_minus.collections import extract_collections

MODEL_NAME = "CollectionsModel"


# TODO: Validate
class CollectionsId(RecordingId[TrivialMinus]):
    # TODO: Validate
    def download(self, client: TrivialMinus) -> str:
        return client.collections.download()


COLLECTIONS = load_named_ids(GENERATOR_PATHS, MODEL_NAME, CollectionsId)


# TODO: Validate
def generate_collections(client: TrivialMinus) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, COLLECTIONS, client, ".html")
    rebuild_model(
        GENERATOR_PATHS,
        MODEL_NAME,
        CollectionsId,
        extract_collections,
        ".html",
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_collections(TrivialMinus(build_client_automatically()))

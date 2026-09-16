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
from trivial_minus.collection import extract_collection

MODEL_NAME = "CollectionModel"


# TODO: Validate
class CollectionId(RecordingId[TrivialMinus]):
    collection_id: str

    # TODO: Validate
    def download(self, client: TrivialMinus) -> str:
        return client.collection.download(self.collection_id)


COLLECTION_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, CollectionId)


# TODO: Validate
def generate_collection(client: TrivialMinus) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, COLLECTION_IDS, client, ".html")
    rebuild_model(
        GENERATOR_PATHS,
        MODEL_NAME,
        CollectionId,
        extract_collection,
        ".html",
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_collection(TrivialMinus(build_client_automatically()))

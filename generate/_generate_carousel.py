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
from trivial_minus.carousel import extract_carousel
from trivial_minus.exceptions import TrivialMinusError

MODEL_NAME = "CarouselModel"


# TODO: Validate
class CarouselId(RecordingId[TrivialMinus]):
    collection_id: str
    title: str

    # TODO: Validate
    def recording_name(self) -> str:
        return f"{self.collection_id}-{self.title}"

    # TODO: Validate
    def download(self, client: TrivialMinus) -> str:
        """Download the carousel, whose token the collection page carries.

        Raises:
            TrivialMinusError: If the collection has no carousel by that title.
        """
        carousels = client.collection(self.collection_id).carousels
        for carousel in carousels:
            if carousel.title == self.title:
                return client.carousel.download(
                    self.collection_id,
                    token=carousel.token,
                )
        msg = f"{self.collection_id} has no carousel called {self.title}"
        raise TrivialMinusError(msg)


CAROUSEL_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, CarouselId)


# TODO: Validate
def generate_carousel(client: TrivialMinus) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, CAROUSEL_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, CarouselId, extract_carousel)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_carousel(TrivialMinus(build_client_automatically()))

# TODO: Validate
import pytest
from get_around import build_client_automatically

from trivial_minus import TrivialMinus


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> TrivialMinus:
    return TrivialMinus(build_client_automatically())

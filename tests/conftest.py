import pytest
from get_around import build_client_automatically

from trivial_minus import TrivialMinus


@pytest.fixture(scope="session")
def client() -> TrivialMinus:
    return TrivialMinus(get_around_client=build_client_automatically())

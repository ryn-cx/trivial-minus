import pytest
from get_around import build_client_automatically

from trivialminus import TrivialMinus


@pytest.fixture(scope="session")
def client() -> TrivialMinus:
    return TrivialMinus(get_around_client=build_client_automatically())

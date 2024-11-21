import pytest

from app.src.cases import DetectMutantResponse


@pytest.fixture
def detect_mutant_response_data_factory(faker) -> callable:
    def _factory(is_mutant: bool) -> DetectMutantResponse:
        return DetectMutantResponse(is_mutant=is_mutant)

    return _factory

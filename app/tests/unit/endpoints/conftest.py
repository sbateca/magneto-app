import pytest

from app.src.cases import DetectMutantResponse, GetDNAVerificationStatisticsResponse


@pytest.fixture
def detect_mutant_response_data_factory(faker) -> callable:
    def _factory(is_mutant: bool) -> DetectMutantResponse:
        return DetectMutantResponse(is_mutant=is_mutant)

    return _factory


@pytest.fixture
def get_dna_verification_statistics_response_data_factory(faker) -> callable:
    def _factory(
        count_mutant_dna: int, count_human_dna: int, ratio: float
    ) -> GetDNAVerificationStatisticsResponse:
        return GetDNAVerificationStatisticsResponse(
            count_mutant_dna=count_mutant_dna, count_human_dna=count_human_dna, ratio=ratio
        )

    return _factory

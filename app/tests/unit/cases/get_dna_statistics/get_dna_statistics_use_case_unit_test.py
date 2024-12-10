import pytest

from app.src.cases import GetDNAVerificationStatisticsCase
from app.src.domain.domain_objects import DNASequence
from app.src.exceptions._mutant_exceptions import (
    GetAllDnaSequencesException,
    GetDNAVerificationStatisticsException,
)


class TestGetDNAStatisticsUseCase:
    @pytest.mark.asyncio
    async def test__get_dna_statistics_returns_sequences__when_there_are_sequences(
        self, detect_mutant_case_dependencies_factory
    ):
        test_data = [
            DNASequence(id="123", dna=["ATCG", "ATCG"], is_mutant=False),
            DNASequence(id="456", dna=["ATCG", "ATCG"], is_mutant=False),
            DNASequence(id="789", dna=["ATCG", "ATCG"], is_mutant=True),
        ]
        expected_count_mutant_dna = 1
        expected_count_human_dna = 2
        expected_ratio = 0.5
        dependencies = detect_mutant_case_dependencies_factory(sequences=test_data)
        case = GetDNAVerificationStatisticsCase(**dependencies)

        response = await case()

        assert response.count_mutant_dna == expected_count_mutant_dna
        assert response.count_human_dna == expected_count_human_dna
        assert response.ratio == expected_ratio

    @pytest.mark.asyncio
    async def test__get_dna_statistics__returns_zero_values__when_there_are_no_sequences(
        self, detect_mutant_case_dependencies_factory
    ):
        dependencies = detect_mutant_case_dependencies_factory()
        case = GetDNAVerificationStatisticsCase(**dependencies)

        response = await case()

        assert response.count_mutant_dna == 0
        assert response.count_human_dna == 0
        assert response.ratio == 0

    @pytest.mark.asyncio
    async def test__get_dna_statistics__raise_an_exception_when_calculate_statistics(
        self, mocker, detect_mutant_case_dependencies_factory
    ):
        expected_error_message = "An error occurred"
        dependencies = detect_mutant_case_dependencies_factory()
        case = GetDNAVerificationStatisticsCase(**dependencies)
        case.calculate_statistics = mocker.Mock(
            side_effect=GetDNAVerificationStatisticsException(expected_error_message)
        )

        with pytest.raises(GetDNAVerificationStatisticsException) as error:
            await case()

        assert expected_error_message in str(error.value)

    @pytest.mark.asyncio
    async def test__get_dna_statistics__raise_an_exception__when_get_all_sequences_fails(
        self, mocker, detect_mutant_case_dependencies_factory
    ):
        expected_error_message = "An error occurred"
        dependencies = detect_mutant_case_dependencies_factory()
        dependencies["detect_mutant_repository"].get_all_sequences = mocker.AsyncMock(
            side_effect=GetAllDnaSequencesException(expected_error_message)
        )
        case = GetDNAVerificationStatisticsCase(**dependencies)

        with pytest.raises(GetAllDnaSequencesException) as error:
            await case()

        assert expected_error_message in str(error.value)

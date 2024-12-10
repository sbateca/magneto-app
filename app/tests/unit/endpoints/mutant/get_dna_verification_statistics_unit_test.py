from typing import Callable

import pytest
from pytest_mock import MockerFixture

from app.src.exceptions._mutant_exceptions import GetDNAVerificationStatisticsException
from app.web_app.routes._stats import get_dna_statistics


class TestDetectMutant:
    @pytest.fixture
    def dependencies_factory(
        self,
        mocker: MockerFixture,
        get_dna_verification_statistics_response_data_factory,
    ):
        def _factory(count_mutant_dna: int, count_human_dna: int, ratio: float):
            return {
                "get_dna_statistics_use_case": mocker.AsyncMock(
                    return_value=get_dna_verification_statistics_response_data_factory(
                        count_mutant_dna=count_mutant_dna,
                        count_human_dna=count_human_dna,
                        ratio=ratio,
                    )
                ),
            }

        return _factory

    @pytest.mark.asyncio
    async def test__get_dna_statistics_returns_successful_dict_when_successful(
        self, dependencies_factory: Callable
    ):
        expected_response = {
            "count_mutant_dna": 1,
            "count_human_dna": 2,
            "ratio": 0.5,
        }
        dependencies_factory = dependencies_factory(**expected_response)
        response = await get_dna_statistics(**dependencies_factory)

        assert response.__dict__ == expected_response

    @pytest.mark.asyncio
    async def test__get_dna_statistics_raise_exception_when_use_case_raises_exception(
        self, dependencies_factory: Callable
    ):
        test_data = {
            "count_mutant_dna": 1,
            "count_human_dna": 2,
            "ratio": 0.5,
        }
        dependencies = dependencies_factory(**test_data)
        dependencies["get_dna_statistics_use_case"].side_effect = (
            GetDNAVerificationStatisticsException("An error occurred while getting statistics")
        )

        with pytest.raises(GetDNAVerificationStatisticsException):
            await get_dna_statistics(**dependencies)

        dependencies["get_dna_statistics_use_case"].assert_called_once_with()

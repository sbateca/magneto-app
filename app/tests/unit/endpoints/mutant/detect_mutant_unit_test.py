from typing import Callable

import pytest
from pytest_mock import MockerFixture

from app.src.exceptions._mutant_exceptions import NotMutantException
from app.web_app.routes._mutant import detect_mutant


class TestDetectMutant:
    @pytest.fixture
    def dependencies_factory(
        self,
        mocker: MockerFixture,
        detect_mutant_request_with_valid_dna,
        detect_mutant_response_data_factory,
    ):
        def _factory():
            return {
                "detect_mutant_request": detect_mutant_request_with_valid_dna,
                "detect_mutant_case": mocker.AsyncMock(
                    return_value=detect_mutant_response_data_factory(is_mutant=True)
                ),
            }

        return _factory

    @pytest.mark.asyncio
    async def test__detect_mutant_returns_successful_dict_when_successful(
        self, dependencies_factory: Callable
    ):
        expected_response = {"is_mutant": True}
        dependencies = dependencies_factory()
        response = await detect_mutant(**dependencies)

        assert response.__dict__ == expected_response

    @pytest.mark.asyncio
    async def test__detect_mutant_raised_exception_when_use_case_raises_exception(
        self, dependencies_factory: Callable
    ):
        dependencies = dependencies_factory()
        dependencies["detect_mutant_case"].side_effect = NotMutantException(
            status_code=403, detail="Error message"
        )

        with pytest.raises(NotMutantException):
            await detect_mutant(**dependencies)

        dependencies["detect_mutant_case"].assert_called_once_with(
            request=dependencies["detect_mutant_request"]
        )

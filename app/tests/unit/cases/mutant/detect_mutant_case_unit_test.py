import pytest
from pytest_mock import MockerFixture

from app.src.cases import DetectMutantUseCase
from app.src.cases.detect_mutant._request import DetectMutantRequest
from app.src.exceptions._mutant_exceptions import MutantException, NotMutantException


class TestDetectMutantCase:
    @pytest.mark.asyncio
    async def test__detect_mutant_returns_true__when_dna_is_mutant(
        self, detect_mutant_request_with_valid_dna
    ):
        case = DetectMutantUseCase()

        response = await case(request=detect_mutant_request_with_valid_dna)

        assert response.is_mutant is True

    @pytest.mark.asyncio
    async def test__detect_mutant_raise_exception_with_message_and_403_status__when_dna_is_not_mutant(  # noqa E501
        self, detect_mutant_request_data_factory
    ):
        request_test_data = detect_mutant_request_data_factory(
            dna_characters=["A", "T", "C", "G"], string_size=6, list_size=6
        )
        expected_error_message = "DNA is not mutant"
        expected_status_code = 403
        request = DetectMutantRequest(**request_test_data)
        case = DetectMutantUseCase()

        with pytest.raises(NotMutantException) as error:
            await case(request=request)

        assert error.value.status_code == expected_status_code
        assert error.value.detail == expected_error_message

    @pytest.mark.asyncio
    async def test__detect_mutant_raise_exception_with_message__when_exception_occurs(
        self, mocker: MockerFixture, detect_mutant_request_with_valid_dna
    ):
        case = DetectMutantUseCase()
        mocker.patch.object(case, "_is_mutant", side_effect=MutantException("Some exception"))

        with pytest.raises(MutantException) as error:
            await case(request=detect_mutant_request_with_valid_dna)

        assert "An error occurred while detecting mutant" in str(error.value)

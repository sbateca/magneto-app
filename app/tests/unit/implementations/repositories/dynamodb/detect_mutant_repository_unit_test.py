from unittest.mock import AsyncMock

import pytest
from pytest_mock import MockerFixture

from app.src.exceptions._mutant_exceptions import (
    CreateDnaSequenceException,
    GetAllDnaSequencesException,
)


class TestDynamoDetectMutantRepository:
    @pytest.mark.asyncio
    async def test__save_sequence_successfully(
        self,
        mocker: MockerFixture,
        dynamo_detect_mutant_repository_data_factory,
        dynamo_detect_mutant_repository_dependencies_factory,
    ):
        test_data = dynamo_detect_mutant_repository_data_factory()
        dependencies = dynamo_detect_mutant_repository_dependencies_factory(test_data=test_data)
        repository = dependencies["repository"]
        mock_save_sequence = mocker.patch.object(
            repository, "save_sequence", new_callable=AsyncMock
        )

        await repository.save_sequence(
            dna=test_data["items"][0]["dna"], is_mutant=test_data["items"][0]["is_mutant"]
        )

        mock_save_sequence.assert_called_once_with(
            dna=test_data["items"][0]["dna"], is_mutant=test_data["items"][0]["is_mutant"]
        )

    @pytest.mark.asyncio
    async def test__save_sequence_should_raise_an_exception_when_fails(
        self,
        dynamo_detect_mutant_repository_data_factory,
        dynamo_detect_mutant_repository_dependencies_factory,
    ):
        test_data = dynamo_detect_mutant_repository_data_factory()
        dependencies = dynamo_detect_mutant_repository_dependencies_factory(test_data=test_data)
        repository = dependencies["repository"]
        expected_error_message = "An error occurred while saving sequence: Error message"
        repository.dynamodb_client.save = AsyncMock(
            side_effect=CreateDnaSequenceException("Error message")
        )

        with pytest.raises(CreateDnaSequenceException) as exception:
            await repository.save_sequence(
                dna=test_data["items"][0]["dna"], is_mutant=test_data["items"][0]["is_mutant"]
            )

        assert str(exception.value) == expected_error_message

    @pytest.mark.asyncio
    async def test__get_all_sequences_return_sequences_successfully(
        self,
        dynamo_detect_mutant_repository_data_factory,
        dynamo_detect_mutant_repository_dependencies_factory,
    ):
        test_data = dynamo_detect_mutant_repository_data_factory(has_id=True)
        dependencies = dynamo_detect_mutant_repository_dependencies_factory(test_data=test_data)
        repository = dependencies["repository"]

        sequences = await repository.get_all_sequences()

        assert sequences == test_data["dna_sequences"]

    @pytest.mark.asyncio
    async def test__get_all_sequences_return_empty_when_sequences_does_not_exist(
        self,
        dynamo_detect_mutant_repository_data_factory,
        dynamo_detect_mutant_repository_dependencies_factory,
    ):
        test_data = dynamo_detect_mutant_repository_data_factory(has_id=True)
        dependencies = dynamo_detect_mutant_repository_dependencies_factory(test_data=test_data)
        repository = dependencies["repository"]
        repository.dynamodb_client.get_all = AsyncMock(return_value=[])

        sequences = await repository.get_all_sequences()

        assert sequences == []


@pytest.mark.asyncio
async def test__get_all_sequences_should_raise_an_exception_when_fails(
    dynamo_detect_mutant_repository_data_factory,
    dynamo_detect_mutant_repository_dependencies_factory,
):
    test_data = dynamo_detect_mutant_repository_data_factory(has_id=True)
    dependencies = dynamo_detect_mutant_repository_dependencies_factory(test_data=test_data)
    repository = dependencies["repository"]
    expected_error_message = "An error occurred while getting all sequences: Error message"
    repository.dynamodb_client.get_all = AsyncMock(
        side_effect=GetAllDnaSequencesException("Error message")
    )

    with pytest.raises(GetAllDnaSequencesException) as exception:
        await repository.get_all_sequences()

    assert str(exception.value) == expected_error_message

from typing import Callable, Dict

import pytest
from faker import Faker
from pytest_mock import MockerFixture

from app.implementations.repositories.dynamodb.detect_mutant_repository import (
    DynamoDetectMutantRepository,
)
from app.src.domain.domain_objects._dna_sequence import DNASequence


@pytest.fixture
def test_setup(mocker: MockerFixture):
    table = mocker.AsyncMock()
    resource = mocker.AsyncMock(Table=mocker.AsyncMock(return_value=table))

    resource_manager = mocker.AsyncMock(
        __aenter__=mocker.AsyncMock(return_value=resource),
        __aexit__=mocker.AsyncMock(return_value=None),
    )

    session = mocker.patch(
        "aioboto3.Session",
        return_value=mocker.AsyncMock(resource=mocker.Mock(return_value=resource_manager)),
    )

    return {
        "table": table,
        "resource": resource,
        "session": session,
    }


@pytest.fixture
def dynamo_detect_mutant_repository_data_factory() -> Callable:
    def _factory(has_id: bool = False) -> Dict:
        fake = Faker()
        items = [
            {
                "id": "123" if has_id else None,
                "dna": [fake.word() for _ in range(4)],
                "is_mutant": fake.boolean(),
            }
        ]

        return {
            "items": items,
            "dna_sequences": [
                DNASequence(
                    id="123",
                    dna=item["dna"],
                    is_mutant=item["is_mutant"],
                )
                for item in items
            ],
        }

    return _factory


@pytest.fixture
def dynamo_detect_mutant_repository_dependencies_factory(mocker: MockerFixture) -> Callable:
    def _factory(test_data: Dict) -> Dict:
        dynamodb_client = mocker.Mock(
            save=mocker.AsyncMock(),
            get_all=mocker.AsyncMock(return_value=test_data["items"]),
        )
        repository = DynamoDetectMutantRepository(dynamodb_client=dynamodb_client)
        return {
            "repository": repository,
        }

    return _factory

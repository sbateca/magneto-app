from typing import Any, Callable, Sequence

import pytest
from faker import Faker
from pytest_mock import MockerFixture

from app.src.cases.detect_mutant._request import DetectMutantRequest


@pytest.fixture
def detect_mutant_request_data_factory(faker: Faker) -> Callable:
    def _factory(
        dna_characters: list[str], string_size: int = 4, list_size: int = 4
    ) -> DetectMutantRequest:
        def generate_dna_string() -> str:
            return "".join([faker.random.choice(dna_characters) for _ in range(string_size)])

        dna = [generate_dna_string() for _ in range(list_size)]

        return {"dna": dna}

    return _factory


@pytest.fixture
def detect_mutant_case_dependencies_factory(mocker: MockerFixture) -> Callable:
    def __factory(sequences: list[Sequence] = []) -> dict[str, Any]:
        return {
            "detect_mutant_repository": mocker.Mock(
                save_sequence=mocker.AsyncMock(),
                get_all_sequences=mocker.AsyncMock(return_value=sequences),
            )
        }

    return __factory

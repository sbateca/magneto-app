from typing import Callable

import pytest
from faker import Faker

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

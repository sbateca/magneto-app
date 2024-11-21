import pytest

from app.src.cases import DetectMutantRequest


@pytest.fixture
def detect_mutant_request_with_valid_dna() -> DetectMutantRequest:
    dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    return DetectMutantRequest(dna=dna)

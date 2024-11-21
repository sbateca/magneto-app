import json
from typing import Callable

import pytest

from app.src.cases.detect_mutant._request import DetectMutantRequest


class TestDetectMutantRequest:
    @pytest.mark.parametrize(
        "dna_characters,string_size,list_size,expected_error_message",
        [
            (["A", "T", "C", "G"], 4, 2, "Value error, DNA must have at least 4 strings"),
            (["A", "T", "C", "G"], 4, 6, "Value error, DNA strings must have the same size"),
            (["W", "X", "Y", "Z"], 4, 4, "Value error, DNA strings must have valid characters"),
            (["w", "x", "y", "z"], 4, 4, "Value error, DNA strings must have valid characters"),
        ],
    )
    def test__raises_validation_error__when_dna_has_invalid_values(
        self,
        detect_mutant_request_data_factory: Callable,
        dna_characters: list[str],
        string_size: int,
        list_size: int,
        expected_error_message: str,
    ):
        test_data = detect_mutant_request_data_factory(
            dna_characters=dna_characters, string_size=string_size, list_size=list_size
        )

        with pytest.raises(ValueError) as error:
            DetectMutantRequest(**test_data)

        validation_errors = json.loads(error.value.json())
        error_message = validation_errors[0]["msg"]
        assert error_message == expected_error_message

    def test__raises_validation_error__when_dna_has_spaces(
        self, detect_mutant_request_data_factory: Callable
    ):
        dna_characters = ["A", "T", "C", "G"]
        test_data = detect_mutant_request_data_factory(
            dna_characters=dna_characters, string_size=4, list_size=4
        )
        test_data["dna"][0] = "A T C G"

        with pytest.raises(ValueError) as error:
            DetectMutantRequest(**test_data)

        validation_errors = json.loads(error.value.json())
        error_message = validation_errors[0]["msg"]
        assert error_message == "Value error, DNA strings must not have spaces"

    def test__request_is_valid_instance__when_dna_format_is_valid(
        self, detect_mutant_request_data_factory: Callable
    ):
        dna_characters = ["A", "T", "C", "G"]
        test_data = detect_mutant_request_data_factory(
            dna_characters=dna_characters, string_size=4, list_size=4
        )

        detect_mutant_request_instance = DetectMutantRequest(**test_data)

        assert isinstance(detect_mutant_request_instance, DetectMutantRequest)

from typing import List

from pydantic import BaseModel, field_validator

_VALID_DNA_CHARACTERS = ["A", "T", "C", "G"]


class DetectMutantRequest(BaseModel):
    dna: List[str]

    @field_validator("dna")
    def check_dna_size(cls, value: List[str]) -> List[str]:
        dna_size = len(value) if value else 0
        if dna_size < 4:
            raise ValueError("DNA must have at least 4 strings")
        for dna_string in value:
            if len(dna_string) != dna_size:
                raise ValueError("DNA strings must have the same size")
        return value

    @field_validator("dna")
    def check_dna_characters(cls, value: List[str]) -> List[str]:
        for dna_string in value:
            for dna_character in dna_string:
                if dna_character not in _VALID_DNA_CHARACTERS:
                    raise ValueError("DNA strings must have valid characters")
        return value

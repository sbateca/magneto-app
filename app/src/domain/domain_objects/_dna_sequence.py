from typing import List

from pydantic import BaseModel


class DNASequence(BaseModel):
    id: str
    dna: List[str]
    is_mutant: bool

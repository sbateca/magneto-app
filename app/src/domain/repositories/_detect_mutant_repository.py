import abc
from typing import List

from app.src.domain import DNASequence


class DetectMutantRepository(abc.ABC):

    @abc.abstractmethod
    async def save_sequence(self, dna: List[str], is_mutant: bool) -> None:
        pass

    @abc.abstractmethod
    async def get_all_sequences(self) -> List[DNASequence]:
        pass

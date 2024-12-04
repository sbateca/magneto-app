import uuid
from typing import List

from app.implementations.clients._dynamodb_client import DynamoDBClient
from app.src.domain.domain_objects import DNASequence
from app.src.domain.repositories import DetectMutantRepository
from app.src.exceptions import CreateDnaSequenceException, GetAllDnaSequencesException


class DynamoDetectMutantRepository(DetectMutantRepository):
    def __init__(self, dynamodb_client: DynamoDBClient):
        self.dynamodb_client = dynamodb_client

    async def save_sequence(self, dna: List[str], is_mutant: bool) -> None:
        dna_sequence_item = {"id": str(uuid.uuid4()), "dna": dna, "is_mutant": is_mutant}
        try:
            await self.dynamodb_client.save(item=dna_sequence_item)
        except CreateDnaSequenceException as exception:
            raise CreateDnaSequenceException(
                f"An error occurred while saving sequence: {str(exception)}"
            )

    async def get_all_sequences(self) -> List[DNASequence]:
        try:
            sequences = await self.dynamodb_client.get_all()
            if not sequences:
                return []
            return [
                DNASequence(
                    id=sequence["id"], dna=sequence["dna"], is_mutant=sequence["is_mutant"]
                )
                for sequence in sequences
            ]
        except GetAllDnaSequencesException as exception:
            raise GetAllDnaSequencesException(
                f"An error occurred while getting all sequences: {str(exception)}"
            )

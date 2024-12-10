from typing import Any, Dict, List

from app.src.domain.domain_objects._dna_sequence import DNASequence
from app.src.domain.repositories._detect_mutant_repository import DetectMutantRepository
from app.src.exceptions._mutant_exceptions import GetDNAVerificationStatisticsException

from ._response import GetDNAVerificationStatisticsResponse


class GetDNAVerificationStatisticsCase:
    def __init__(self, detect_mutant_repository: DetectMutantRepository):
        self.detect_mutant_repository = detect_mutant_repository

    async def __call__(self) -> GetDNAVerificationStatisticsResponse:
        try:
            verified_sequences = await self.detect_mutant_repository.get_all_sequences()
            stats_data = self.calculate_statistics(verified_sequences)
            return GetDNAVerificationStatisticsResponse(**stats_data)
        except GetDNAVerificationStatisticsException as exception:
            raise GetDNAVerificationStatisticsException(
                f"An error occurred while getting statistics {str(exception)}"
            )

    def calculate_statistics(self, verified_sequences: List[DNASequence]) -> Dict[str, Any]:
        count_human_dna = 0
        count_mutant_dna = 0
        ratio = 0.0

        if not verified_sequences:
            return {
                "count_mutant_dna": count_mutant_dna,
                "count_human_dna": count_human_dna,
                "ratio": ratio,
            }

        for sequence in verified_sequences:
            if sequence.is_mutant:
                count_mutant_dna += 1
            else:
                count_human_dna += 1

        if count_human_dna:
            try:
                ratio = count_mutant_dna / count_human_dna
            except ZeroDivisionError:
                raise GetDNAVerificationStatisticsException("Ratio error: Division by zero")

        return {
            "count_mutant_dna": count_mutant_dna,
            "count_human_dna": count_human_dna,
            "ratio": ratio,
        }

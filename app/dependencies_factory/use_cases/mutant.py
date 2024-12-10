from app.dependencies_factory.repositories import detect_mutant_repository_factory
from app.src.cases import DetectMutantUseCase, GetDNAVerificationStatisticsCase


def detect_mutant_use_case() -> DetectMutantUseCase:
    return DetectMutantUseCase(
        detect_mutant_repository=detect_mutant_repository_factory(),
    )


def get_dna_verifications_statistics_use_case() -> GetDNAVerificationStatisticsCase:
    return GetDNAVerificationStatisticsCase(
        detect_mutant_repository=detect_mutant_repository_factory(),
    )

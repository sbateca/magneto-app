from fastapi import APIRouter, Depends

from app.dependencies_factory.use_cases.mutant import (
    get_dna_verifications_statistics_use_case,
)
from app.src.cases import (
    GetDNAVerificationStatisticsCase,
    GetDNAVerificationStatisticsResponse,
)

statistics_router = APIRouter(prefix="/stats")


@statistics_router.get("/")
async def get_dna_statistics(
    get_dna_statistics_use_case: GetDNAVerificationStatisticsCase = Depends(
        get_dna_verifications_statistics_use_case
    ),
) -> GetDNAVerificationStatisticsResponse:
    return await get_dna_statistics_use_case()

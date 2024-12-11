from fastapi import APIRouter, Depends

from app.dependencies_factory.use_cases import detect_mutant_use_case
from app.src.cases import DetectMutantRequest, DetectMutantResponse, DetectMutantUseCase

mutant_router = APIRouter(prefix="/mutant")


@mutant_router.post("")
async def detect_mutant(
    detect_mutant_request: DetectMutantRequest,
    detect_mutant_case: DetectMutantUseCase = Depends(detect_mutant_use_case),
) -> DetectMutantResponse:
    return await detect_mutant_case(request=detect_mutant_request)

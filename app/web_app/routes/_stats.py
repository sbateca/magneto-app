from typing import Dict

from fastapi import APIRouter

statistics_router = APIRouter(prefix="/stats")


@statistics_router.get("/")
async def get_dna_statistics() -> Dict:
    return {"count_mutant_dna": 40, "count_human_dna": 100, "ratio": 0.4}

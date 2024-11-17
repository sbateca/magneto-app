from typing import Dict

from fastapi import APIRouter

mutant_router = APIRouter(prefix="/mutant")


@mutant_router.post("/")
async def is_mutant() -> Dict:
    return {"is_mutant": True}

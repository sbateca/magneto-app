from pydantic import BaseModel


class DetectMutantResponse(BaseModel):
    is_mutant: bool

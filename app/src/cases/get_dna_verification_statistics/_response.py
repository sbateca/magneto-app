from pydantic import BaseModel


class GetDNAVerificationStatisticsResponse(BaseModel):
    count_mutant_dna: int
    count_human_dna: int
    ratio: float

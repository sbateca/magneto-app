from app.config import Settings
from app.implementations.clients._dynamodb_client import DynamoDBClient


def dynamodb_client_for_mutant_data(settings: Settings) -> DynamoDBClient:
    return DynamoDBClient(
        table=settings.magneto_dna_data_table,
    )

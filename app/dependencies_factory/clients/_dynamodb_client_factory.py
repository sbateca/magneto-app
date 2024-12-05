from app.implementations.clients._dynamodb_client import DynamoDBClient
from config import Settings


def dynamodb_client_for_mutant_data(settings: Settings) -> DynamoDBClient:
    return DynamoDBClient(
        table=settings.magneto_dna_data_table,
    )

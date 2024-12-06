import app.config as config
from app.dependencies_factory.clients._dynamodb_client_factory import (
    dynamodb_client_for_mutant_data,
)
from app.implementations.repositories import DynamoDetectMutantRepository


def detect_mutant_repository_factory() -> DynamoDetectMutantRepository:
    return DynamoDetectMutantRepository(
        dynamodb_client=dynamodb_client_for_mutant_data(settings=config.get_settings())
    )

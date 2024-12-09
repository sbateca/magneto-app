import pytest

from app.implementations.clients._dynamodb_client import DynamoDBClient


class TestSaveMethod:

    @pytest.mark.asyncio
    async def test_save_calls_put_item(self, test_setup):
        dynamo_client = DynamoDBClient(table="test_table")
        item = {"id": "123", "dna": ["ABC", "DEF"], "is_mutant": False}
        test_setup["table"].put_item.return_value = {"ResponseMetadata": {"HTTPStatusCode": 200}}

        result = await dynamo_client.save(item)

        test_setup["table"].put_item.assert_awaited_once_with(Item=item)
        assert result == {"ResponseMetadata": {"HTTPStatusCode": 200}}
        assert test_setup["session"].called
        assert test_setup["resource"].Table.called


class TestGetAllMethod:

    @pytest.mark.asyncio
    async def test_get_all_calls_scan(self, test_setup):
        dynamo_client = DynamoDBClient(table="test_table")
        test_setup["table"].scan.return_value = {
            "Items": [{"id": "123", "dna": ["ABC", "DEF"], "is_mutant": False}]
        }

        result = await dynamo_client.get_all()

        test_setup["table"].scan.assert_awaited_once()
        assert result == [{"id": "123", "dna": ["ABC", "DEF"], "is_mutant": False}]
        assert test_setup["session"].called
        assert test_setup["resource"].Table.called

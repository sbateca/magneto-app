from typing import Dict, List, Union

import aioboto3


class DynamoDBClient:
    def __init__(self, table: str):
        self.table = table

    async def save(self, item: Dict) -> Union[Dict, None]:
        session = aioboto3.Session()
        async with session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table)
            item = await table.put_item(Item=item)
            return item

    async def get_all(self) -> Union[List[dict], None]:
        session = aioboto3.Session()
        async with session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table)
            response = await table.scan()
            return response.get("Items")

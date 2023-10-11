import yaml
import asyncpg
from pathlib import Path

cred_path = Path(__file__).parent.parent.parent / "keys"

async def get_database_connection():
    return await asyncpg.connect(
        user = credentials["user"],
        password = credentials["password"],
        database = credentials["database"],
        host = credentials["host"],
        port = credentials["port"],
    )


class DBManager:
    
    def __init__(self) -> None:
        with open(cred_path / "postgres_keys.yaml", 'r') as f:
            credentials = yaml.safe_load(f)
        self.credentials = credentials
        self.pool = None

    async def setup(self):
        self.pool = await asyncpg.create_pool(
            user=self.credentials["user"],
            password=self.credentials["password"],
            database=self.credentials["database"],
            host=self.credentials["host"],
            port=self.credentials["port"],
        )

    async def close(self):
        if self.pool:
            await self.pool.close()

    async def get_connection(self):
        if not self.pool:
            await self.setup()
        return await self.pool.acquire()
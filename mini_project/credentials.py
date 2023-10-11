import yaml
import asyncpg
from pathlib import Path

cred_path = Path(__file__).parent.parent.parent / "keys"

with open(cred_path / "postgres_keys.yaml", 'r') as f:
            credentials = yaml.safe_load(f)

async def get_database_connection():
    return await asyncpg.connect(
        user = credentials["user"],
        password = credentials["password"],
        database = credentials["database"],
        host = credentials["host"],
        port = credentials["port"],
    )
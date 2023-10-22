import yaml
from pathlib import Path

cred_path = Path(__file__).parent.parent.parent / "keys"

with open(cred_path / "postgres_keys.yaml", 'r') as f:
            credentials = yaml.safe_load(f)

class Settings:
    PROJECT_NAME: str = "My first connection"
    PROJECT_VERSION: str = "0.0.1"

    POSTGRES_USER: str = credentials["user"]
    POSTGRES_PASSWORD = credentials["password"]
    POSTGRES_HOST: str = credentials["host"]
    POSTGRES_PORT: str = credentials["port"]
    POSTGRES_DATABASE: str = credentials["database"]

settings = Settings()

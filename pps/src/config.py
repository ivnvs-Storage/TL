from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    RABBITMQ_URL: str
    TINKOFF_TOKEN: str
    PARQUET_PATH: str = "pps/src/adapters/repository/tinkoff/data"

    class Config:
        env_file = str(Path(__file__).parent.parent.parent / ".env")

settings = Settings() 
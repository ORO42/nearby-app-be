from typing import List
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "My FastAPI App"
    DEBUG: bool = False
    VERSION: str = "0.1.0"
    SQLALCHEMY_DATABASE_URL: str

    AUTH0_DOMAIN: str
    AUTH0_AUDIENCE: str
    ALGORITHMS: List[str]

    class Config:
        env_file = ".env"


settings = Settings()

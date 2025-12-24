import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_PATH: str = os.getenv("MODEL_PATH")
    API_KEY: str = os.getenv("API_KEY")

settings = Settings()
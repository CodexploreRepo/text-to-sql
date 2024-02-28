from functools import lru_cache
from typing import Dict

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Text To SQL"
    app_description: str = (
        "This is to generate SQL commands based on user prompt"
    )
    app_version: str = "0.0.1"
    app_owner: Dict[str, str] = {
        "name": "CodeXplore",
        "email": "quan.ngha95@gmail.com",
        "url": "https://github.com/CodexploreRepo",
    }


@lru_cache
def get_settings():
    return Settings()

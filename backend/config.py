from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Text To SQL"
    admin_email: str = "quan.ngha95@gmail.com"


@lru_cache
def get_settings():
    return Settings()

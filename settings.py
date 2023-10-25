from typing import Self

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str

    @property
    def async_database_url(self: Self) -> str:
        async_database_url = self.database_url.replace(
            "postgresql://",
            "postgresql+asyncpg://",
        )

        if not async_database_url.startswith("postgresql+asyncpg://"):
            raise ValueError("async_database_url must start with postgresql+asyncpg://")

        return async_database_url


settings = Settings()

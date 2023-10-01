from typing import Optional

from decouple import config
from pydantic import SecretStr
from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    APP_NAME: str = config("APP_NAME")
    APP_DESCRIPTION: str = config("APP_DESCRIPTION")
    APP_VERSION: str = config("APP_VERSION")
    CONTACT: dict = {
        "name": config("CONTACT_NAME"),
        "email": config("CONTACT_EMAIL")
    }
    LICENSE_NAME: dict = {"name": config("LICENSE_NAME")}


class CryptSettings(BaseSettings):
    SECRET_KEY: str = config("SECRET_KEY")
    ALGORITHM: str = config("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES")


class PostgresSettings(BaseSettings):
    POSTGRES_USER: str = config("POSTGRES_USER", default="postgres")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD", default="postgres")
    POSTGRES_SERVER: str = config("POSTGRES_SERVER", default="localhost")
    POSTGRES_PORT: str = config("POSTGRES_PORT", default=5432)
    POSTGRES_DB: str = config("POSTGRES_DB", default="postgres")
    POSTGRES_URI: str = f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


class FirstUserSettings(BaseSettings):
    ADMIN_NAME: str = config("ADMIN_NAME", default="admin")
    ADMIN_EMAIL: str = config("ADMIN_EMAIL", default="admin@admin.com")
    ADMIN_USERNAME: str = config("ADMIN_USERNAME", default="admin")
    ADMIN_PASSWORD: str = config("ADMIN_PASSWORD", default="!Ch4ng3Th1sP4ssW0rd!")


class Settings(
    AppSettings, 
    PostgresSettings, 
    CryptSettings, 
    FirstUserSettings
):
    pass


settings = Settings()
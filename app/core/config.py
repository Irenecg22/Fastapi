from pydantic_settings import BaseSettings

class Config(BaseSettings):
    database_url: str | None = None
    debug: bool = False

    class Config:
        env_file = ".env"

config = Config()
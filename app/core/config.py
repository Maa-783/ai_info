from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    PROJECT_NAME: str = "My FastAPI App"
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./app.db"


settings = Settings()
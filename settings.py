from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    DB_ADDRESS: str
    YOOKASSA_ACCOUNT_ID: int
    YOOKASSA_SECRET_KEY: str
    ADMIN_SECRET_KEY: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
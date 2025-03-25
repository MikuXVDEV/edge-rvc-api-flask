from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    rvc_api: str
    host: str
    port: int

    model_config = SettingsConfigDict(env_file='edge-tts-api/.env', env_file_encoding='utf-8')

config = Config()
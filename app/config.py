from pydantic import BaseSettings

class Settings(BaseSettings):
    debug: bool = False
    secret_key: str = 'S#perS3crEt_9999'
    server_port: int = 5000

    class Config:
        env_file = "./.env"


settings = Settings()


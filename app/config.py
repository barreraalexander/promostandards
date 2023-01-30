from pydantic import BaseSettings

class Settings(BaseSettings):
    debug: bool = False
    secret_key: str = 'S#perS3crEt_9999'
    server_port: int = 5005
    service_location: str = 'http://localhost:5005'
    
    database_hostname: str = 'probably_root'
    database_port: int = 5432
    database_password: str = 'secretly_secret'
    database_name: str = 'promostandards'

    # algorithm for creating json web tokens
    algorithm: str

    access_token_expire_minutes: int = 30

    


    class Config:
        env_file = "./.env"


settings = Settings()


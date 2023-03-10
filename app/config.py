from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = "postgres"
    database_port: str = "postgres"
    database_name: str = "postgres"
    database_password: str = "postgres"
    database_username: str = "postgres"
    secret_key: str = "postgres"
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()

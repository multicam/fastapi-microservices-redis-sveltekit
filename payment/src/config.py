from pydantic import BaseSettings


class Settings(BaseSettings):
    redis_host: str
    redis_port: str
    redis_password: str
    inventory_server_url: str = 'https://localhost:8000'

    class Config:
        env_file = ".env"

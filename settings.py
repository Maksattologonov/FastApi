from pydantic.env_settings import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = "postgresql://postgres:postgres@postgres/fastapi_db"
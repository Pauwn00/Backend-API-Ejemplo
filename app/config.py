from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional


class Settings(BaseSettings):
    # Database - puede usar DATABASE_URL directamente o parámetros individuales
    DATABASE_URL: Optional[str] = None
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = ""
    DB_NAME: str = "postgres"
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # App
    APP_NAME: str = "Backend Ejemplo API"
    API_V1_PREFIX: str = "/api/v1"
    
    def get_database_url(self) -> str:
        """
        Retorna la URL de base de datos. Si DATABASE_URL está definida, la usa.
        Si no, construye la URL desde los parámetros individuales.
        """
        if self.DATABASE_URL:
            return self.DATABASE_URL
        else:
            return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()

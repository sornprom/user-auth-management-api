from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM:str
    JWT_EXPIRE_TOKEN: str

    class Config:
        env_file = ".env"

configs = Settings()
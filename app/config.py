from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    magneto_dna_data_table: str

    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    return Settings()

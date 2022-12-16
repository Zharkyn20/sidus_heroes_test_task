import os


class Settings:
    PROJECT_NAME: str = "Zharkyn Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.environ("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.environ("POSTGRES_HOST")
    POSTGRES_PORT: str = os.environ("POSTGRES_PORT")
    POSTGRES_DB: str = os.environ("POSTGRES_DB")
    DATABASE_URL = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
        f"{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )


settings = Settings()

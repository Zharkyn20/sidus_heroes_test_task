from decouple import config


class Settings:
    PROJECT_NAME: str = "Sidus Heroes Test Task"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = config("POSTGRES_USER")
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = config("POSTGRES_HOST")
    POSTGRES_PORT: str = config("POSTGRES_PORT")
    POSTGRES_DB: str = config("POSTGRES_DB")
    DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
        f"{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )


settings = Settings()

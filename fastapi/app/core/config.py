import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_USERNAME = os.getenv("DB_USER")
    DATABASE_PASSWORD = os.getenv("DB_PASSWORD")
    URL_PROD = os.getenv("DB_URL_PROD")
    URL_LOCAL = os.getenv("DB_URL_LOCAL")
    DATABASE_NAME = os.getenv("DB_NAME")
    DATABASE_PORT = os.getenv("DB_PORT")

    DATABASE_URL = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{URL_LOCAL}:{DATABASE_PORT}/{DATABASE_NAME}"
    APP_NAME = "Ayo Lulus Den!!! Aku Padamu"

settings = Settings()

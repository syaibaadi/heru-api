import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://deden:K0d!r@103.250.11.13:33065/deden_project")
    APP_NAME = "Ayo Lulus Den!!! Aku Padamu"

settings = Settings()

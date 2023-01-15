import os

API_TITLE = os.getenv("API_TITLE", "Default API Title")
API_VERSION = "v1"

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SERVER = os.getenv("DB_SERVER")
DB_PORT = os.getenv("DB_PORT")
DB_DATABASE = os.getenv("DB_DATABASE")

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{int(DB_PORT)}/{DB_DATABASE}"
print(SQLALCHEMY_DATABASE_URI)
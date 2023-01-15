#!/usr/bin/env python
import os
from dotenv import load_dotenv
from pathlib import Path

from settings import PATH_ENV

def set_env():
    #print("set_env---",PATH_ENV)
    dotenv_path = Path(PATH_ENV)
    load_dotenv(dotenv_path=dotenv_path)

set_env()

DB_SERVER = os.getenv("DB_SERVER", "localhost")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "pass")
DB_PORT = os.getenv("DB_PORT", 3309)
DB_DATABASE = os.getenv("DB_DATABASE", "db")

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{int(DB_PORT)}/{DB_DATABASE}"
)

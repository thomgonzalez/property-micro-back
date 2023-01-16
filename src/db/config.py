# -*- coding: utf-8 -*-
import os


def get_database_url():
    DB_SERVER = os.getenv("DB_SERVER", "localhost")
    DB_USER = os.getenv("DB_USER", "user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "pass")
    DB_PORT = os.getenv("DB_PORT", 3309)
    DB_DATABASE = os.getenv("DB_DATABASE", "db")

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{int(DB_PORT)}/{DB_DATABASE}"
    return SQLALCHEMY_DATABASE_URI

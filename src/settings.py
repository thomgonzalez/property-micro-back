# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_ENV = os.path.join(BASE_DIR, ".db.env")


def set_env(path=None):
    # print("set_env---",PATH_ENV)
    dotenv_path = Path(PATH_ENV)
    load_dotenv(dotenv_path=dotenv_path)

# -*- coding: utf-8 -*-
import os
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path_env = os.path.join(BASE_DIR, ".env")

dotenv_path = Path(path_env)
load_dotenv(dotenv_path=dotenv_path)

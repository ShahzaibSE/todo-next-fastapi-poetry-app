from starlette.config import Config
from starlette.datastructures import Secret
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())

try:
    config = Config(".env")
    print(".Env file is in the path")
except FileNotFoundError:
    config = Config()
    

# NEON_DATABASE_URL = os.getenv("NEON_DATABASE_URL") 
DATABASE_URL = config("NEON_DATABASE_URL", cast=Secret)

# TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=Secret)


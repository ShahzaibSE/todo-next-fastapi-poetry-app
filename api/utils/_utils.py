from passlib.context import CryptContext
from jose import jwt
from typing import Union, Any
from datetime import timedelta, datetime
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

password_context = CryptContext(schemes=["bcrypt"], depreciated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']   # should be kept secret
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']    # should be kept secret


def hash_password(password:str)->str:
    return password_context.hash(password)

def verify_password(password:str, hashed_password:str)->bool:
    return password_context.verify(password,hashed_password)


def create_access_token_jwt()->str:
    pass

def create_refresh_token_jwt()->str:
    pass
from passlib.context import CryptContext
from jose import jwt
from typing import Union, Any
from datetime import timedelta, datetime, timezone
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

password_context = CryptContext(schemes=["bcrypt"])

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']   # should be kept secret
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']    # should be kept secret


def hash_password(password:str)->str:
    return password_context.hash(password)

def verify_password(password:str, hashed_password:str)->bool:
    return password_context.verify(password,hashed_password)


def create_access_token_jwt(subject:Union[str,Any], expires_delta:str)->str:
    try:
        print("Creating access token")
        if expires_delta is not None:
            expires_delta = datetime.now(timezone.utc) + expires_delta
        else:
            expires_delta = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {"exp":expires_delta, "sub":str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except:
        return {
            "status":False,
            "message":"Couldn't create access token for the first time",
            "isError":True
        }

def create_refresh_token_jwt(subject:Union[str,Any], expires_delta:str)->str:
    try:
        print("Create Refresh Token")
        if expires_delta is not None:
            expires_delta = datetime.now(timezone.utc) + expires_delta
        else:
            expires_delta = datetime.now(timezone.utc) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
        to_encode = {"exp":expires_delta, "sub":str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except:
        return {
            "status":False,
            "message":"Couldn't refresh token",
            "isError":True
        }
from passlib.context import CryptContext
from jose import jwt, JWTError
from typing import Annotated, Any
from datetime import timedelta, datetime, timezone
import os
from dotenv import load_dotenv, find_dotenv
from fastapi import status, Depends, HTTPException
from sqlmodel import Session, select
from api._database import startSession
from api.models._user_model import User

_ = load_dotenv(find_dotenv())

password_context = CryptContext(schemes=["bcrypt"])

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']   # should be kept secret
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']    # should be kept secret
SECRET_KEY = "090e3ba2a1d93d843715cb8cec50e1730e20991c62b04e7e249ef9b378d1490c"


def hash_password(password:str)->str:
    return password_context.hash(password)

def verify_password(password:str, hashed_password:str)->bool:
    return password_context.verify(password,hashed_password)

        
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=7)  # Example: 7 days expiry for refresh token
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def validate_refresh_token(token:str, session:Annotated[Session, Depends(startSession)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email:str|None = payload.get('sub')
        #
        if not email:
            raise credentials_exception
    except:
        raise JWTError
    user = session.exec(select(User).filter(User.email == email)).first()
    print("User: {0}".format(user))
    if user is None:
        raise credentials_exception
    return user
    
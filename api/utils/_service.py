from api._database import startSession
from sqlmodel import SQLModel, Session
from _utils import verify_password
from typing import Annotated
from fastapi import Depends
from models import User


def authenticate_user(email:str, password:str, session: Annotated[Session, Depends(startSession)])->bool:
    user:User = session.get({"email":email})
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
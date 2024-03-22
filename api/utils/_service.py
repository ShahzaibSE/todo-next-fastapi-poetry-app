from api._database import startSession
from sqlmodel import SQLModel, Session, select
from api.utils._utils import verify_password
from typing import Annotated
from fastapi import Depends
from api.models._user_model import User
from fastapi.security import OAuth2PasswordBearer


outh2_password = OAuth2PasswordBearer(tokenUrl="token")

async def authenticate_user(username:str, password:str, session: Annotated[Session, Depends(startSession)])->bool:
    user:User = session.exec(select(User).filter([User.firstname == username, User.password == password])).first()
    print("Existing user found to login")
    print(user)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
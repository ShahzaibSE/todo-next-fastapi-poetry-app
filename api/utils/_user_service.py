from api._database import startSession
from sqlmodel import Session, select
from api.utils._utils import verify_password
from typing import Annotated
from fastapi import Depends
from api.models._user_model import User
from fastapi.security import OAuth2PasswordBearer
from fastapi import status


outh2_password = OAuth2PasswordBearer(tokenUrl="token")

async def authenticate_user(username:str, password:str, session: Annotated[Session, Depends(startSession)])->bool:
    user:User = session.exec(select(User).filter([User.username == username, User.password == password])).first()
    print("Existing user found to login")
    print(user)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

async def getUsername(username:str, session:Annotated[Session, Depends(startSession)])->str:
    try:
        user:User = session.exec(select(User).filter(User.username == username)).first()
        return user.username
    except:
        return {
            "status":status.HTTP_401_UNAUTHORIZED,
            "message":"User not found"
        }
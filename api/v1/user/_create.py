from fastapi import APIRouter, Depends, Response, HTTPException, status
from api._database import startSession
from api.models._user_model import User, UserResponse
from typing import Annotated, Union
from sqlmodel import Session, select
from api.utils._utils import hash_password

session = startSession()
signup_route = APIRouter()


# @signup_route.post("/signup", response_model=User)
# def signup(user: User, session: Annotated[Session, Depends(startSession)]):
#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     return user

@signup_route.post("/signup", response_model=UserResponse)
async def create_user(user:User, session: Annotated[Session, Depends(startSession)]):
    try:
       print("Creating new user")
       print(user)
       existedUser:User = session.exec(select(User).filter(User.username == user.username)).first()
       print(existedUser)
       if existedUser:
            return {
                "status":status.HTTP_202_ACCEPTED,
                "message":"User already exist",
                "data":existedUser
            }
       else:
           hashedPassword = hash_password(user.password)
           user.password = hashedPassword
           session.add(user) 
           session.commit()
           session.refresh(user)
           return {
               "status":status.HTTP_201_CREATED,
               "message":"User Signed Up Successfully",
               "data":user
               } 
    except:
        return Response(status_code=500, content="Couldn't create user successfully")

from fastapi import APIRouter, Depends, Response, HTTPException, status
from api._database import startSession
from api.models._user_model import User
from typing import Annotated
from sqlmodel import Session
from api.utils._utils import hash_password

session = startSession()
signup_route = APIRouter()


# @signup_route.post("/signup", response_model=User)
# def signup(user: User, session: Annotated[Session, Depends(startSession)]):
#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     return user

@signup_route.post("/signup", response_model=User)
async def create_user(user:User, session: Annotated[Session, Depends(startSession)]):
    try:
       existedUser = session.get({"email":user.email})
       if existedUser is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exist"
            )
       else:
           hashedPassword = hash_password(user.password)
           user.password = hashedPassword
           session.add(user) 
           session.commit()
           session.refresh(user)
           return user 
    except:
        return Response(status_code=500, content="Couldn't create user successfully")
from fastapi import APIRouter, Depends, Response, HTTPException, status
from api._database import startSession
from api.models._user_model import Token, User
from fastapi.security import OAuth2PasswordRequestForm
from api.utils._service import authenticate_user
from typing import Annotated
from datetime import timedelta
from api.utils._utils import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES, create_access_token_jwt, create_refresh_token_jwt
from sqlmodel import Session, select

session = startSession()
login_route = APIRouter()

# @login_route.post("/login", summary="Create access and refresh token for user", response_model=Token)
# async def login(formData:Annotated[OAuth2PasswordRequestForm, Depends()])->Token:
#     try:
#         user:User = authenticate_user(formData.username, formData.password)
#         print("User to authenticate")
#         print(user)
#         if not user:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Incorrect username or password",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
#         access_token = create_access_token_jwt(user.email) 
#         refresh_token = create_refresh_token_jwt(user.email)
#         return Token(access_token=access_token, refresh_token=refresh_token, token_type="bearer")
#     except:
#         return {
#             "status":status.HTTP_401_UNAUTHORIZED,
#             "message":"Account doesn't exist"
#         }

@login_route.post("/login", summary="Create access and refresh token for user", response_model=User)
async def login(user:User, session:Annotated[Session,Depends(startSession)]):
    try:
        user = session.exec(select(User).filter(User.username==user.username)).first()
        return user
    except:
        return {
            "status":status.HTTP_401_UNAUTHORIZED,
            "message":"Account doesn't exist"
        }
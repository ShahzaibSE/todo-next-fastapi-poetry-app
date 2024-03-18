from fastapi import APIRouter, Depends, Response, HTTPException, status
from _database import startSession
from models._user_model import User
from typing import Annotated
from sqlmodel import Session
from utils._utils import create_access_token_jwt, create_refresh_token_jwt

session = startSession()
login_route = APIRouter()

@login_route.post("", summary="Create access and refresh token for user", response_model=User)
def login(user:User, session:Annotated[Session, Depends(startSession)]):
    try:
        pass
    except:
        pass
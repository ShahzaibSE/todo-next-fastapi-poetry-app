from fastapi import APIRouter, Depends
from _database import startSession
from models._user_model import User
from typing import Annotated
from sqlmodel import Session

session = startSession()
signup_route = APIRouter()


@signup_route.post("/signup", response_model=User)
def signup(user: User, session: Annotated[Session, Depends(startSession)]):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
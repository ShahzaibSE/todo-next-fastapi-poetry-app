from fastapi import APIRouter, Depends, Response, HTTPException, status
from api._database import startSession
from api.models._todo_model import ToDoResponse, Todo
from api.utils._todo_service import addToDo
from sqlmodel import select

todo_create_route = APIRouter()

todo_create_route.post("/create",summary="Create a new todo",response_model=ToDoResponse)
async def createToDo(todo:Todo):
    try:
        pass
    except:
        pass
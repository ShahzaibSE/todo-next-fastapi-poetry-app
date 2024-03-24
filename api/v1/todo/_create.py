from fastapi import APIRouter, Depends, Response, HTTPException, status
from api._database import startSession
from api.models._todo_model import ToDoResponse, Todo
from api.utils._todo_service import addToDo
from sqlmodel import select

todo_create_route = APIRouter()

todo_create_route.post("/create",summary="Create a new todo",response_model=ToDoResponse)
async def createToDo(todo:Todo):
    try:
        todo_to_create:ToDoResponse = await addToDo(todo)
        if not todo_to_create:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not create todo"
            )
        else:
            return ToDoResponse(
                status=todo_to_create.status,
                message=todo_to_create.status,
                data=todo_to_create.data
            )
    except:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content="Couldn't create To-do succesfully")
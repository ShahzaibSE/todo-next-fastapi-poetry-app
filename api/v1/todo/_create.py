from fastapi import APIRouter, Response, HTTPException, status
from api.models._todo_model import ToDoResponse, Todo
from api.utils._todo_service import addToDo

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
            return {
                "status":todo_to_create.status,
                "message":todo_to_create.message,
                "data":todo_to_create.data
            }
    except:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            message="Couldn't create To-do succesfully")
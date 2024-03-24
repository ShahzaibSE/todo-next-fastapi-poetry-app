from fastapi import APIRouter, Response, HTTPException, status
from api.models._todo_model import Todo, ToDoResponse
from api.utils._todo_service import deleteToDo

delete_todo_route = APIRouter()

@delete_todo_route.delete("/delete", summary="Delete todo", response_model=ToDoResponse)
async def delete_todo(todo:Todo):
    try:
        todo_to_delete:ToDoResponse = await deleteToDo(todo.id)
        if not todo_to_delete:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Couldn't delete todo successfully"
            )
        elif(todo_to_delete):
            return {
                "status":todo_to_delete.status,
                "message":todo_to_delete.message,
                "data":todo_to_delete.data
            }
        # todo_to_delete = 
    except:
        return Response(status_code=todo_to_delete.status,
                    content=todo_to_delete.message)
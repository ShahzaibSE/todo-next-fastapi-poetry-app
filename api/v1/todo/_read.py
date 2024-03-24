from fastapi import APIRouter, Response, HTTPException, status
from api.models._todo_model import ToDoResponse, Todo
from api.utils._todo_service import getToDos

todo_list_route = APIRouter()

@todo_list_route.get("/list", summary="Get a list of todos",response_model=ToDoResponse)
async def getToDos():
    try:
        todos = await getToDos()
        if not todos:
            raise HTTPException(
                status_code=status.HTTP_204_NO_CONTENT,
                detail="There are no todos in the list"
            )
        else:
            return Response(
                status=status.HTTP_200_OK,
                message="Found todos successfully",
                data=todos
            )
    except:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    content="Couldn't retrieve todo list") 
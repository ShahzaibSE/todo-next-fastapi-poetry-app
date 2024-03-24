from api._database import startSession
from sqlmodel import Session, select, delete, update
from typing import Annotated
from fastapi import Depends
from api.models._todo_model import Todo
from fastapi import status, HTTPException
from api.models._todo_model import ToDoResponse

def getToDos(session:Annotated[Session,Depends(startSession)]):
    try:
        todos = session.exce(select(Todo))
        return ToDoResponse(
            status=status.HTTP_200_OK,
            message="Todo list fetched successfully",
            data=todos
        )
    except:
        raise ToDoResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Couldn't fetch list of todos"
        )
        
async def addToDo(todo:Todo,session:Annotated[Session,Depends(startSession)])->ToDoResponse:
    try:
        existingTodo = await session.exec(select(Todo).filter(Todo.content==todo.content)).first()
        if not existingTodo:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Todo not found")
        elif existingTodo:
            return ToDoResponse(
                status=status.HTTP_202_ACCEPTED,
                message="Todo already exists",
                data=existingTodo
            )
        else:
            todo.content = str.lower(todo.content)
            session.add(todo)
            session.commit()
            session.refresh()
            return ToDoResponse(
                status=status.HTTP_201_CREATED,
                message="Todo created successfully",
                data=todo
            )
        
    except:
        return ToDoResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Couldn't create a new todo"
        )
        
async def deleteToDo(todo:Todo, session:Annotated[Session,Depends(startSession)])->ToDoResponse:
    try:
        existingTodo = await session.exec(select(Todo).filter(Todo.id == todo.id)).first()
        if not existingTodo:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Todo not found")
        session.exec(delete(existingTodo))
        session.commit()
        session.close()
        return ToDoResponse(
            status=status.HTTP_200_OK,
            message="Todo deleted successfully",
            data=existingTodo
        )
    except:
        return ToDoResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Couldn't delete todo successfully"
        )
    
async def updateToDo(todo:Todo, session:Annotated[Session,Depends(startSession)]):
    try:
        todo_to_update:Todo = await session.exce(select(Todo).filter(Todo.id == todo.id)).first()
        if not todo_to_update:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Todo not found")
        todo_to_update.content = todo.content
        session.commit()
        session.refresh(todo)
        session.close()
        return todo
    except:
        return ToDoResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Couldn't update todo successfully"
        )
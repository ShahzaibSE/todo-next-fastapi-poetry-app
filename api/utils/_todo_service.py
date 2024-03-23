from api._database import startSession
from sqlmodel import Session, select, delete, update
from typing import Annotated
from fastapi import Depends
from api.models._todo_model import Todo
from fastapi import status, HTTPException

def getToDos(session:Annotated[Session,Depends(startSession)]):
    try:
        todos = session.exce(select(Todo))
        return todos
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Couldn't get all todos"
        )
        
async def addToDo(todo:Todo,session:Annotated[Session,Depends(startSession)]):
    try:
        existingTodo = await session.exec(select(Todo).filter(Todo.content==todo.content)).first()
        if not existingTodo:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Todo not found")
        elif existingTodo:
            return existingTodo
        else:
            todo.content = str.lower(todo.content)
            session.add(todo)
            session.commit()
            session.refresh()
            return todo
        
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Couldn't create a new todo"
        )
        
async def deleteToDo(todo:Todo, session:Annotated[Session,Depends(startSession)]):
    try:
        existingTodo = await session.exec(select(Todo).filter(Todo.id == todo.id)).first()
        if not existingTodo:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Todo not found")
        session.exec(delete(existingTodo))
        session.commit()
        session.close()
        return {
            "status":status.HTTP_202_ACCEPTED,
            "message":"Todo deleted successfully"
        }
    except:
        pass
    
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
        pass
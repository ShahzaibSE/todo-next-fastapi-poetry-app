from sqlmodel import Field, SQLModel,ForeignKey
from typing import Union, Optional, Annotated
from _user_model import User

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    content: str = Field(index=True)
    user_id = Field(foreign_key=User.id, index=True)

class ToDoResponse(SQLModel):
    status:int
    message:str
    todo:Todo
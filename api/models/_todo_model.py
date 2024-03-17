from sqlmodel import Field, SQLModel 
from typing import Union, Optional, Annotated

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    content: str = Field(index=True)

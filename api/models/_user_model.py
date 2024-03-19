from sqlmodel import Field, SQLModel 
from typing import Union, Optional, Annotated


class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    firstname:str
    lastname:Optional[str] = None
    email:str
    password:str
    
class Token(SQLModel):
    access_token: str
    token_type: str
    # expires_in: int
    refresh_token: str
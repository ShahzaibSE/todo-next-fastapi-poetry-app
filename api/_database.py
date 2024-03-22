import api._settings
from sqlmodel import Field, Session, SQLModel, create_engine, select
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api._settings import DATABASE_URL

connection_string = str(DATABASE_URL).replace("postgresql", "postgresql+psycopg")

# print("Creating connection string using DATABASE URL")
# print(connection_string)

db_engine = create_engine(
    connection_string, connect_args={
        "sslmode":"require"
    },
    pool_recycle=300
)

# print("DB Engine")
# print(db_engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(db_engine)
    

def startSession():
    with Session(db_engine) as session:
        yield session
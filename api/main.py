from fastapi import FastAPI
from contextlib import asynccontextmanager
from api._database import create_db_and_tables
from api.v1.user._user import userRouter

# The first part of the function, before the yield, will
# be executed before the application starts.
# https://fastapi.tiangolo.com/advanced/events/#lifespan-function
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield

app: FastAPI = FastAPI(
    lifespan=lifespan,
    title="Todo fastAPI", 
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.1:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
    ])

#Adding routes.
app.include_router(userRouter, prefix="/user/v1", tags=["users"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
from fastapi import APIRouter
# Routes
from api.v1.user._read import userReadRoute
from api.v1.user._create import signup_route
from api.v1.user._login import login_route

userRouter = APIRouter()

userRouter.include_router(userReadRoute, prefix="", tags=["user"])
userRouter.include_router(signup_route, prefix="", tags=["signup"])
userRouter.include_router(login_route, prefix="", tags=["login"])
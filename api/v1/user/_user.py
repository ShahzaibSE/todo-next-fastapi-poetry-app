from fastapi import APIRouter
# Routes
from v1.user._read import userReadRoute
from v1.user._create import signup_route

userRouter = APIRouter()

userRouter.include_router(userReadRoute, prefix="", tags=["user"])
userRouter.include_router(signup_route, prefix="", tags=["signup"])
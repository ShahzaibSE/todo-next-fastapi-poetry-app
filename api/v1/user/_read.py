from fastapi import APIRouter

userReadRoute = APIRouter()

@userReadRoute.get("/test")
def user_test():
    return {
        "message":"Welcome user!"
    }
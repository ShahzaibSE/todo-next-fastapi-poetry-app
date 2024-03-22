from fastapi import APIRouter

userReadRoute = APIRouter()

# Route to test code snippets.
@userReadRoute.get("/test")
def user_test():
    return {
        "message":"Welcome user!"
    }
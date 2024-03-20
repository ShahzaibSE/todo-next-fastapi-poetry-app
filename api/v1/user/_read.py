from fastapi import APIRouter
from api.utils._utils import create_access_token_jwt

userReadRoute = APIRouter()

# Route to test code snippets.
@userReadRoute.get("/test")
def user_test():
    create_access_token_jwt("shahzaib","noor")
    return {
        "message":"Welcome user!"
    }
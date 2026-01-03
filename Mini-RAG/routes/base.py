#Instead of writing all code (APIs) in main.py, we create a separate file for base routes
#we can add more route files in the future for better organization and use them in main.py to make the main.py cleaner and more maintainable.

from fastapi import APIRouter
import os

base_router = APIRouter(
    prefix = "/api/v1",
    tags = ["Base"]
)

@base_router.get("/welcome")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("VERSION")
    return {"message": f"Welcome to {app_name} v{app_version}"}
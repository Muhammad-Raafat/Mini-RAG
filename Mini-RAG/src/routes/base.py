#Instead of writing all code (APIs) in main.py, we create a separate file for base routes
#we can add more route files in the future for better organization and use them in main.py to make the main.py cleaner and more maintainable.

from fastapi import APIRouter, Depends
from helpers.config import get_settings, Settings
# import os

base_router = APIRouter(
    prefix = "/api/v1",
    tags = ["Base"]
)

@base_router.get("/welcome")
#app_setting 
async def welcome(app_settings: Settings = Depends(get_settings)):
    # app_name = os.getenv("APP_NAME")
    # app_version = os.getenv("VERSION")
    app_name = app_settings().APP_NAME
    app_version = app_settings().VERSION

    return {"message": f"Welcome to {app_name} v{app_version}"}
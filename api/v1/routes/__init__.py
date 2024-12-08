from api.v1.routes import file
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(file.router, prefix="/file", tags=["file"])

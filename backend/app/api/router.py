from fastapi import APIRouter
from app.api.endpoints.v1 import database
from app.api.endpoints.v1 import health
from app.api.endpoints.v1 import auth

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health.router)
api_router.include_router(auth.router)

api_router.include_router(
    database.router,
    tags=["Database"],
)
from fastapi import APIRouter
from app.api.endpoints.v1 import database
from app.api.endpoints.v1 import health
from app.api.endpoints.v1 import auth
from app.api.endpoints.v1 import known_faces
from app.api.endpoints.v1 import recognition

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health.router)
api_router.include_router(auth.router)

api_router.include_router(
    database.router,
    tags=["Database"],
)

api_router.include_router(
    known_faces.router,
    prefix="/known-faces",
    tags=["Known Faces"],
)

api_router.include_router(
    recognition.router,
    prefix="/recognition",
    tags=["Recognition"],
)
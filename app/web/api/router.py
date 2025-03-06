from fastapi.routing import APIRouter

from app.web.api import healthcheck, users

api_router = APIRouter()
api_router.include_router(healthcheck.router)
api_router.include_router(users.router)

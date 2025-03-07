from fastapi.routing import APIRouter

from app.web.api import healthcheck, users, blogs

api_router = APIRouter()
api_router.include_router(healthcheck.router)
api_router.include_router(users.router)
api_router.include_router(blogs.router, tags=["blog"])

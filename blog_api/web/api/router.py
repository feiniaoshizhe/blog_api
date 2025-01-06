from fastapi.routing import APIRouter
from blog_api.web.api import users
from blog_api.db.models.users import api_users
from blog_api.web.api import echo
from blog_api.web.api import redis
from blog_api.web.api import docs
from blog_api.web.api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(users.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(redis.router, prefix="/redis", tags=["redis"])

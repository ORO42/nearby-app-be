from fastapi import Depends, FastAPI
from app.core.auth import verify_token
from app.core.config import settings
from app.db.database import engine
from app.models.base import Base
from app.api.endpoints import user

app = FastAPI(title=settings.APP_NAME)

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/users", tags=["users"])

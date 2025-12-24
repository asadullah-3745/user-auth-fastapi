import utils.transport
import utils.session
from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI OAuth2 Authentication")

app.include_router(auth_router)
app.include_router(user_router)

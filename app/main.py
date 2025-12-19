from fastapi import FastAPI
from app.api.v1.routers import health
from app.api.v1.routers import auth

app = FastAPI(title="User & Auth API", version="1.0.0")

app.include_router(health.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
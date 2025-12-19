from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService
from app.core.database import AsyncSessionLocal

router = APIRouter(prefix="/auth", tags=["Auth"])
service = AuthService()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/register")
async def register(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await service.repo.get_by_email(db, payload.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    await service.register(db, payload.email, payload.password)
    return { "message": "Resregister success"}

@router.post("/login")
async def login(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    token = await service.login(db, payload.email, payload.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return token
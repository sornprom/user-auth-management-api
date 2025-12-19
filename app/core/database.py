from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import configs

engine = create_async_engine(
    configs.DATABASE_URL,
    echo=True,
)

class Base(DeclarativeBase):
    pass

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
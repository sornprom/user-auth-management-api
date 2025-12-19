from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")

def hash_password(password: str) -> str:
    password = password[:72]
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    password = password[:72]
    return pwd_context.verify(password, hashed)

def create_access_token(subject: str) -> str:
    payload = {
        "sub": subject,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=15),
    }
    return jwt.encode(payload, settings.JWT_SECRET, settings.JWT_ALGORITHM)
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import configs

pwd_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")
token_expired = int(configs.JWT_EXPIRE_TOKEN)
def hash_password(password: str) -> str:
    password = password[:72]
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    password = password[:72]
    return pwd_context.verify(password, hashed)

def create_access_token(subject: str) -> str:
    payload = {
        "sub": subject,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=token_expired),
    }
    return jwt.encode(payload, configs.JWT_SECRET, configs.JWT_ALGORITHM)
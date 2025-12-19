from app.repositories.user_repo import UserRepository
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User

class AuthService:

    def __init__(self):
        self.repo = UserRepository()

    async def register(self, db, email: str, password: str):
        user = User(
            email=email,
            hashed_password=hash_password(password),
        )
        return await self.repo.create(db, user)
    
    async def login(self, db, email: str, password: str):
        user = await self.repo.get_by_email(db, email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return create_access_token(str(user.id))
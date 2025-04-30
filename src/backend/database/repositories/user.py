from uuid import UUID
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..models.user import User
from .base import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, User)
    
    async def get_by_username(self, username: str) -> Optional[User]:
        """Get a user by username"""
        try:
            stmt = select(User).where(User.username == username)
            result = await self.session.execute(stmt)
            return result.scalars().first()
        except Exception as e:
            print(f"Error retrieving user by username: {e}")
            return None
    
    async def get_by_email(self, email: str) -> Optional[User]:
        """Get a user by email"""
        try:
            stmt = select(User).where(User.email == email)
            result = await self.session.execute(stmt)
            return result.scalars().first()
        except Exception as e:
            print(f"Error retrieving user by email: {e}")
            return None

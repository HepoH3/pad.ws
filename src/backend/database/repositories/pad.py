from uuid import UUID
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..models.pad import Pad
from .base import BaseRepository

class PadRepository(BaseRepository[Pad]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Pad)
    
    async def get_by_user_id(self, user_id: UUID) -> List[Pad]:
        """Get all pads for a user"""
        try:
            stmt = select(Pad).where(Pad.user_id == user_id)
            result = await self.session.execute(stmt)
            return list(result.scalars().all())
        except Exception as e:
            print(f"Error retrieving pads by user_id: {e}")
            return []

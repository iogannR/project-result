import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.user import UserEntity
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.database.models.user import User


class UserSQLAlchemyRepostory(UserRepository):
    """User repository SQLAlchemy implementation"""
    
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        
    async def create(self, entity: UserEntity) -> None:
        user = User(**entity.model_dump())
        self._session.add(user)
        await self._session.commit()
        await self._session.refresh(user)
        
    async def get_all(self) -> list[UserEntity]:
        result: Result = await self._session.execute(select(User))
        users: Sequence[User] = result.scalars().all()
        return [user.to_entity() for user in users]
        
    async def get_by_id(self, id_: uuid.UUID) -> UserEntity | None:
        user: User | None = await self._session.get(User, id_)
        return user.to_entity() if user else None
    
    async def get_by_email(self, email: str) -> UserEntity | None:
        stmt = select(User).where(User.email == email)
        result: Result = await self._session.execute(stmt)
        user: User | None = result.scalar_one_or_none()
        return user.to_entity() if user else None
    
    async def delete_by_id(self, id_: uuid.UUID) -> None:
        user: User | None = await self._session.get(User, id_)
        await self._session.delete(user)
        await self._session.commit()
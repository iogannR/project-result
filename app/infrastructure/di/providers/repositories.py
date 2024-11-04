from sqlalchemy.ext.asyncio import AsyncSession
from dishka import Provider, provide, Scope

from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.repositories.user_repository_impl import UserSQLAlchemyRepostory


class UserRepositoryProvider(Provider):
    
    @provide(scope=Scope.REQUEST)
    async def provide_user_repository(
        self,
        session: AsyncSession,
    ) -> UserRepository:
        return UserSQLAlchemyRepostory(session=session)
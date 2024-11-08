from typing import AsyncIterable

from sqlalchemy.ext.asyncio import (
    create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession,
)
from dishka import Provider, Scope, provide

from app.infrastructure.config import settings


class SQLAlchemyProvider(Provider):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url
    
    @provide(scope=Scope.APP)
    def provide_egnine(self) -> AsyncEngine: 
        engine: AsyncEngine = create_async_engine(
            url=self.url,
            echo=settings.db.ECHO,
            pool_size=settings.db.POOL_SIZE,
            max_overflow=settings.db.MAX_OVERFLOW,
        )
        return engine

    @provide(scope=Scope.APP)
    def provide_session_factory(
        self,
        engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=engine,
            autoflush=False,
            expire_on_commit=False,
            future=True,
        )
        return session_factory
    
    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(
        self,
        session_factory: async_sessionmaker[AsyncSession],
    ) -> AsyncIterable[AsyncSession]:
        async with session_factory() as session:
            yield session
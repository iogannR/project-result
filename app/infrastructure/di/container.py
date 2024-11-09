from dishka import AsyncContainer, make_async_container

from app.infrastructure.di.providers.adapters import AdaptersProvider
from app.infrastructure.di.providers.database import SQLAlchemyProvider
from app.infrastructure.di.providers.repositories import UserRepositoryProvider
from app.infrastructure.di.providers.use_cases.auth import UserAuthUseCaseProvider
from app.infrastructure.di.providers.use_cases.user import UserUseCaseProvider


def create_container(db_url: str) -> AsyncContainer:
    return make_async_container(
        SQLAlchemyProvider(db_url),
        UserRepositoryProvider(),
        UserUseCaseProvider(),
        UserAuthUseCaseProvider(),
        AdaptersProvider(),
    )
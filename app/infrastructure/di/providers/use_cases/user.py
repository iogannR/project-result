from dishka import Provider, Scope, provide

from app.application.use_cases.user_use_cases import (
    CreateUserUseCase,
    DeleteUserByIdUseCase, 
    GetAllUsersUseCase,
    GetUserByEmailUseCase, 
    GetUserByIdUseCase,
)
from app.domain.repositories.user_repository import UserRepository


class UserUseCaseProvider(Provider):
    
    @provide(scope=Scope.REQUEST)
    async def provide_create(
        self,
        user_repository: UserRepository,
    ) -> CreateUserUseCase:
        return CreateUserUseCase(user_repository)
    
    @provide(scope=Scope.REQUEST)
    async def provide_get_all(
        self,
        user_repository: UserRepository,
    ) -> GetAllUsersUseCase:
        return GetAllUsersUseCase(user_repository)
    
    @provide(scope=Scope.REQUEST)
    async def provide_get_by_id(
        self,
        user_repository: UserRepository,
    ) -> GetUserByIdUseCase:
        return GetUserByIdUseCase(user_repository)
    
    @provide(scope=Scope.REQUEST)
    async def provide_get_by_email(
        self,
        user_repository: UserRepository,
    ) -> GetUserByEmailUseCase:
        return GetUserByEmailUseCase(user_repository)
    
    @provide(scope=Scope.REQUEST)
    async def provide_delete_by_id(
        self,
        user_repository: UserRepository,
    ) -> DeleteUserByIdUseCase:
        return DeleteUserByIdUseCase(user_repository)
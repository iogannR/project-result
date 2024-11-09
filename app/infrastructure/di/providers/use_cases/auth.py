from dishka import Provider, Scope, provide

from app.application.use_cases.auth_use_cases import LoginUserUseCase
from app.domain.adapters.jwt_token_adapter import BaseJWTTokenAdapter
from app.domain.adapters.password_hash_adapter import BasePasswordHashAdapter
from app.domain.repositories.user_repository import UserRepository


class UserAuthUseCaseProvider(Provider):
    
    @provide(scope=Scope.REQUEST)
    async def proide_user_login(
        self,
        user_repository: UserRepository,
        password_hash_adapter: BasePasswordHashAdapter,
        jwt_token_adapter: BaseJWTTokenAdapter,
    ) -> LoginUserUseCase:
        return LoginUserUseCase(
            user_repository=user_repository,
            password_hash_adapter=password_hash_adapter,
            jwt_token_adapter=jwt_token_adapter,
        )
        
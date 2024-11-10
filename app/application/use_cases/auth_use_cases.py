import uuid

from fastapi import HTTPException, status

from app.application.dto.user_dto import LoginUserRequest, UserResponse
from app.application.use_cases.interactor import Interactor
from app.domain.adapters.jwt_token_adapter import BaseJWTTokenAdapter
from app.domain.adapters.password_hash_adapter import BasePasswordHashAdapter
from app.domain.repositories.user_repository import UserRepository


# literals
SUB: str = "sub"

class LoginUserUseCase(Interactor[LoginUserRequest, UserResponse]):
    def __init__(
        self, 
        user_repository: UserRepository,
        password_hash_adapter: BasePasswordHashAdapter,
        jwt_token_adapter: BaseJWTTokenAdapter,
    ) -> None:
        self._user_repository = user_repository
        self._password_hash_adapter = password_hash_adapter
        self._jwt_token_adapter = jwt_token_adapter
        
    async def __call__(self, request: LoginUserRequest) -> UserResponse:
        user = await self._user_repository.get_by_email(request.email)
        if not user or not self._password_hash_adapter.verify_password(
            request.password,
            user.password,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Ошибка авторизации: неверный логин или пароль!")
        return user
    

class CreateAccessTokenUseCase(Interactor[uuid.UUID, str]):
    def __init__(
        self,
        jwt_token_adapter: BaseJWTTokenAdapter,
    ) -> None:
        self._jwt_token_adapter = jwt_token_adapter
        
    async def __call__(self, request: uuid.UUID) -> str:
        access_token = self._jwt_token_adapter.encode_access_token(
            payload={SUB: str(request)},
        )
        return access_token
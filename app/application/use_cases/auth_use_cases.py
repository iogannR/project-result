from fastapi import HTTPException, status

from app.application.dto.user_dto import LoginUserRequest, UserResponse
from app.application.use_cases.interactor import Interactor
from app.domain.adapters.password_hash_adapter import BasePasswordHashAdapter
from app.domain.repositories.user_repository import UserRepository


class LoginUserUseCase(Interactor[LoginUserRequest, UserResponse]):
    def __init__(
        self, 
        user_repository: UserRepository,
        hash_password_adapter: BasePasswordHashAdapter,
    ) -> None:
        self._user_repository = user_repository
        self._hash_password_adapter = hash_password_adapter
        
    async def __call__(self, request: LoginUserRequest) -> UserResponse:
        user = await self._user_repository.get_by_email(request.email)
        if user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Ошибка авторизации",
            )
        check_password = self._hash_password_adapter.verify_password(
            request.password, user.password,
        )
        if not check_password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Ошибка авторизации",
            )
        return user
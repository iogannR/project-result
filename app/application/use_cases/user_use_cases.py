import uuid

from fastapi import HTTPException, status

from app.domain.adapters.password_hash_adapter import BasePasswordHashAdapter
from app.domain.entities.user import UserEntity
from app.domain.repositories.user_repository import UserRepository
from app.application.use_cases.interactor import Interactor
from app.application.dto.user_dto import CreateUserRequest, UserResponse


class CreateUserUseCase(Interactor[CreateUserRequest, UserResponse]):
    def __init__(
        self,
        user_repository: UserRepository, 
        password_hash_adapter: BasePasswordHashAdapter,
    ) -> None:
        self._user_repository = user_repository
        self._password_hash_adapter = password_hash_adapter
        
    async def __call__(self, request: CreateUserRequest) -> UserResponse:
        existing: UserEntity | None = await self._user_repository.get_by_email(request.email)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Пользователь с таким email уже существует!",
            )
        request.password = self._password_hash_adapter.hash_password(request.password)
        user_entity = UserEntity(**request.model_dump())
        await self._user_repository.create(user_entity)
        return UserResponse.from_entity(user_entity)
    

class GetAllUsersUseCase(Interactor[None, list[UserResponse]]):
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
        
    async def __call__(self, request: None = None) -> list[UserResponse]:
        user_entities: list[UserEntity] = await self._user_repository.get_all()
        return [
            UserResponse.from_entity(user_entity) 
            for user_entity in user_entities
        ] 
    

class GetUserByIdUseCase(Interactor[uuid.UUID, UserResponse]):
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
        
    async def __call__(self, request: uuid.UUID) -> UserResponse:
        user_entity: UserEntity | None = await self._user_repository.get_by_id(request)
        if user_entity is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Пользователь с таким id не найден!",
            )
        return UserResponse.from_entity(user_entity)
    

class GetUserByEmailUseCase(Interactor[str, UserResponse]):
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
        
    async def __call__(self, request: str) -> UserResponse:
        user_entity: UserEntity | None = await self._user_repository.get_by_email(request)
        if user_entity is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Пользователь с таким email не найден!",
            )
        return UserResponse.from_entity(user_entity)


class DeleteUserByIdUseCase(Interactor[uuid.UUID, None]):
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
        
    async def __call__(self, request: uuid.UUID) -> None:
        return await self._user_repository.delete_by_id(request)
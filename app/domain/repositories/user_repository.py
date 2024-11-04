import uuid
from abc import ABC, abstractmethod

from app.domain.entities.user import UserEntity


class UserRepository(ABC):
    """Base user repository from which the implementation should be inherited"""
    
    @abstractmethod
    async def create(self, entity: UserEntity) -> None:
        ...
        
    
    @abstractmethod
    async def get_all(self) -> list[UserEntity]:
        ...
    
    @abstractmethod
    async def get_by_id(self, id_: uuid.UUID) -> UserEntity | None:
        ...
        
    @abstractmethod
    async def get_by_email(self, email: str) -> UserEntity | None:
        ...
        
    @abstractmethod
    async def delete_by_id(self, id_: uuid.UUID) -> None:
        ...
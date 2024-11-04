from __future__ import annotations

import uuid
from pydantic import BaseModel, EmailStr, ConfigDict

from app.domain.entities.user import UserEntity


class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr
    password: str
    
    model_config = ConfigDict(
        from_attributes=True,
    )
    
    @classmethod
    def from_entity(cls, entity: UserEntity) -> UserResponse:
        return cls(
            id=entity.id,
            username=entity.username,
            email=entity.email,
            password=entity.password,
        )
        
        
class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
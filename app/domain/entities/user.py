from pydantic import EmailStr

from app.domain.entities.base import BaseEntity


class UserEntity(BaseEntity):
    """Entity that represents users model"""
    
    username: str
    email: EmailStr
    password: str
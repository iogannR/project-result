from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.entities.user import UserEntity
from app.infrastructure.database.models.base import Base


class User(Base):
    username: Mapped[str] = mapped_column(String(65), nullable=False)
    email: Mapped[str] = mapped_column(String(160), nullable=False, unique=True)
    password: Mapped[str]
    
    def to_entity(self) -> UserEntity:
        return UserEntity(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
        )
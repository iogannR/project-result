import uuid

from pydantic import BaseModel, Field


class BaseEntity(BaseModel):
    """Base entity from which other entities should be inherited"""
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
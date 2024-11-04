from typing import Any
from abc import ABC, abstractmethod


class BaseJWTTokenAdapter(ABC):
    
    @abstractmethod
    def encode_jwt(self, payload: dict[str, Any]) -> str:
        ...
        
    @abstractmethod
    def decode_jwt(self, token: str) -> dict[str, Any]:
        ...
from typing import Any
from abc import ABC, abstractmethod


class BaseJWTTokenAdapter(ABC):
    
    @abstractmethod
    def encode_access_token(self, payload: dict[str, Any]) -> str:
        ...
        
    @abstractmethod
    def decode_access_token(self, token: str) -> dict[str, Any]:
        ...
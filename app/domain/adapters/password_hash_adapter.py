from abc import ABC, abstractmethod


class BasePasswordHashAdapter(ABC):
    
    @abstractmethod
    def hash_password(self, password: str) -> str:
        ...
        
    @abstractmethod
    def verify_password(
        self, 
        plain_password: str, 
        hashed_password: str,
    ) -> bool:
        ...
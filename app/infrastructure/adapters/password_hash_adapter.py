from passlib.context import CryptContext

from app.domain.adapters.password_hash_adapter import BasePasswordHashAdapter


class PasswordHashAdapter(BasePasswordHashAdapter):
    def __init__(
        self, 
        pwd_context: CryptContext = CryptContext(
            schemes=["bcrypt"], deprecated="auto",
        ),
    ) -> None:
        self.pwd_context = pwd_context
        
    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)
    
    def verify_password(
        self, 
        plain_password: str, 
        hashed_password: str,
    ) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
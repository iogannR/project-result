import uuid
from datetime import UTC, datetime, timedelta
from typing import Any

from jose import jwt, JWTError

from app.domain.adapters.jwt_token_adapter import BaseJWTTokenAdapter
from app.infrastructure.config import settings


# code literals
EXP: str = "exp"
IAT: str = "iat"
JTI: str = "jti"

class JoseJWTTokenAdapter(BaseJWTTokenAdapter):
    """Adapter for working with JWT-tokens"""
        
    def encode_access_token(self, payload: dict[str, Any]) -> str:
        data = payload.copy()
        now = datetime.now(UTC)
        expire = now + timedelta(
            minutes=settings.jwt_auth.ACCESS_TOKEN_EXPIRE_MINUTES,
        )
        data.update({EXP: expire, IAT: now, JTI: str(uuid.uuid4())})
        access_token = jwt.encode(
            data, settings.jwt_auth.PRIVATE_KEY, algorithm=settings.jwt_auth.ALGORITHM,
        )
        return access_token
    
    def decode_access_token(self, token: str) -> dict[str, Any]:
        try: 
            decoded = jwt.decode(
                token, 
                settings.jwt_auth.PUBLIC_KEY, 
                algorithms=[settings.jwt_auth.ALGORITHM],
            )
        except JWTError as exception:
            raise ValueError("Невалидный токен!") from exception
        return decoded
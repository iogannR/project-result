import uuid
from datetime import UTC, datetime, timedelta
from typing import Any

from jose import jwt, JWTError

from app.domain.adapters.jwt_token_adapter import BaseJWTTokenAdapter
from app.infrastructure.config import settings


class JoseJWTTokenAdapter(BaseJWTTokenAdapter):
    def __init__(
        self,
        private_key: str = settings.jwt_auth.private_key_path.read_text(),
        public_key: str = settings.jwt_auth.public_key_path.read_text(),
        algorithm: str = settings.jwt_auth.algorithm,
        access_token_expire_minutes: int = settings.jwt_auth.access_token_expire_minutes,
        expire_timedelta: timedelta | None = None,
    ) -> None:
        self.private_key = private_key
        self.public_key = public_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes
        self.expire_timedelta = expire_timedelta
        
    def encode_jwt(self, payload: dict[str, Any]) -> str:
        data = payload.copy()
        now = datetime.now(UTC)
        if self.expire_timedelta:
            expire = now + self.expire_timedelta
        else:
            expire = now + timedelta(minutes=self.access_token_expire_minutes)
        data.update(
            {
                "exp": expire,
                "iat": now,
                "jti": str(uuid.uuid4()),
            }
        )
        access_token = jwt.encode(
            data, self.private_key, algorithm=self.algorithm,
            )
        return access_token
    
    def decode_jwt(self, token: str) -> dict[str, Any]:
        try: 
            decoded = jwt.decode(
                token, self.public_key, algorithms=[self.algorithm],
            )
        except JWTError as exception:
            raise ValueError("Невалидный токен!") from exception
        return decoded
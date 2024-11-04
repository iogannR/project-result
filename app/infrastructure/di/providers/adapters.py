from dishka import Provider, Scope, provide

from app.domain.adapters.jwt_token_adapter import BaseJWTTokenAdapter
from app.domain.adapters.password_hash_adapter import BasePasswordHashAdapter
from app.infrastructure.adapters.jwt_token_adapter import JoseJWTTokenAdapter
from app.infrastructure.adapters.password_hash_adapter import PasswordHashAdapter


class AdaptersProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_password_hash_adapter(
        self,
    ) -> BasePasswordHashAdapter:
        return PasswordHashAdapter()
    
    @provide(scope=Scope.APP)
    def provide_jwt_token_adapter(
        self,
    ) -> BaseJWTTokenAdapter:
        return JoseJWTTokenAdapter()
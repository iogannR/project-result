from datetime import timedelta

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
    def provide_timedelta(
        self,
    ) -> timedelta | None:
        return timedelta
    
    @provide(scope=Scope.REQUEST)
    def provide_jwt_token_adapter(
        self,
        timedelta: timedelta | None,
    ) -> BaseJWTTokenAdapter:
        return JoseJWTTokenAdapter(timedelta)
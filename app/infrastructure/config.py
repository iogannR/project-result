from pathlib import Path
from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent


class RunConfig(BaseModel):
    HOST: str = "localhost"
    PORT: int = 8000


class JWTAuthConfig(BaseModel):
    private_key_path: Path = BASE_DIR / "infrastructure" / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "infrastructure" / "certs" / "jwt-public.pem"
    ALGORITHM: str = "RS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 3

    @property
    def PRIVATE_KEY(self) -> str:
        return self.private_key_path.read_text()
    
    @property
    def PUBLIC_KEY(self) -> str:
        return self.public_key_path.read_text()
    

class DatabaseConfig(BaseModel):
    URL: PostgresDsn
    ECHO: bool
    POOL_SIZE: int
    MAX_OVERFLOW: int
    
    NAMING_CONVENTION: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
    

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    jwt_auth: JWTAuthConfig = JWTAuthConfig()
    db: DatabaseConfig
    
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        env_nested_delimiter="__",
        env_prefix="MAIN__",
        extra="allow",
    )
    

settings = Settings()
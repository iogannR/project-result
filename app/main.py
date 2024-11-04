import uvicorn
from fastapi import FastAPI
from dishka.integrations.fastapi import setup_dishka

from app.infrastructure.config import settings
from app.infrastructure.di.container import create_container
from app.api import router as api_router


def create_app() -> FastAPI:
    app = FastAPI(title="Образовательная платформа")
    container = create_container(db_url=str(settings.db.url))
    setup_dishka(container, app)
    app.include_router(api_router, prefix="/api")
    
    return app


if __name__ == "__main__":
    uvicorn.run(
        "app.main:create_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True, 
        factory=True,
    )
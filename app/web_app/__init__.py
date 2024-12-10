from fastapi import FastAPI

from .routes import mutant_router, statistics_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(mutant_router)
    app.include_router(statistics_router)

    return app

from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config import get_settings
from src.db.factory import make_database
from src.routers import ping


@asynccontextmanager
async def lifespan(app: FastAPI):

    settings = get_settings()
    app.state.settings = settings

    database = make_database()
    app.state.database = database

    yield

    database.teardown()

app = FastAPI(
        title="arXiv RAG Assistant API",
        description="Personal arXiv RAG Assistant",
        version="0.1.0",
        lifespan=lifespan
    )

app.include_router(ping.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000, host="0.0.0.0")
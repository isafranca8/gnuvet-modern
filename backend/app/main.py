from fastapi import FastAPI
from app.routes import client_routes
from app.database.session import engine, Base
from app.core.config import settings

import app.models.client

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

Base.metadata.create_all(bind=engine)

app.include_router(client_routes.router)


@app.get("/")
def health():
    return {"status": "ok"}
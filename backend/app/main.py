from fastapi import FastAPI

from app.database.session import engine, Base
from app.routes import client_routes
from app.core.config import settings
from app.core.exceptions import NotFoundException, not_found_exception_handler

import app.models.client
import app.models.pet
import app.models.appointment


app = FastAPI(
    title=settings.app_name,
    description="Veterinary management system",
    version=settings.app_version
)

Base.metadata.create_all(bind=engine)

app.include_router(client_routes.router)

app.add_exception_handler(
    NotFoundException,
    not_found_exception_handler
)


@app.get("/")
def health():
    return {"status": "running"}
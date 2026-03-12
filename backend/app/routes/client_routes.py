"""
Client Routes

Endpoints relacionados a clientes.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.client_schema import ClientCreate
from app.services import client_service

router = APIRouter()


@router.post("/", status_code=201)
def create_client(
    client: ClientCreate,
    db: Session = Depends(get_db)
):
    """
    Endpoint para criar cliente.
    """

    return client_service.create_client(db, client)
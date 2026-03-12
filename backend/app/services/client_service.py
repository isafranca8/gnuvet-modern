"""
Service responsável pelas regras de negócio de clientes
"""

from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client_schema import ClientCreate


def create_client(db: Session, client_data: ClientCreate):

    """
    Cria cliente no banco
    """

    client = Client(**client_data.model_dump())

    db.add(client)

    db.commit()

    db.refresh(client)

    return client
"""
Client Service

Responsável pela lógica de negócio de clientes.
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.client import Client


def create_client(db: Session, client_data):
    """
    Cria um novo cliente.
    """

    existing = db.query(Client).filter(
        Client.email == client_data.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    client = Client(**client_data.model_dump())

    db.add(client)
    db.commit()
    db.refresh(client)

    return client
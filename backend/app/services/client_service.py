from sqlalchemy.orm import Session
from app.repository import client_repository


def create_client(db: Session, client_data):
    return client_repository.create_client(db, client_data)


def list_clients(db: Session):
    return client_repository.get_clients(db)
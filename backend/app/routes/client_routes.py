from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.services import client_service
from app.schemas.client_schema import ClientCreate

router = APIRouter(prefix="/clients", tags=["clients"])


@router.get("/")
def list_clients(db: Session = Depends(get_db)):
    return client_service.list_clients(db)


@router.post("/")
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return client_service.create_client(db, client)
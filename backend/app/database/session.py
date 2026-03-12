"""
Database session configuration.

Responsável por:
- criar engine do SQLAlchemy
- criar sessão de banco
- fornecer dependência get_db para FastAPI
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings


DATABASE_URL = settings.database_url

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    """
    Dependency usada nas rotas FastAPI
    para obter sessão de banco.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
"""
Base mixin utilizado para auditoria
Permite rastrear criação e atualização de registros
"""

from sqlalchemy import Column, DateTime
from datetime import datetime


class TimestampMixin:

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
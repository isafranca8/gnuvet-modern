"""
Schemas relacionados ao cliente (dono do animal)
"""

from pydantic import BaseModel, Field, EmailStr, ConfigDict


class ClientCreate(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=120,
        description="Nome completo do cliente"
    )

    phone: str = Field(
        pattern=r"^\d{10,15}$",
        description="Telefone apenas números"
    )

    email: EmailStr


class ClientUpdate(BaseModel):

    name: str | None = None

    phone: str | None = None

    email: EmailStr | None = None


class ClientResponse(BaseModel):

    id: int

    name: str

    phone: str

    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
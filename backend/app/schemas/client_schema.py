from pydantic import BaseModel, ConfigDict


class ClientResponse(BaseModel):

    id: int
    name: str
    phone: str

    model_config = ConfigDict(
        from_attributes=True
    )
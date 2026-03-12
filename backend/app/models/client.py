from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.session import Base


class Client(Base):

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)

    # relacionamento com pets
    pets = relationship("Pet", back_populates="owner", cascade="all, delete")
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base


class Pet(Base):

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    species = Column(String)

    breed = Column(String)

    age = Column(Integer)

    owner_id = Column(Integer, ForeignKey("clients.id"))

    owner = relationship("Client", back_populates="pets")

    vaccines = relationship("Vaccine")

    medical_records = relationship("MedicalRecord")
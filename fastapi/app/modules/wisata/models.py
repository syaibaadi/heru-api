from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Wisata(Base):
    __tablename__ = "wisata"
    
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(50), index=True)
    destination = Column(String(50), index=True)
    benefit = Column(String, index=True)
    description = Column(String(50), index=True)
    price = Column(String(50))
    image = Column(Text)
    min_person = Column(Integer)
    max_person = Column(Integer)
    

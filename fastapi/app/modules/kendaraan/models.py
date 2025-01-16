from sqlalchemy import Column, Integer, String, Text
from core.database import Base

class Kendaraan(Base):
    __tablename__ = "kendaraan"
    
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(50), index=True)
    type = Column(String(50), index=True)
    capacity = Column(Integer, index=True)
    number = Column(String(50), unique=True, index=True)
    

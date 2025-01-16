from sqlalchemy import Column, Integer, String
from core.database import Base

class User(Base):
    __tablename__ = "pelanggan"
    
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(50), index=True)
    phone = Column(String(50), index=True)
    address = Column(String, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(50))

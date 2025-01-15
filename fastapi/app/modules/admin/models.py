from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Admin(Base):
    __tablename__ = "admin"
    
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(50), index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(50))

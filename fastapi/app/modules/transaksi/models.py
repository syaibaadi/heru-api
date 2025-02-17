import enum
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from core.database import Base

class StatusTransaksiEnum(enum.Enum):
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'
    PENDING = 'PENDING'

class Transaksi(Base):
    __tablename__ = "transaksi"
    
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, nullable=False)
    telfon = Column(String, nullable=False)
    alamat = Column(String, nullable=False)
    book_date = Column(DateTime, nullable=True)
    total_user = Column(Integer, nullable=True)
    description = Column(String, nullable=False)
    status = Column(String, default='PENDING', nullable=True)
    wisata_id = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=True)
    order_id = Column(String)
    
    

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
    customer_id = Column(Integer, nullable=False)
    wisata_id = Column(Integer, nullable=False)
    kendaraan_id = Column(Integer, nullable=False)
    book_date = Column(DateTime, nullable=True)
    pick_loc = Column(Text, nullable=True)
    total_users = Column(Integer, nullable=True)
    total_price = Column(Integer, nullable=True)
    status = Column(Enum(StatusTransaksiEnum), default=StatusTransaksiEnum.PENDING, nullable=True)
    
    

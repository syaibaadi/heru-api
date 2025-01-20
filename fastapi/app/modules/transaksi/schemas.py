from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr

class StatusTransaksiEnum(str, Enum):
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'
    PENDING = 'PENDING'
    
class TransaksiBase(BaseModel):
    # id: int
    nama: str
    telfon: str 
    alamat: str 
    book_date: Optional[datetime] = None
    total_user: Optional[int] = None
    description: str
    status: Optional[StatusTransaksiEnum] = StatusTransaksiEnum.PENDING
    wisata_id: int 
    total_price: int

class TransaksiCreate(TransaksiBase):
    pass

class TransaksiOut(TransaksiBase):
    id: int

    class Config:
        from_attributes = True

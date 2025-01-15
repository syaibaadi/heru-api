from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr

class StatusTransaksiEnum(str, Enum):
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'
    PENDING = 'PENDING'
    
class TransaksiBase(BaseModel):
    customer_id: int
    wisata_id: int
    kendaraan_id: int
    book_date: Optional[datetime] = None
    pick_loc: Optional[str] = None
    total_users: Optional[int] = None
    total_price: Optional[int] = None
    status: Optional[StatusTransaksiEnum] = StatusTransaksiEnum.PENDING
    image: str

class TransaksiCreate(TransaksiBase):
    pass

class TransaksiOut(TransaksiBase):
    id: int

    class Config:
        from_attributes = True

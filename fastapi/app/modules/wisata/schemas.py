# .module/wisata/schemas.py
from pydantic import BaseModel

class WisataBase(BaseModel):
    nama: str
    destination: str
    benefit: str
    description: str
    price: int
    image: str
    min_person: int 
    max_person: int

class WisataCreate(WisataBase):
    pass

class WisataResponse(WisataBase):
    id: int
    nama: str
    destination: str
    benefit: str
    description: str
    price: int
    image: str
    min_person: int 
    max_person: int

    class Config:
        from_attributes = True

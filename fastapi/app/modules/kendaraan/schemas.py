from pydantic import BaseModel, EmailStr

class KendaraanBase(BaseModel):
    nama: str
    type: str
    capacity: int
    number: str

class KendaraanCreate(KendaraanBase):
    pass

class KendaraanResponse(KendaraanBase):
    id: int
    nama: str
    type: str
    capacity: int
    number: str

    class Config:
        from_attributes = True

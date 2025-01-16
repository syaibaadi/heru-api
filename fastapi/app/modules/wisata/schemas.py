from pydantic import BaseModel, EmailStr

class WisataBase(BaseModel):
    nama: str
    destination: str
    benefit: str
    description: str
    price: int
    image: str

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

    class Config:
        from_attributes = True

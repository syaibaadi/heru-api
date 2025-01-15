from pydantic import BaseModel, EmailStr

class AdminBase(BaseModel):
    nama: str
    email: str

class AdminCreate(AdminBase):
    nama: str
    email: str
    password: str

class AdminResponse(AdminBase):
    id: int
    nama: str
    email: str

    class Config:
        from_attributes = True

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    nama: str
    phone: str
    address: str
    email: str
    password: str

class UserCreate(UserBase):
    nama: str
    phone: str
    address: str
    email: str
    password: str

class UserResponse(UserBase):
    id: int
    nama: str 
    phone: str
    address: str
    email: str
    password: str

    class Config:
        from_attributes = True

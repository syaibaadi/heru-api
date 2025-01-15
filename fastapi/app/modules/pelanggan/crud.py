from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate

# get all data
def get_users(db: Session):
    return db.query(User).all()
# post data
def create_user(db: Session, user: UserCreate):
    new_user = User(nama=user.nama, email=user.email, phone=user.phone, address=user.address, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
# get by id
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
# edit data
def update_user(db: Session, user_id: int, nama: str, phone:str, address: str, email: str, password: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.nama = nama
        user.phone = phone
        user.address = address
        user.email = email
        user.password = password
        db.commit()
        db.refresh(user)
    return user
# hapus
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
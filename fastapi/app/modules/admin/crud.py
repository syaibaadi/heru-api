from sqlalchemy.orm import Session
from .models import Admin
from .schemas import AdminBase, AdminCreate

# get all data
def get_users(db: Session):
    # Return all data in admin table record
    return db.query(Admin).all()

# post data
def create_user(db: Session, user: AdminBase):
    new_user = Admin(nama=user.nama, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get by id
def get_user(db: Session, user_id: int):
    return db.query(Admin).filter(Admin.id == user_id).first()
# edit data
def update_user(db: Session, user_id: int, nama: str, phone:str, address: str, email: str, password: str):
    user = db.query(Admin).filter(Admin.id == user_id).first()
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
    user = db.query(Admin).filter(Admin.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
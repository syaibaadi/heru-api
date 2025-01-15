from sqlalchemy.orm import Session
from .models import Kendaraan
from .schemas import KendaraanCreate

# get all data
def get_kendaraans(db: Session):
    return db.query(Kendaraan).all()

# post data
def create_kendaraan(db: Session, kendaraan: KendaraanCreate):
    new_kendaraan = Kendaraan(nama=kendaraan.nama, type=kendaraan.type, capacity=kendaraan.capacity, number=kendaraan.number)
    db.add(new_kendaraan)
    db.commit()
    db.refresh(new_kendaraan)
    return new_kendaraan

# get by id
def get_kendaraan(db: Session, kendaraan_id: int):
    return db.query(Kendaraan).filter(Kendaraan.id == kendaraan_id).first()

# edit data
def update_kendaraan(db: Session, kendaraan_id: int, nama: str, type:str, capacity: int, number: str):
    kendaraan = db.query(Kendaraan).filter(Kendaraan.id == kendaraan_id).first()
    if kendaraan:
        kendaraan.nama = nama
        kendaraan.type = type
        kendaraan.capacity = capacity
        kendaraan.number = number
        db.commit()
        db.refresh(kendaraan)
    return kendaraan

# hapus
def delete_kendaraan(db: Session, kendaraan_id: int):
    kendaraan = db.query(Kendaraan).filter(Kendaraan.id == kendaraan_id).first()
    if kendaraan:
        db.delete(kendaraan)
        db.commit()
    return kendaraan
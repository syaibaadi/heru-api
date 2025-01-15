from sqlalchemy.orm import Session
from .models import Wisata
from .schemas import WisataCreate

# get all data
def get_wisatas(db: Session):
    return db.query(Wisata).all()

# post data
def create_wisata(db: Session, wisata: WisataCreate):
    new_wisata = Wisata(nama=wisata.nama, destinasi=wisata.destinasi, benefit=wisata.benefit, description=wisata.description, price=wisata.price, image=wisata.image)
    db.add(new_wisata)
    db.commit()
    db.refresh(new_wisata)
    return new_wisata

# get by id
def get_wisata(db: Session, wisata_id: int):
    return db.query(Wisata).filter(Wisata.id == wisata_id).first()

# edit data
def update_wisata(db: Session, wisata_id: int, nama: str, destinasi:str, benefit: str, description: str, price: int, image: str):
    wisata = db.query(Wisata).filter(Wisata.id == wisata_id).first()
    if wisata:
        wisata.nama = nama
        wisata.destinasi = destinasi
        wisata.benefit = benefit
        wisata.description = description
        wisata.price = price
        wisata.image = image
        db.commit()
        db.refresh(wisata)
    return wisata

# hapus
def delete_wisata(db: Session, wisata_id: int):
    wisata = db.query(Wisata).filter(Wisata.id == wisata_id).first()
    if wisata:
        db.delete(wisata)
        db.commit()
    return wisata
# .module/wisata/crud.py
from sqlalchemy.orm import Session
from .models import Wisata
from .schemas import WisataCreate

# Get all data
def get_wisatas(db: Session):
    return db.query(Wisata).all()

# Post data
def create_wisata(db: Session, wisata: WisataCreate):
    new_wisata = Wisata(nama=wisata.nama, destination=wisata.destination, benefit=wisata.benefit, description=wisata.description, price=wisata.price, image=wisata.image, min_person = wisata.min_person, max_person = wisata.max_person)
    db.add(new_wisata)
    db.commit()
    db.refresh(new_wisata)
    return new_wisata

# Get by id
def get_wisata(db: Session, wisata_id: int):
    return db.query(Wisata).filter(Wisata.id == wisata_id).first()

# Update data
def update_wisata(db: Session, wisata_id: int, nama: str, destination:str, benefit: str, description: str, price: int, image: str, min_person: int, max_person: int):
    wisata = db.query(Wisata).filter(Wisata.id == wisata_id).first()
    if wisata:
        wisata.nama = nama
        wisata.destination = destination
        wisata.benefit = benefit
        wisata.description = description
        wisata.price = price
        wisata.image = image
        wisata.min_person = min_person
        wisata.max_person = max_person
        db.commit()
        db.refresh(wisata)
    return wisata

# Delete data
def delete_wisata(db: Session, wisata_id: int):
    wisata = db.query(Wisata).filter(Wisata.id == wisata_id).first()
    if wisata:
        db.delete(wisata)
        db.commit()
    return wisata

import datetime
from sqlalchemy.orm import Session
from .models import Transaksi
from .schemas import TransaksiCreate

# get all data
def get_transaksis(db: Session):
    return db.query(Transaksi).all()

# post data
def create_transaksi(db: Session, transaksi: TransaksiCreate):
    new_transaction = Transaksi(customer_id=transaksi.customer_id, wisata_id=transaksi.wisata_id, kendaraan_id=transaksi.kendaraan_id, book_date=transaksi.book_date, pick_loc=transaksi.pick_loc, total_users=transaksi.total_users, total_price=transaksi.total_price, status='PENDING', image=transaksi.image)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

# get by id
def get_transaksi(db: Session, transaksi_id: int):
    return db.query(Transaksi).filter(Transaksi.id == transaksi_id).first()

# edit data
def update_transaksi(db: Session, transaksi_id: int, customer_id: int, wisata_id: int, kendaraan_id: int, book_date: datetime, pic_loc: str, total_users: int, total_price: int, image: str):
    transaksi = db.query(Transaksi).filter(Transaksi.id == transaksi_id).first()
    if transaksi:
        transaksi.customer_id = customer_id
        transaksi.wisata_id = wisata_id
        transaksi.kendaraan_id = kendaraan_id
        transaksi.book_date = book_date
        transaksi.pic_loc = pic_loc
        transaksi.total_users = total_users
        transaksi.total_price = total_price
        transaksi.image = image
        db.commit()
        db.refresh(transaksi)
    return transaksi

# hapus
def delete_transaksi(db: Session, transaksi_id: int):
    transaksi = db.query(Transaksi).filter(Transaksi.id == transaksi_id).first()
    if transaksi:
        db.delete(transaksi)
        db.commit()
    return transaksi
import datetime
import uuid
from sqlalchemy.orm import Session
from .models import Transaksi
from .schemas import TransaksiCreate, TransaksiOut

# get all data
def get_transaksis(db: Session):
    return db.query(Transaksi).all()

# post data
def create_transaksi(db: Session, transaksi: TransaksiCreate) -> TransaksiOut:
    # Generate UUID untuk order_id
    generated_order_id = str(uuid.uuid4())
    
    # Membuat transaksi baru dengan generated order_id
    new_transaction = Transaksi(
        nama=transaksi.nama,
        telfon=transaksi.telfon,
        alamat=transaksi.alamat,
        book_date=transaksi.book_date,
        total_user=transaksi.total_user,
        description=transaksi.description,
        status='PENDING',
        wisata_id=transaksi.wisata_id,
        total_price=transaksi.total_price,
        order_id=generated_order_id  # Set UUID yang baru dihasilkan
    )
    
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    
    # Kembalikan response menggunakan TransaksiOut yang mencakup order_id
    return TransaksiOut(
        id=new_transaction.id,
        nama=new_transaction.nama,
        telfon=new_transaction.telfon,
        alamat=new_transaction.alamat,
        book_date=new_transaction.book_date,
        total_user=new_transaction.total_user,
        description=new_transaction.description,
        status=new_transaction.status,
        wisata_id=new_transaction.wisata_id,
        total_price=new_transaction.total_price,
        order_id=new_transaction.order_id  # Include order_id in the response
    )

# get by id
def get_transaksi(db: Session, transaksi_id: int):
    return db.query(Transaksi).filter(Transaksi.id == transaksi_id).first()

# edit data
def update_transaksi(db: Session, transaksi_id: int, nama: str, telfon: str, alamat: str, book_date: datetime, total_user: int, description: str, status: str, wisata_id : int, total_price: int):
    transaksi = db.query(Transaksi).filter(Transaksi.id == transaksi_id).first()
    if transaksi:
        transaksi.nama = nama
        transaksi.telfon = telfon
        transaksi.alamat = alamat
        transaksi.book_date = book_date
        transaksi.total_user = total_user
        transaksi.description = description
        transaksi.status = status
        transaksi.wisata_id = wisata_id
        transaksi.total_price = total_price
        
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
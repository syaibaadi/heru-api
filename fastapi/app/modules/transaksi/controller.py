from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from . import crud, schemas
from typing import List
from .models import Transaksi

router = APIRouter()

@router.get("", response_model=List[schemas.TransaksiOut])
async def read_transaksis(db: Session = Depends(get_db)):
    return crud.get_transaksis(db)

@router.post("", response_model=schemas.TransaksiOut)  # Ganti response_model menjadi TransaksiOut
async def create_new_transaksi(transaksi: schemas.TransaksiCreate, db: Session = Depends(get_db)):
    return crud.create_transaksi(db, transaksi)

@router.get("/{transaksi_id}", response_model=schemas.TransaksiOut)
async def read_transaksi(transaksi_id: int, db: Session = Depends(get_db)):
    db_transaksi = crud.get_transaksi(db, transaksi_id)

    if db_transaksi is None:
        raise HTTPException(status_code = 404, detail="Transaksi Not Found")
    
    return db_transaksi

@router.post("/webhook")
async def handle_webhook(payload: dict, db: Session = Depends(get_db)):
    # Ambil order_id dari payload
    order_id = payload.get('order_id')
    status_payment = payload.get('status')  # Misalnya status pembayaran ada di payload
    
    # Periksa jika status adalah "PAID"
    if status_payment == "PAID":
        # Cari transaksi berdasarkan order_id
        transaksi = db.query(Transaksi).filter(Transaksi.order_id == order_id).first()

        if transaksi:
            # Jika transaksi ditemukan, ubah status menjadi PAID
            transaksi.status = "PAID"
            db.commit()  # Simpan perubahan ke database
            return {"message": "Status pembayaran berhasil diperbarui", "order_id": order_id}
        else:
            return {"error": "Transaksi tidak ditemukan", "order_id": order_id}
    
    return {"error": "Status pembayaran tidak valid", "status": status_payment}

# @router.put("/{transaksi_id}", response_model=schemas.TransaksiOut)
# def update_wisata(transaksi_id: int, wisata: schemas.TransaksiCreate, db: Session = Depends(get_db)):
#     db_wisata = crud.update_wisata(db, transaksi_id, wisata.nama)
#     if db_wisata is None:
#         raise HTTPException(status_code=404, detail="Wisata not found")
#     return db_wisata

# @router.delete("/{wisata_id}", response_model=schemas.WisataResponse)
# def delete_wisata(wisata_id: int, db: Session = Depends(get_db)):
#     db_wisata = crud.delete_wisata(db, wisata_id)
#     if db_wisata is None:
#         raise HTTPException(status_code=404, detail="Wisata not found")
#     return db_wisata

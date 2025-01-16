from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from . import crud, schemas
from typing import List

router = APIRouter()

@router.get("", response_model=List[schemas.TransaksiOut])
async def read_transaksis(db: Session = Depends(get_db)):
    return crud.get_transaksis(db)

@router.post("", response_model=schemas.TransaksiCreate)
async def create_new_transaksi(transaksi: schemas.TransaksiCreate, db: Session = Depends(get_db)):
    return crud.create_transaksi(db, transaksi)

@router.get("/{transaksi_id}", response_model=schemas.TransaksiOut)
async def read_transaksi(transaksi_id: int, db: Session = Depends(get_db)):
    db_transaksi = crud.get_transaksi(db, transaksi_id)

    if db_transaksi is None:
        raise HTTPException(status_code = 404, detail="Transaksi Not Found")
    
    return db_transaksi

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

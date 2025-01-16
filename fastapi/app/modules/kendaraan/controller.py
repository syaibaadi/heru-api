from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from . import crud, schemas

router = APIRouter()

@router.get("", response_model=List[schemas.KendaraanResponse])
async def read_kendaraans(db: Session = Depends(get_db)):
    return crud.get_kendaraans(db)

@router.post("", response_model=schemas.KendaraanCreate)
async def create_kendaraan(kendaraan: schemas.KendaraanCreate, db: Session = Depends(get_db)):
    existing_kendaraan = db.query(crud.Kendaraan).filter(crud.Kendaraan.number == kendaraan.number).first()
    if existing_kendaraan:
        raise HTTPException(status_code=400, detail="Number Kendaraan already registered")
    return crud.create_kendaraan(db, kendaraan)

@router.get("/{kendaraan_id}", response_model=schemas.KendaraanResponse)
async def read_kendaraan(kendaraan_id: int, db: Session = Depends(get_db)):
    db_kendaraan = crud.get_kendaraan(db, kendaraan_id)

    if db_kendaraan is None:
        raise HTTPException(status_code = 404, detail="Kendaraan Not Found")
    
    return db_kendaraan

@router.put("/{kendaraan_id}", response_model=schemas.KendaraanResponse)
def update_kendaraan(kendaraan_id: int, kendaraan: schemas.KendaraanCreate, db: Session = Depends(get_db)):
    db_kendaraan = crud.update_kendaraan(db, kendaraan_id, kendaraan.nama)
    if db_kendaraan is None:
        raise HTTPException(status_code=404, detail="Kendaraan not found")
    return db_kendaraan

@router.delete("/{kendaraan_id}", response_model=schemas.KendaraanResponse)
def delete_wisata(kendaraan_id: int, db: Session = Depends(get_db)):
    db_kendaraan = crud.delete_kendaraan(db, kendaraan_id)
    if db_kendaraan is None:
        raise HTTPException(status_code=404, detail="Kendaraan not found")
    return db_kendaraan

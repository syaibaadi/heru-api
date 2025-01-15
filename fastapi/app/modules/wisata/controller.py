from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from . import crud, schemas

router = APIRouter()

@router.get("", response_model=list[schemas.WisataResponse])
async def read_wisatas(db: Session = Depends(get_db)):
    return crud.get_wisatas(db)

@router.post("", response_model=schemas.WisataCreate)
async def create_new_user(wisata: schemas.WisataCreate, db: Session = Depends(get_db)):
    existing_wisata = db.query(crud.Wisata).filter(crud.Wisata.nama == wisata.nama).first()
    if existing_wisata:
        raise HTTPException(status_code=400, detail="Wisata already registered")
    return crud.create_wisata(db, wisata)

@router.get("/{wisata_id}", response_model=schemas.WisataResponse)
async def read_user(wisata_id: int, db: Session = Depends(get_db)):
    db_wisata = crud.get_wisata(db, wisata_id)

    if db_wisata is None:
        raise HTTPException(status_code = 404, detail="User Not Found")
    
    return db_wisata

@router.put("/{wisata_id}", response_model=schemas.WisataResponse)
def update_wisata(wisata_id: int, wisata: schemas.WisataCreate, db: Session = Depends(get_db)):
    db_wisata = crud.update_wisata(db, wisata_id, wisata.nama)
    if db_wisata is None:
        raise HTTPException(status_code=404, detail="Wisata not found")
    return db_wisata

@router.delete("/{wisata_id}", response_model=schemas.WisataResponse)
def delete_wisata(wisata_id: int, db: Session = Depends(get_db)):
    db_wisata = crud.delete_wisata(db, wisata_id)
    if db_wisata is None:
        raise HTTPException(status_code=404, detail="Wisata not found")
    return db_wisata

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from . import crud, schemas
from typing import List

router = APIRouter()

@router.get("", response_model=List[schemas.UserResponse])
async def read_users_pelanggan(db: Session = Depends(get_db)):
    return crud.get_users_pelanggan(db)

@router.post("", response_model=schemas.UserResponse)
async def create_new_user_pelanggan(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(crud.User).filter(crud.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user_pelanggan(db, user)

@router.get("/{user_id}", response_model=schemas.UserResponse)
async def read_user_pelanggan(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_pelanggan(db, user_id)

    if db_user is None:
        raise HTTPException(status_code = 404, detail="User Not Found")
    
    return db_user

@router.put("/{user_id}", response_model=schemas.UserResponse)
def update_user_pelanggan(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.update_user_pelanggan(db, user_id, user.name, user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=schemas.UserResponse)
def delete_user_pelanggan(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user_pelanggan(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

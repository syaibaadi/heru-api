from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from . import crud, schemas

router = APIRouter()

@router.get("", response_model=list[schemas.AdminResponse])
async def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.post("", response_model=schemas.AdminResponse)
async def create_new_user(user: schemas.AdminCreate, db: Session = Depends(get_db)):
    existing_user = db.query(crud.Admin).filter(crud.Admin.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@router.get("/{user_id}", response_model=list[schemas.AdminResponse])
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)

    if db_user is None:
        raise HTTPException(status_code = 404, detail="User Not Found")
    
    return db_user

@router.put("/{user_id}", response_model=schemas.AdminResponse)
def update_user(user_id: int, user: schemas.AdminCreate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id, user.name, user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=schemas.AdminResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.database import SessionLocal
from src.users import schemas
from src.utils.db_queries import get_user_by_discriminant, get_users

router = APIRouter(tags=["users"], prefix="/users")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[schemas.User])
async def read_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users


@router.get("/{discriminant}", response_model=schemas.User)
async def read_user(discriminant: int, db: Session = Depends(get_db)):
    user = get_user_by_discriminant(db, discriminant)
    return user


@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.put("/{discriminant}")
async def update_status_user(discriminant: int, status: int, db: Session = Depends(get_db)):
    user = get_user_by_discriminant(db, discriminant)
    user.status = status
    db.commit()
    db.refresh(user)
    return user


@router.delete("/{discriminant}", response_model=schemas.User)
async def delete_user(discriminant: int, db: Session = Depends(get_db)):
    user = get_user_by_discriminant(db, discriminant)
    db.delete(user)
    db.commit()
    return user
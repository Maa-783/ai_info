from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.services import user_service

router = APIRouter()


@router.get("/", response_model=list[schemas.User])
def list_users(db: Session = Depends(deps.get_db)):
    return user_service.list_users(db)


@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(deps.get_db)):
    return user_service.create_user(db, user_in)


@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(deps.get_db)):
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
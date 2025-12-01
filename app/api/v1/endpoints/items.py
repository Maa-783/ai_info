from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.services import item_service

router = APIRouter()


@router.get("/", response_model=list[schemas.Item])
def list_items(db: Session = Depends(deps.get_db)):
    return item_service.list_items(db)


@router.post("/", response_model=schemas.Item, status_code=status.HTTP_201_CREATED)
def create_item(item_in: schemas.ItemCreate, db: Session = Depends(deps.get_db)):
    return item_service.create_item(db, item_in)


@router.get("/{item_id}", response_model=schemas.Item)
def get_item(item_id: int, db: Session = Depends(deps.get_db)):
    item = item_service.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item